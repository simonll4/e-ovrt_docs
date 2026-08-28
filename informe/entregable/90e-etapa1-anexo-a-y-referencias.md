# 90e — Anexo A y Referencias de la Etapa 1 (material para §19 y para el listado global)

> **Extracción derivada (2026-08-27).** Este material **salió del entregable de la Etapa 1**
> por decisión del usuario: el `.docx` de la etapa contiene **solo el desarrollo** (§15 y §16).
> El Anexo A pertenece a §19 y el listado de referencias es global del informe — los arma el
> equipo, no el redactor de la etapa.
>
> **No se descarta, y hay una razón dura:** el cuerpo de §15 **cita la Tabla A.1**
> («en la Tabla A.1 del Anexo A se incluye una matriz ampliada…», §15.2.3) y §15.3.3 **cita la
> Tabla A.2**. Si esas tablas no llegan a §19, quedan dos remisiones colgadas en el informe.
>
> Lo que este material aporta, ya corregido en los cuatro pases:
> - **Tabla A.1** pasó de 12 a **20 filas** e incorpora **Grounding DINO Swin-T/Swin-L y
>   MM-Grounding-DINO**, que faltaban pese a ser los modelos del trabajo (E1-34).
> - Sus **licencias están corregidas** (E1-33/`AJ-1.09`): DINO-X y Grounding DINO 1.5 figuran
>   como «API cerrada; Apache-2.0 aplica al SDK, no a los pesos», no como Apache-2.0 a secas.
> - **Tabla A.2** reescrita en términos del límite de cada métrica frente a la alerta; la
>   antigua Tabla A.3 (servidores de medios) se eliminó por quedar sin uso (D-E1-9).
> - **83 entradas de referencia**, sin huérfanas y sin citas sin entrada, con las altas de los
>   cuatro pases (Kumar 2022, Lee 2023, OASIS 2019, Ultralytics 2026, Yuksekgonul 2023,
>   Thrush 2022) y `Luxonis` con su letra.

---

## 19. Anexos

### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario

El Anexo A reúne comparativas complementarias que respaldan el estado del arte sin sobrecargar el cuerpo principal. La Tabla A.1 amplía el catálogo de alternativas de detección open-vocabulary y modelos relacionados; la Tabla A.2 sintetiza el alcance y las limitaciones de las métricas MOT tratadas en la sección 15.3.3.

**Tabla A.1**

*Matriz ampliada de alternativas de detección open-vocabulary y modelos relacionados*

