import glob, statistics as st, torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

IMGS = sorted(glob.glob("/home/simonll4/projects/e-ovrt_datasets/datasets/raw/construction_site_safety/train/images/*.jpg"))[:12]
PROMPT = "person. helmet. vest. head."
M = "/home/simonll4/projects/e-ovrt_media-plane/models"
CKPTS = [
    ("mm-gdino-tiny ", f"{M}/mm-grounding-dino/original/mm_grounding_dino_tiny_o365v1_goldg_v3det"),
    ("mm-gdino-base ", f"{M}/mm-grounding-dino/original/mm_grounding_dino_base_all"),
    ("mm-gdino-large", f"{M}/mm-grounding-dino/original/mm_grounding_dino_large_all"),
    ("gdino-tiny(ok)", f"{M}/grounding-dino/original/grounding-dino-tiny"),
]
dev = "cuda" if torch.cuda.is_available() else "cpu"
for name, path in CKPTS:
    try:
        pr = AutoProcessor.from_pretrained(path)
        mo = AutoModelForZeroShotObjectDetection.from_pretrained(path).to(dev).eval()
    except Exception as e:
        print(f"{name}: NO CARGA -> {type(e).__name__}: {str(e)[:110]}"); continue
    ws, hs, per, deg, n = [], [], [], 0, 0
    for p in IMGS:
        im = Image.open(p).convert("RGB")
        inp = pr(images=im, text=PROMPT, return_tensors="pt").to(dev)
        with torch.no_grad():
            out = mo(**inp)
        r = pr.post_process_grounded_object_detection(
            out, inp["input_ids"], threshold=0.30, text_threshold=0.25,
            target_sizes=[(im.height, im.width)])[0]
        labs = r.get("text_labels", r.get("labels"))
        for b, lb in zip(r["boxes"].tolist(), labs):
            w, h = b[2]-b[0], b[3]-b[1]
            ws.append(w); hs.append(h); n += 1
            if w <= 1 or h <= 1: deg += 1
            if isinstance(lb, str) and "person" in lb and h > 0: per.append(w/h)
    if not n:
        print(f"{name}: 0 cajas en {len(IMGS)} imgs"); del mo; torch.cuda.empty_cache(); continue
    print(f"{name}: n={n:3d} | w med={st.median(ws):6.1f} min={min(ws):6.2f} | h med={st.median(hs):6.1f} min={min(hs):6.2f} "
          f"| degeneradas={deg} | person w/h med={st.median(per):.2f} (n={len(per)})" if per else
          f"{name}: n={n:3d} | w med={st.median(ws):6.1f} min={min(ws):6.2f} | h med={st.median(hs):6.1f} min={min(hs):6.2f} | degeneradas={deg} | sin person")
    del mo; torch.cuda.empty_cache()
