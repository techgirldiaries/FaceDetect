# FaceDetect

Real-time webcam face detection with privacy controls, recording, and photo capture.

## Quick Start

### 1. Install

```bash
pip install opencv-python
```

### 2. Run

```bash
python main.py
```

On first launch, you'll be asked for camera consent. Type `yes` to proceed.

### 3. Controls

| Key | Action                                    |
| --- | ----------------------------------------- |
| `q` | Quit                                      |
| `c` | Capture photo                             |
| `r` | Start/stop recording                      |
| `p` | Toggle privacy mode (blur/pixelate faces) |

## Features

**Real-time face detection** — Haar cascade (fast) or DNN model (accurate)  
**Privacy modes** — Blur or pixelate faces in preview and recordings  
**Photo capture** — Save snapshots with `c` key  
**Video recording** — Record with `r` key, saves to `recordings/`  
**Consent management** — First-run consent prompt  
**Local processing** — No cloud, no data transmission

## Documentation

**[Installation Guide](docs/INSTALLATION.md)** — Detailed setup and DNN model download  
**[Keyboard Controls](docs/KEYBOARD_CONTROLS.md)** — All shortcuts and on-screen indicators  
**[Privacy & Consent](docs/PRIVACY.md)** — Data handling and compliance notes  
**[Recording Features](docs/RECORDING.md)** — Photo/video capture guide  
**[CLI Reference](docs/CLI_REFERENCE.md)** — All command-line options  
**[Troubleshooting](docs/TROUBLESHOOTING.md)** — Common issues and solutions

## Example Commands

### Basic usage (Haar cascade, default)

```bash
  python main.py
```

### With DNN model (better accuracy)

```bash
  python main.py --model dnn \
    --dnn-config-path deploy.prototxt \
    --dnn-model-path res10_300x300_ssd_iter_140000_fp16.caffemodel
```

### Start with privacy mode enabled

```bash
  python main.py --privacy-mode blur
```

## License

See [LICENSE.md](LICENSE.md) for terms.
See [CLI Reference](docs/CLI_REFERENCE.md) for all options.