| **Modelo** | **Familia** | **Mecanismo visión-lenguaje** | **AP zero-shot reportado** | **Rendimiento reportado** | **Licencia / disponibilidad** |
| --- | --- | --- | --- | --- | --- |
| DINO-X | Transformer | Universal Object Prompt | 59,8 (LVIS-minival) | N/D | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| G-DINO 1.5 Pro | Transformer | Fusión cross-modal profunda | 55,7 (LVIS-minival) | N/D | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| G-DINO 1.5 Edge | Transformer | Fusión cross-modal optimizada | 36,2 (LVIS-minival) | 75,2 FPS (A100, TensorRT) | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| Grounding DINO Swin-L | Transformer | Feature Enhancer, selección de consultas guiada y decoder cross-modal | 52,5 (COCO); 26,1 mean AP (ODinW-35) | N/D | Apache-2.0 |
| Grounding DINO Swin-T | Transformer | Feature Enhancer, selección de consultas guiada y decoder cross-modal | 48,4 (COCO) | N/D | Apache-2.0 |
| MM-Grounding-DINO Tiny | Transformer | Pipeline unificado de grounding y detección | 50,4–50,6 (COCO); 35,7–41,4 (LVIS-minival) | N/D | Apache-2.0 |
| GLIP | Dynamic Head + Swin | Alineamiento región-palabra con fusión profunda | 49,8 (COCO); 26,9 (LVIS) | N/D | MIT |
| OV-DINO | Transformer | LASF + UniDI | 50,6 (COCO) | N/D | Apache-2.0 |
| OV-DETR | Deformable DETR | Matching condicional binario con prompts textuales o visuales | 17,4 novel (OV-LVIS); 29,4 AP50 novel (OV-COCO) | N/D | CC BY-NC-SA 4.0 |
| APE-L (D) | Transformer | Alineamiento por producto punto y encoder cross-modal | 59,6 caja (LVIS); 58,3 caja (COCO) | N/D | Apache-2.0 |
| LLMDet | Transformer + LLM | Coentrenamiento con LLM; LLM descartado en inferencia | 51,1 (LVIS-minival) | N/D | Apache-2.0 |
| DetCLIPv3 | Transformer | Formulación generativa con VLLM | 48,8 (LVIS-minival) | N/D | N/D |
| OWLv2 L/14 | ViT dual-encoder | Autoentrenamiento escalable | 44,6 (LVIS rare) | N/D | Apache-2.0 |
| Detic | Two-stage | Embeddings CLIP como pesos del clasificador de regiones | 17,8 rare (OV-LVIS); 27,8 novel AP50 (OV-COCO) | N/D | Apache-2.0 |
| T-Rex2 Swin-L | Transformer multimodal | Prompts textuales y visuales con fusión tardía | 46,7 texto / 46,8 visual (LVIS-minival) | N/D | IDEA License 1.0; uso no comercial |
| YOLOE-v8-L | One-stage | RepRTA + SAVPE + LRPC | 35,9 (LVIS-minival) | 102,5 FPS (T4, TensorRT) | AGPL-3.0 |
| YOLO-World-L | One-stage | RepVL-PAN contrastivo | 35,4 (LVIS-minival) | 52,0 FPS (V100, PyTorch) | GPL-3.0 |
| OmDet-Turbo-Base | Transformer para tiempo real | EFH + caché textual | 34,7 (LVIS-minival) | 100,2 FPS (A100, TensorRT + caché textual) | Apache-2.0 |
| YOLOE-v8-S | One-stage | RepRTA reparametrizable | 27,9 (LVIS-minival) | 305,8 FPS (T4, TensorRT) | AGPL-3.0 |
| Florence-2-L | Seq2Seq | Generación condicionada por instrucciones | 37,5 (COCO) | Variable | MIT |

Nota. Las cifras conservan el protocolo, el conjunto de evaluación y el hardware informados por cada fuente; por ello, no constituyen un benchmark homogéneo. N/D indica información no reportada o no comparable. En DINO-X y Grounding DINO 1.5, la licencia Apache-2.0 corresponde al SDK de acceso y no a pesos abiertos. Fuente: elaboración propia basada en Cheng et al. (2024), Fu et al. (2025), Jiang et al. (2024), L. H. Li et al. (2021), Liu et al. (2024), Minderer et al. (2023), Ren, Chen, et al. (2024), Ren, Jiang, et al. (2024), Shen et al. (2023), A. Wang et al. (2025), H. Wang et al. (2024), Xiao et al. (2024), Yao et al. (2024), Zang et al. (2022), T. Zhao et al. (2024), X. Zhao et al. (2024) y X. Zhou et al. (2022).

**Tabla A.2**

*Comparación conceptual de métricas MOT y sus límites para evaluar alertas temporales*

| **Métrica** | **Qué caracteriza** | **Sesgo principal** | **Límite respecto de las alertas** |
| --- | --- | --- | --- |
| MOTA | Errores acumulados de detección y cambios de identidad | Está fuertemente condicionada por falsos positivos y falsos negativos del detector | No mide persistencia, oportunidad ni resolución de episodios de alerta |
| IDF1 | Consistencia de identidad a lo largo de una secuencia | Privilegia la correspondencia de identidad y exige anotaciones de trayectorias | No mide la condición semántica ni el comportamiento temporal de la alerta |
| HOTA | Calidad combinada de detección, asociación y localización | Resume componentes del tracker y requiere referencia MOT explícita | No sustituye la evaluación por persona ni la evaluación por episodio temporal |

Nota. MOTA resume errores de detección y cambios de identidad; IDF1 enfatiza la continuidad de identidad; HOTA separa y combina detección, asociación y localización. Las tres caracterizan el seguimiento, pero no miden por sí mismas el estado semántico ni el episodio de alerta. Fuente: elaboración propia basada en Bernardin y Stiefelhagen (2008), Ristani et al. (2016) y Luiten et al. (2021).

## Referencias

