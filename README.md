# CSW-YOLO: Fire Detection with YOLO11

Improved YOLO11 for fire and smoke detection with attention mechanisms, multi-scale feature enhancement, and dynamic loss focusing.

> ⚠️ **Status: Active Development (Started 2026-04)**
> 
> This repository is the second-generation codebase for the CSW-YOLO project. It is under active development as we port the method from our original (non-standard) dataset to the public **D-Fire benchmark**, and extend experiments with cross-dataset evaluation and comparisons against recent fire-detection-specific SotA methods.
> 
> Final results, pretrained weights, and the final version of the paper will be updated here before submission.

---

## Overview

CSW-YOLO introduces three structural modifications to the YOLO11n baseline to improve fire and smoke detection performance:

1. **CBAM attention module** inserted at each of the three detection branches in the head network, enabling per-scale feature refinement along both channel and spatial dimensions.
2. **SPPeLAN module** replacing the default SPPF at the end of the backbone, combining spatial pyramid pooling with efficient layer aggregation for richer multi-scale context.
3. **WIoU loss function** replacing CIoU, employing a dynamic non-monotonic focusing mechanism that reduces sensitivity to low-quality training samples.

The method is evaluated on the **D-Fire dataset** (21,000+ images, fire & smoke classes), which is a widely-used public benchmark for fire detection. Cross-dataset generalization is further evaluated on the **FLAME dataset**.

---

## Repository Structure
CSW-YOLO-fire-detection/
├── ultralytics/              # Official Ultralytics source (modified)
│   └── ultralytics/          # Core package (CBAM/SPPeLAN/WIoU changes go here)
├── configs/                  # Model YAMLs and dataset configs
├── scripts/                  # Training, evaluation, and utility scripts
├── results/                  # Experiment outputs (organized per experiment)
├── weights/                  # Pretrained weights (see Releases for trained models)
├── docs/                     # Experiment log and documentation
├── requirements.txt
├── README.md
└── LICENSE
---

## Environment

Experiments are conducted under the following environment:

| Component | Version |
|---|---|
| OS | Windows 11 |
| Python | 3.11.14 |
| PyTorch | 2.10.0 (CUDA 12.8) |
| Ultralytics | 8.4.x (installed from source, editable) |
| GPU | NVIDIA GeForce RTX 5060 |

See [`requirements.txt`](requirements.txt) for the full dependency list.

---

## Installation

```bash
# 1. Clone this repository
git clone https://github.com/WexxHo/CSW-YOLO-fire-detection.git
cd CSW-YOLO-fire-detection

# 2. Create a conda environment
conda create -n csw-yolo python=3.11 -y
conda activate csw-yolo

# 3. Install PyTorch (adjust CUDA version to match your system)
# See https://pytorch.org/ for the correct command
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

# 4. Install Ultralytics in editable mode (from our modified source)
cd ultralytics
pip install -e .
cd ..

# 5. Install remaining dependencies
pip install -r requirements.txt
```

---

## Datasets

This project uses two public benchmark datasets:

- **D-Fire** (primary): https://github.com/gaiasd/DFireDataset — used for training and in-domain evaluation.
- **FLAME** (cross-dataset): https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs — used for cross-dataset generalization testing only (inference, no training).

Datasets should be placed **outside** the repository (e.g., `G:\DL\datasets\D-Fire\`) and referenced via the YAML configs in `configs/`. See `configs/dfire.yaml` (to be added) for the expected path format.

---

## Experiments

The planned experimental design comprises 15 core experiments organized into four blocks:

| Block | Purpose | Experiments |
|---|---|---|
| **A** | Module ablation on D-Fire | 8 (baseline + 3 single-module + 3 dual-module + full CSW-YOLO) |
| **B** | SotA comparison on D-Fire | 5 (YOLOv8n, YOLOv10n, RT-DETR-L, plus 2 fire-detection-specific methods) |
| **C** | Attention mechanism comparison | 4 (SE, CA, ECA, SimAM vs CBAM) |
| **D** | Cross-dataset inference | Inference only on FLAME / other external set |

Detailed results and training logs will be added to `results/` and `docs/experiment_log.md` as experiments progress.

---

## Reproduction

Instructions for reproducing individual experiments will be added as they are completed.
(Placeholder — see `scripts/README.md` for usage once scripts are implemented.)

---

## Related Publication

This repository accompanies the manuscript:

> **CSW-YOLO: improved YOLO11 for fire detection with attention and multi-scale feature enhancement**  
> Qinkun Xu, Siyao He, Hanzhang Cheng  
> Southwest University of Science and Technology  
> *Manuscript in preparation / under revision.*

Citation information (BibTeX) will be provided upon acceptance.

---

## Acknowledgments

This project builds upon the excellent [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics) framework. We thank the authors of the [D-Fire dataset](https://github.com/gaiasd/DFireDataset) and [CBAM](https://github.com/Jongchan/attention-module) for making their work publicly available.

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.