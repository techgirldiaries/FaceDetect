# CLI Reference

## Synopsis

```bash
python main.py [OPTIONS]
```

## Options

### General

| Flag                   | Type  | Default                  | Description                                                     |
| ---------------------- | ----- | ------------------------ | --------------------------------------------------------------- |
| `--camera`             | int   | `0`                      | Camera device index (0 = default camera)                        |
| `--window-name`        | str   | `"Video Face Detection"` | OpenCV window title                                             |
| `--read-fail-sleep-ms` | float | `10.0`                   | Delay in milliseconds before retrying after camera read failure |

### Detection Model

| Flag      | Type | Default  | Description                     |
| --------- | ---- | -------- | ------------------------------- |
| `--model` | str  | `"haar"` | Detector model: `haar` or `dnn` |

### Haar Cascade Options

| Flag              | Type  | Default | Description                                         |
| ----------------- | ----- | ------- | --------------------------------------------------- |
| `--scale-factor`  | float | `1.3`   | Haar cascade scale factor for multi-scale detection |
| `--min-neighbors` | int   | `5`     | Minimum neighbors required for positive detection   |
| `--min-size`      | int   | `30`    | Minimum face size in pixels (width and height)      |

### DNN Options

| Flag                | Type  | Default | Description                                               |
| ------------------- | ----- | ------- | --------------------------------------------------------- |
| `--dnn-model-path`  | str   | `None`  | Path to DNN model weights (.caffemodel file)              |
| `--dnn-config-path` | str   | `None`  | Path to DNN model config (.prototxt file)                 |
| `--dnn-confidence`  | float | `0.6`   | Minimum confidence threshold (0.0-1.0) for DNN detections |

### Display

| Flag              | Type | Default | Description                           |
| ----------------- | ---- | ------- | ------------------------------------- |
| `--box-thickness` | int  | `2`     | Bounding box line thickness in pixels |

### Privacy

| Flag             | Type | Default  | Description                                         |
| ---------------- | ---- | -------- | --------------------------------------------------- |
| `--privacy-mode` | str  | `"none"` | Initial privacy mode: `none`, `blur`, or `pixelate` |

## Usage Examples

### Basic usage (Haar cascade)

```bash
python main.py
```

### Specify camera

```bash
python main.py --camera 1
```

### Use DNN model

```bash
python main.py --model dnn \
  --dnn-config-path deploy.prototxt \
  --dnn-model-path res10_300x300_ssd_iter_140000_fp16.caffemodel
```

### Start with privacy mode enabled

```bash
python main.py --privacy-mode blur
```

### Adjust detection sensitivity

```bash
python main.py --scale-factor 1.1 --min-neighbors 3 --min-size 20
```

### Custom window title

```bash
python main.py --window-name "My Face Detector"
```

## Exit Codes

| Code  | Meaning                                |
| ----- | -------------------------------------- |
| `0`   | Normal exit                            |
| `1`   | Consent denied or camera access error  |
| Other | Unexpected error (see terminal output) |