Adžemović, M. (2025). Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art (arXiv:2506.13457). arXiv. https://doi.org/10.48550/arXiv.2506.13457

Agencia de Acceso a la Información Pública. (s. f.-a). Conocé tus derechos respecto a tus datos personales. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/derechos

Agencia de Acceso a la Información Pública. (s. f.-b). Videovigilancia: ¿Por qué hay que registrar bases de datos de videovigilancia y presentar el manual de tratamiento? Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/responsables/videovigilancia

Aharon, N., Orfaig, R., & Bobrovsky, B.-Z. (2022). BoT-SORT: Robust Associations Multi-Pedestrian Tracking (arXiv:2206.14651). arXiv. https://doi.org/10.48550/arXiv.2206.14651

Ahmad, H. M., y Rahimi, A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. Journal of Safety Science and Resilience, 6(2), 175–185. https://doi.org/10.1016/j.jnlssr.2024.09.002

Ahmad, I., Xiaohui Wei, Yu Sun, & Ya-Qin Zhang. (2005). Video transcoding: An overview of various techniques and research issues. IEEE Transactions on Multimedia, 7(5), 793–804. https://doi.org/10.1109/TMM.2005.854472

AILab-CVC. (2024, January 30). YOLO-World. GitHub. Retrieved January 21, 2026, from https://github.com/AILab-CVC/YOLO-World

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2014). Janus: A general purpose WebRTC gateway. Proceedings of the Conference on Principles, Systems and Applications of IP Telecommunications, 1–8. https://doi.org/10.1145/2670386.2670389

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2015). Performance analysis of the Janus WebRTC gateway. Proceedings of the 1st Workshop on All-Web Real-Time Systems, 1–7. https://doi.org/10.1145/2749215.2749223

Ananthanarayanan, G., Bahl, P., Bodik, P., Chintalapudi, K., Philipose, M., Ravindranath, L., & Sinha, S. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. Computer, 50(10), 58–67. https://doi.org/10.1109/MC.2017.3641638

Argentina. (2000). Ley N.º 25.326: Ley de Protección de los Datos Personales. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm

Argentina. (2001, noviembre 29). Decreto 1558/2001: Ley 25.326—Reglamentación. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368

Argentina. (2006, septiembre 19). Disposición 11/2006: Medidas de seguridad para el tratamiento y conservación de los datos personales. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-11-2006-120120

Argentina. (2015, febrero 24). Disposición 10/2015: Condiciones de licitud para las actividades de recolección y posterior tratamiento de imágenes digitales de personas con fines de seguridad. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-10-2015-243335

Axis Communications AB. (2015). Latency in live network video surveillance (63380/EN/R1/1504) [White paper]. https://www.axis.com/dam/public/9d/e4/5d/latency-in-live-network-video-surveillance-en-US-190945.pdf

Bachhuber, C., Steinbach, E., Freundl, M., & Reisslein, M. (2018). On the Minimization of Glass-to-Glass and Glass-to-Algorithm Delay in Video Communication. IEEE Transactions on Multimedia, 20(1), 238–252. https://doi.org/10.1109/TMM.2017.2726189

Bass, L., Clements, P., & Kazman, R. (2022). Software architecture in practice (Fourth edition). Addison-Wesley.

Bernardin, K., & Stiefelhagen, R. (2008). Evaluating multiple object tracking performance: The CLEAR MOT metrics. EURASIP Journal on Image and Video Processing, 2008(1), 1-10. https://doi.org/10.1155/2008/246309

Bewley, A., Ge, Z., Ott, L., Ramos, F., y Upcroft, B. (2016). Simple online and realtime tracking. En 2016 IEEE International Conference on Image Processing (ICIP) (pp. 3464-3468). IEEE. https://doi.org/10.1109/ICIP.2016.7533003

Cao, J., Pang, J., Weng, X., Khirodkar, R., & Kitani, K. (2023). Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9686–9696. https://doi.org/10.1109/CVPR52729.2023.00934

Card, S. K., Moran, T. P., & Newell, A. (2008). The psychology of human-computer interaction (Repr). Erlbaum.

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers (arXiv:2005.12872). arXiv. https://doi.org/10.48550/arXiv.2005.12872

