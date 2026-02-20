# Installation Guide

## Prerequisites

- Python 3.7 or higher
- Webcam/camera device
- Windows, macOS, or Linux

## Installation Steps

### 1. Install Python dependencies

```bash
pip install opencv-python
```

For development or additional features:

```bash
pip install opencv-contrib-python
```

### 2. Verify installation

```bash
python -c "import cv2; print(cv2.__version__)"
```

You should see the OpenCV version number (e.g., `4.x.x`).

## DNN Model Files (Optional)

For better accuracy, download DNN model files:

### Deploy configuration

```bash
curl -O https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
```

### Model weights

```bash
curl -O https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000_fp16.caffemodel
```

Place both files in the project root or specify paths with `--dnn-model-path` and `--dnn-config-path`.

## Troubleshooting Installation

### Camera access denied

On Windows, ensure camera permissions are enabled:

- Settings → Privacy → Camera → Allow desktop apps to access camera

### OpenCV import error

Try reinstalling:

```bash
pip uninstall opencv-python opencv-contrib-python
pip install opencv-python
```

### Missing haarcascade files

If you see "haarcascade data path unavailable", reinstall OpenCV or download the cascade file manually from the OpenCV GitHub repository.
