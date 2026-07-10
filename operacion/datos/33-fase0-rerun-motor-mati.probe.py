"""Reproduce el conteo de items EPP 'disputados' del doc 33.

Un item disputado es aquel cuyo centro cae en la region de mas de una persona:
es la unica situacion en la que el matching bipartito 1:1 puede diferir del
matching por contencion. El resultado (0 disputados) explica por que el motor
nuevo produce alertas identicas al viejo sobre el BENCH.

Uso:
    cd e-ovrt_control-plane
    .venv/bin/python <ruta_a_este_script>
"""
import sys
from collections import Counter

sys.path.insert(0, "/home/simonll4/projects/e-ovrt_control-plane/src")

from eovrt_control.config import load_patterns_file
from eovrt_control.contracts.media import DetectionEvent
from eovrt_control.engine.evaluators.spatial_absence import (
    _center_inside_region,
    _matches_detection,
    _region_bbox,
)

DET = (
    "/home/simonll4/projects/e-ovrt_media-plane/runs/"
    "run_20260704_205708_dbe_grounding_dino_96b2b0/detections.jsonl"
)
PATTERNS = "/home/simonll4/projects/e-ovrt_control-plane/configs/patterns/cr01_cr02_v1.yaml"

patterns = {p.id: p for p in load_patterns_file(PATTERNS).pattern_set.patterns}
stats: Counter = Counter()

for line in open(DET):
    event = DetectionEvent.model_validate_json(line)
    for pid, pattern in patterns.items():
        subjects = [
            d
            for d in event.detections
            if _matches_detection(d, pattern.subject_class)
            and d.confidence >= pattern.evidence.min_subject_confidence
        ]
        items = [
            d
            for d in event.detections
            if _matches_detection(d, pattern.required_absent_class)
            and d.confidence >= pattern.evidence.min_absent_class_confidence
        ]
        regions = [_region_bbox(s.bbox_xyxy, pattern) for s in subjects]

        stats[f"{pid}:units"] += 1
        stats[f"{pid}:subjects"] += len(subjects)
        stats[f"{pid}:items"] += len(items)
        if len(subjects) > 1:
            stats[f"{pid}:units_multisubject"] += 1

        for item in items:
            owners = sum(1 for region in regions if _center_inside_region(item, region))
            if owners > 1:
                stats[f"{pid}:items_DISPUTADOS"] += 1
            elif owners == 1:
                stats[f"{pid}:items_1owner"] += 1
            else:
                stats[f"{pid}:items_0owner"] += 1

for key in sorted(stats):
    print(f"{key:32s} {stats[key]}")