Chen, J., & Ran, X. (2019). Deep Learning With Edge Computing: A Review. Proceedings of the IEEE, 107(8), 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977

Chen, X., & Zou, Z. (2025). Are large pre-trained vision language models effective construction safety inspectors? (arXiv:2508.11011). arXiv. https://doi.org/10.48550/arXiv.2508.11011

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 16901–16911). https://doi.org/10.1109/CVPR52733.2024.01599

Choi, L., & Greer, R. (2024). Evaluating cascaded methods of vision-language models for zero-shot detection and association of hardhats for increased construction safety (arXiv:2410.12225). arXiv. https://doi.org/10.48550/arXiv.2410.12225

Cugola, G., & Margara, A. (2012). Processing flows of information: From data stream to complex event processing. ACM Computing Surveys, 44(3), 1–62. https://doi.org/10.1145/2187671.2187677

DASH Industry Forum. (2020, marzo 27). Low-latency Modes for DASH. CR-Low-Latency-Live-r8. https://dashif.org/docs/CR-Low-Latency-Live-r8.pdf

Deber, J., Jota, R., Forlines, C., & Wigdor, D. (2015). How Much Faster is Fast Enough?: User Perception of Latency & Latency Improvements in Direct and Indirect Touch. Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, 1827–1836. https://doi.org/10.1145/2702123.2702300

Decreto 351/79 de 1979. Reglamentación de la Ley 19.587 de Higiene y Seguridad en el Trabajo. (1979, febrero 5). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/30000-34999/32030/dto351-1979-anexo1.htm

Decreto 911/96 de 1996. Reglamento de Higiene y Seguridad para la Industria de la Construcción. (1996, 5 de agosto). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/38568/texact.htm

Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K., & Leal-Taixé, L. (2020). MOT20: A benchmark for multi object tracking in crowded scenes (arXiv:2003.09003). arXiv. https://doi.org/10.48550/arXiv.2003.09003

Du, C., Lin, C., Jin, R., Chai, B., Yao, Y., & Su, S. (2024). Exploring the State-of-the-Art in Multi-Object Tracking: A Comprehensive Survey, Evaluation, Challenges, and Future Directions. Multimedia Tools and Applications, 83(29), 73151–73189. https://doi.org/10.1007/s11042-023-17983-2

Du, Y., Wei, F., Zhang, Z., Shi, M., Gao, Y., & Li, G. (2022). Learning to prompt for open-vocabulary object detection with vision-language model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 14084-14093). https://doi.org/10.1109/CVPR52688.2022.01369

European Data Protection Board. (2020, enero 30). Guidelines 3/2019 on processing of personal data through video devices (Version 2.0). EDPB. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en

Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., & Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. International Journal of Computer Vision, 88(2), 303–338. https://doi.org/10.1007/s11263-009-0275-4

Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., & Zheng, W.-S. (2025, January 31). [2501.18954] LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2501.18954

Gettys, J., & Nichols, K. (2012). Bufferbloat: Dark buffers in the internet. Communications of the ACM, 55(1), 57–65. https://doi.org/10.1145/2063176.2063196

Google. (2022, May). owlvit-large-patch14. Hugging Face. https://huggingface.co/google/owlvit-large-patch14

Google. (2023, June). owlv2-base-patch16-ensemble. Hugging Face. https://huggingface.co/google/owlv2-base-patch16-ensemble

Gupta, A., Dollár, P., & Girshick, R. (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation (arXiv:1908.03195). arXiv. https://doi.org/10.48550/arXiv.1908.03195

IDEA-Research. (2024a, noviembre 20). DINO-X-API: A unified vision model for open-world object detection and understanding [Repositorio de código]. GitHub. https://github.com/IDEA-Research/DINO-X-API

IDEA-Research. (2024c, mayo 18). GroundingDINO: Official implementation of “Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection” [Repositorio de código]. GitHub. https://github.com/IDEA-Research/GroundingDINO

Iorga, M., Feldman, L., Barton, R., Martin, M. J., Goren, N., & Mahmoudi, C. (2018). Fog computing conceptual model (NIST SP 500-325; p. NIST SP 500-325). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.500-325

ISO. (2018). ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use. ISO. https://www.iso.org/standard/63787.html

ISO. (2023). ISO/IEC 42001:2023—Artificial intelligence management system. ISO. https://www.iso.org/standard/42001

ISO/IEC. (2022). Information technology—Dynamic adaptive streaming over HTTP (DASH)—Part 1: Media presentation description and segment formats. ISO/IEC 23009-1:2022. https://www.iso.org/standard/83314.html

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy (arXiv:2403.14610). arXiv. https://doi.org/10.48550/arXiv.2403.14610

Keranen, A., Holmberg, C., & Rosenberg, J. (2018). Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal (No. RFC8445; p. RFC8445). RFC Editor. https://doi.org/10.17487/RFC8445

Khattak, M. U., Rasheed, H., Maaz, M., Khan, S., & Khan, F. S. (2023). MaPLe: Multi-modal Prompt Learning (arXiv:2210.03117). arXiv. https://doi.org/10.48550/arXiv.2210.03117

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13), 3521-3526. https://doi.org/10.1073/pnas.1611835114

Kreutz, D., Ramos, F. M. V., Esteves Verissimo, P., Esteve Rothenberg, C., Azodolmolky, S., & Uhlig, S. (2015). Software-Defined Networking: A Comprehensive Survey. Proceedings of the IEEE, 103(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kumar, A., Raghunathan, A., Jones, R. M., Ma, T., & Liang, P. (2022). Fine-tuning can distort pretrained features and underperform out-of-distribution. International Conference on Learning Representations. https://arxiv.org/abs/2202.10054

Kurose, J. F., & Ross, K. W. (2021). Computer networking: A top-down approach (Eighth edition). Pearson.

Lee, Y., Chen, A. S., Tajwar, F., Kumar, A., Yao, H., Liang, P., & Finn, C. (2023). Surgical fine-tuning improves adaptation to distribution shifts. International Conference on Learning Representations. https://arxiv.org/abs/2210.11466

Ley 19.587 de 1972. Ley de Higiene y Seguridad en el Trabajo. (1972). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/17612/norma.htm

Li, L. H., Zhang, P., Zhang, H., Yang, J., Li, C., Zhong, Y., Wang, L., Yuan, L., Zhang, L., Hwang, J.-N., Chang, K.-W., & Gao, J. (2021). Grounded language-image pre-training (arXiv:2112.03857). arXiv. https://doi.org/10.48550/arXiv.2112.03857

Li, S., Fischer, T., Ke, L., Ding, H., Danelljan, M., & Yu, F. (2023). OVTrack: Open-Vocabulary Multiple Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5567–5577. https://doi.org/10.1109/CVPR52729.2023.00539

Li, S., Ren, H., Xie, X., & Cao, Y. (2025). A Review of Multi‐Object Tracking in Recent Times. IET Computer Vision, 19(1), e70010. https://doi.org/10.1049/cvi2.70010

Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollar, P. y Zitnick, C. L. (2014). Microsoft COCO: Common objects in context. En D. Fleet, T. Pajdla, B. Schiele y T. Tuytelaars (Eds.), Computer Vision - ECCV 2014 (Vol. 8693, pp. 740-755). Springer. https://doi.org/10.1007/978-3-319-10602-1_48

Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., Zhu, J., & Zhang, L. (2024). Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection. In Computer Vision - ECCV 2024 (pp. 38-55). Springer. https://doi.org/10.1007/978-3-031-72970-6_3

Luiten, J., Os̆ep, A., Dendorfer, P., Torr, P., Geiger, A., Leal-Taixé, L., & Leibe, B. (2021). HOTA: A Higher Order Metric for Evaluating Multi-object Tracking. International Journal of Computer Vision, 129(2), 548–578. https://doi.org/10.1007/s11263-020-01375-2

Luo, W., Xing, J., Milan, A., Zhang, X., Liu, W., & Kim, T.-K. (2021). Multiple object tracking: A literature review. Artificial Intelligence, 293, 103448. https://doi.org/10.1016/j.artint.2020.103448

Luxonis. (s. f.-b). OAK-D Pro PoE [Documentación de hardware]. Luxonis Docs. https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20PoE

May, W. (2017). HTTP Live Streaming (R. Pantos, Ed.; No. RFC8216; p. RFC8216). RFC Editor. https://doi.org/10.17487/RFC8216

Microsoft. (2024, June). Florence-2-large. Hugging Face. https://huggingface.co/microsoft/Florence-2-large

Milan, A., Leal-Taixe, L., Reid, I., Roth, S., & Schindler, K. (2016). MOT16: A Benchmark for Multi-Object Tracking (arXiv:1603.00831). arXiv. https://doi.org/10.48550/arXiv.1603.00831

Minderer, M., Gritsenko, A., & Houlsby, N. (2023). Scaling open-vocabulary object detection (arXiv:2306.09683). arXiv. https://doi.org/10.48550/arXiv.2306.09683

Minderer, M., Gritsenko, A., Stone, A., Neumann, M., Weissenborn, D., Dosovitskiy, A., Mahendran, A., Arnab, A., Dehghani, M., Shen, Z., Wang, X., Zhai, X., Kipf, T., & Houlsby, N. (2022). Simple open-vocabulary object detection with vision transformers. In Computer Vision – ECCV 2022 (pp. 728–755). Springer. https://doi.org/10.1007/978-3-031-20080-9_42

Nakagawa, K., Tsukada, M., Shima, K., & Esaki, H. (2021). WebRTC-based measurement tool for peer-to-peer applications and preliminary findings with real users. Asian Internet Engineering Conference, 1–8. https://doi.org/10.1145/3497777.3498544

NVIDIA. (2024). DeepStream SDK 8.0 for NVIDIA dGPU/X86 and Jetson—DeepStream documentation. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Release_notes.html

NVIDIA. (s. f.-g). Grounding DINO. NVIDIA TAO Toolkit Documentation. Recuperado el 27 de agosto de 2026, de https://docs.nvidia.com/tao/tao-toolkit/latest/text/cv_finetuning/pytorch/object_detection/grounding_dino.html

NVIDIA. (s. f.-h). NVIDIA Triton Inference Server. Recuperado el 27 de agosto de 2026, de https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html

OASIS. (2019). MQTT Version 5.0. OASIS Standard. https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html

ONVIF. (2019). ONVIF Profile S Specification (ONVIF Profile S). ONVIF. https://www.onvif.org/wp-content/uploads/2019/12/ONVIF_Profile_-S_Specification_v1-3.pdf

Organisation for Economic Co-operation and Development. (2019, mayo 1). OECD AI Principles overview. OECD. https://oecd.ai/en/ai-principles

Otgonbold, M.-E., Gochoo, M., Alnajjar, F. S., Ali, L., Tan, T.-H., Hsieh, J.-W., y Chen, P.-Y. (2022). SHEL5K: An extended dataset and benchmarking for safety helmet detection. Sensors, 22(6), 2315. https://doi.org/10.3390/s22062315

Pantos, R. (2025). HTTP Live Streaming 2nd Edition (Internet-Draft). Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/18/

Parmar, H., & Thornburgh, M. (2012). Adobe’s Real Time Messaging Protocol. Adobe. https://ptacts.uspto.gov/ptacts/public-informations/petitions/1557060/download-documents?artifactId=CX29dwexemvGTAgu1npsGb4QtKzyjACHSNYXLhjJp5m1SpQS4AAf-3A

Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., & Sutskever, I. (2021). Learning Transferable Visual Models From Natural Language Supervision (arXiv:2103.00020). arXiv. https://doi.org/10.48550/arXiv.2103.00020

Rasaee, H., Koleilat, T., & Rivaz, H. (2025). Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models. IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 72(10), 1414-1425. https://doi.org/10.1109/TUFFC.2025.3605285

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024). DINO-X: A unified vision model for open-world object detection and understanding (arXiv:2411.14347). arXiv. https://doi.org/10.48550/arXiv.2411.14347

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection (Versión 2). arXiv. https://doi.org/10.48550/ARXIV.2405.10300

Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., Zeng, Z., Zhang, H., Li, F., Yang, J., Li, H., Jiang, Q., & Zhang, L. (2024). Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks (arXiv:2401.14159). arXiv. https://doi.org/10.48550/arXiv.2401.14159

Ristani, E., Solera, F., Zou, R., Cucchiara, R., & Tomasi, C. (2016). Performance Measures and a Data Set for Multi-target, Multi-camera Tracking. En G. Hua & H. Jégou (Eds.), Computer Vision – ECCV 2016 Workshops (Vol. 9914, pp. 17–35). Springer International Publishing. https://doi.org/10.1007/978-3-319-48881-3_2

Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which Protocol Should You Choose? (Update). Wowza Media Systems. Wowza Blog. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose

Satyanarayanan, M. (2017). The Emergence of Edge Computing. Computer, 50(1), 30–39. https://doi.org/10.1109/MC.2017.9

Schulzrinne, H., Casner, S., Frederick, R., & Jacobson, V. (2003). RTP: A Transport Protocol for Real-Time Applications (No. RFC3550; p. RFC3550). RFC Editor. https://doi.org/10.17487/rfc3550

Schulzrinne, H., Rao, A., & Lanphier, R. (1998). Real Time Streaming Protocol (RTSP) (No. RFC2326; p. RFC2326). RFC Editor. https://doi.org/10.17487/rfc2326

Schulzrinne, H., Rao, A., Lanphier, R., & Westerlund, M. (2016). Real-Time Streaming Protocol Version 2.0 (M. Stiemerling, Ed.; No. RFC7826; p. RFC7826). RFC Editor. https://doi.org/10.17487/RFC7826

Sharabayko, M. P., Sharabayko, M. A., Dube, J., Kim, J., & Kim, J. (2024). The SRT Protocol (Internet-Draft (working copy)). Internet Engineering Task Force. https://haivision.github.io/srt-rfc/draft-sharabayko-srt.html

Shen, Y., Fu, C., Chen, P., Zhang, M., Li, K., Sun, X., Wu, Y., Lin, S., & Ji, R. (2023, December 4). Aligning and Prompting Everything All at Once for Universal Visual Perception. arXiv. https://arxiv.org/abs/2312.02153

Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal, 3(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198

Sonono, T. (2019). Interoperable Retransmission Protocols with Low Latency and Constrained Delay: A Performance Evaluation of RIST and SRT [Master’s thesis, KTH Royal Institute of Technology]. https://www.diva-portal.org/smash/get/diva2:1335907/FULLTEXT01.pdf

SRT. (1997, julio 7). Resolución SRT 51/97 de 1997. Mecanismo Preventivo de Control en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/44588/norma.htm

SRT. (1998, marzo 31). Resolución SRT 35/98 de 1998. Coordinación de Programas de Seguridad en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/50000-54999/50188/norma.htm

SRT. (s. f.). Programa de Construcción. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/srt/prevencion/programas/construccion

THU-MIG. (2025). THU-MIG / yoloe: YOLOE: Real-Time Seeing Anything. GitHub. https://github.com/THU-MIG/yoloe

Thrush, T., Jiang, R., Bartolo, M., Singh, A., Williams, A., Kiela, D., & Ross, C. (2022). Winoground: Probing vision and language models for visio-linguistic compositionality (arXiv:2204.03162). arXiv. https://doi.org/10.48550/arXiv.2204.03162

Ucar, A., Ro, S., Satwika, S., Gayathri, P. Y., & Balsha, M. G. (2025). Fine-Tuning Florence2 for Enhanced Object Detection in Un-constructed Environments: Vision-Language Model Approach (arXiv:2503.04918). arXiv. https://doi.org/10.48550/arXiv.2503.04918

Ultralytics. (2026). Ultralytics YOLO26. https://docs.ultralytics.com/models/yolo26/

UNESCO. (2021). Recommendation on the ethics of artificial intelligence. https://unesdoc.unesco.org/ark:/48223/pf0000380455

Video Services Forum. (2020). Reliable Internet Stream Transport (RIST) protocol specification – Simple profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-1_2020_06_25.pdf

Video Services Forum. (2024). Reliable Internet Stream Transport (RIST) Protocol Specification – Main Profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-2_2024_06_12.pdf

Wang, A., Liu, L., Chen, H., Lin, Z., Han, J., & Ding, G. (2025). YOLOE: Real-Time Seeing Anything (arXiv:2503.07465). arXiv. https://doi.org/10.48550/arXiv.2503.07465

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024). OV-DINO: Unified open-vocabulary detection with language-aware selective fusion (arXiv:2407.07844). arXiv. https://doi.org/10.48550/arXiv.2407.07844

Wang, H., Zhang, X., Chen, H., Xu, Y., & Ma, Z. (2022). Inferring End-to-End Latency in Live Videos. IEEE Transactions on Broadcasting, 68(2), 517–529. https://doi.org/10.1109/TBC.2021.3071060

Wang, Z., Wu, Y., Yang, L., Thirunavukarasu, A., Evison, C., y Zhao, Y. (2021). Fast personal protective equipment detection for real construction sites using deep learning approaches. Sensors, 21(10), 3478. https://doi.org/10.3390/s21103478

Wojke, N., Bewley, A., & Paulus, D. (2017). Simple online and realtime tracking with a deep association metric. 2017 IEEE International Conference on Image Processing (ICIP), 3645–3649. https://doi.org/10.1109/ICIP.2017.8296962

World Wide Web Consortium. (2025). WebRTC: Real-Time Communication in Browsers (W3C Recommendation). World Wide Web Consortium. https://www.w3.org/TR/webrtc/

Xiao, B., Wu, H., Xu, W., Dai, X., Hu, H., Lu, Y., Zeng, M., Liu, C., & Yuan, L. (2024). Florence-2: Advancing a unified representation for a variety of vision tasks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4818–4829). https://doi.org/10.1109/CVPR52733.2024.00461

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024). DetCLIPv3: Towards versatile generative open-vocabulary object detection (arXiv:2404.09216). arXiv. https://doi.org/10.48550/arXiv.2404.09216

Yousefpour, A., Fung, C., Nguyen, T., Kadiyala, K., Jalali, F., Niakanlahiji, A., Kong, J., & Jue, J. P. (2019). All one needs to know about fog computing and related edge computing paradigms: A complete survey. Journal of Systems Architecture, 98, 289–330. https://doi.org/10.1016/j.sysarc.2019.02.009

Yuksekgonul, M., Bianchi, F., Kalluri, P., Jurafsky, D., & Zou, J. (2023). When and why vision-language models behave like bags-of-words, and what to do about it? International Conference on Learning Representations. https://arxiv.org/abs/2210.01936

Zang, Y., Li, W., Zhou, K., Huang, C., & Loy, C. C. (2022, March 22). [2203.11876] Open-Vocabulary DETR with Conditional Matching. arXiv. https://arxiv.org/abs/2203.11876

Zareian, A., Rosa, K. D., Hu, D. H., & Chang, S.-F. (2021). Open-Vocabulary Object Detection Using Captions (arXiv:2011.10678). arXiv. https://doi.org/10.48550/arXiv.2011.10678

Zhang, H., Zhang, P., Hu, X., Chen, Y.-C., Li, L. H., Dai, X., Wang, L., Yuan, L., Hwang, J.-N., & Gao, J. (2022). GLIPv2: Unifying Localization and Vision-Language Understanding (arXiv:2206.05836). arXiv. https://doi.org/10.48550/arXiv.2206.05836

Zhang, Y., Sun, P., Jiang, Y., Yu, D., Weng, F., Yuan, Z., Luo, P., Liu, W., & Wang, X. (2022). ByteTrack: Multi-object Tracking by Associating Every Detection Box. En S. Avidan, G. Brostow, M. Cissé, G. M. Farinella, & T. Hassner (Eds.), Computer Vision – ECCV 2022 (Vol. 13682, pp. 1–21). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-20047-2_1

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head (arXiv:2403.06892). arXiv. https://doi.org/10.48550/arXiv.2403.06892

Zhao, X., Chen, Y., Xu, S., Li, X., Wang, X., Li, Y., & Huang, H. (2024). An Open and Comprehensive Pipeline for Unified Object Grounding and Detection (arXiv:2401.02361). arXiv. https://doi.org/10.48550/arXiv.2401.02361

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022b). Learning to Prompt for Vision-Language Models. International Journal of Computer Vision, 130(9), 2337–2348. https://doi.org/10.1007/s11263-022-01653-1

Zhou, X., Girdhar, R., Joulin, A., Krähenbühl, P., & Misra, I. (2022). Detecting twenty-thousand classes using image-level supervision (arXiv:2201.02605). arXiv. https://doi.org/10.48550/arXiv.2201.02605
