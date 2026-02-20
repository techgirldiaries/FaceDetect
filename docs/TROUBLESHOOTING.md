# Troubleshooting

## Common Issues

### Camera Issues

#### "Unable to open camera index: 0"

**Cause**: Camera not available, in use, or permissions denied.

**Solutions**:

1. Check if another application is using the camera
2. Verify camera permissions:
   - **Windows**: Settings -> Privacy -> Camera -> Allow desktop apps
   - **macOS**: System Preferences -> Security & Privacy -> Camera
   - **Linux**: Check `/dev/video*` permissions
3. Try a different camera index: `--camera 1`
4. Test camera with another app to verify it works

#### Camera feed is black or frozen

**Solutions**:

1. Disconnect and reconnect the camera
2. Restart the application
3. Update camera drivers (Windows)
4. Try `--read-fail-sleep-ms 100` for slower cameras

### Window Issues

#### Window keeps reopening after closing

**Fixed in current version**. If you still experience this:

1. Use `q` key to exit instead of clicking X
2. Update to the latest version
3. Report issue with OpenCV version: `python -c "import cv2; print(cv2.__version__)"`

#### Window doesn't appear

**Solutions**:

1. Check if window is behind other windows
2. Verify OpenCV GUI support: `python -c "import cv2; print(cv2.getBuildInformation())"`
3. Try `--window-name "Test"` with a different name
4. On Linux, ensure X11 or Wayland display is available

### Detection Issues

#### No faces detected

**Solutions**:

1. **Lighting**: Ensure adequate lighting on faces
2. **Distance**: Move closer or farther from camera
3. **Angle**: Face camera directly (frontal face)
4. **Sensitivity**: Lower detection threshold:

```bash
   python main.py --scale-factor 1.1 --min-neighbors 3 --min-size 20
```

5. **Try DNN model**: Often more accurate than Haar cascade

#### Too many false positives

**Solutions**:

1. Increase detection strictness:

   ```bash
   python main.py --scale-factor 1.5 --min-neighbors 7 --min-size 50
   ```

2. For DNN model, increase confidence for accuracy: `--dnn-confidence 0.8`

### DNN Model Issues

#### "Failed to load cascade classifier" or "DNN detector requires model and config paths"

**Solutions**:

1. Download model files (see [INSTALLATION](INSTALLATION.md))
2. Verify file paths are correct and files exist
3. Use absolute paths: `--dnn-model-path "C:\path\to\model.caffemodel"`

#### DNN model runs very slowly

**Solutions**:

1. DNN models are more accurate but slower than Haar
2. Consider using Haar for real-time: `--model haar`
3. Reduce camera resolution (requires code modification)
4. Use GPU-enabled OpenCV build if available

### Privacy and Recording Issues

#### Privacy mode doesn't apply to recordings

**Cause**: Privacy mode must be active before/during recording.

**Solution**: Press `p` to enable privacy mode BEFORE pressing `r` to start recording.

#### Recording file is corrupted or won't play

**Solutions**:

1. Install VLC Media Player or K-Lite Codec Pack
2. Ensure recording was stopped properly (press `r` or `q` to exit)
3. Try converting with FFmpeg:
   ```bash
   ffmpeg -i input.avi -c:v libx264 output.mp4
   ```

#### "VideoWriter_fourcc not available"

**Solutions**:

1. Install full OpenCV build: `pip install opencv-contrib-python`
2. Try alternative codecs (requires code modification)

### Performance Issues

#### Low FPS (<10)

**Solutions**:

1. Use Haar cascade instead of DNN: `--model haar`
2. Close other resource-intensive applications
3. Reduce detection frequency (requires code modification)
4. Lower camera resolution (requires code modification)

#### High CPU usage

**Solutions**:

1. Increase `--min-size` to detect only larger faces
2. Use `--read-fail-sleep-ms` to add frame delay
3. Close unnecessary background applications

### Consent Issues

#### Consent prompt doesn't appear

**Cause**: Settings file already exists.

**Solution**: Delete settings file and restart:

- **Windows**: `del %APPDATA%\FaceDetect\settings.json`
- **macOS/Linux**: `rm ~/FaceDetect/settings.json`

#### Consent denied but want to re-enable

**Solution**: Same as above - delete settings file and restart.

## Platform-Specific Issues

### Windows

#### Camera access denied even with permissions

1. Run as administrator (right-click -> Run as administrator)
2. Check Windows Camera app works first
3. Disable camera privacy mode in Settings

### macOS

#### "operation not permitted" error

1. Grant Terminal camera permissions in System Preferences
2. Run Python directly (not through IDE) if permissions issue persists

### Linux

#### "/dev/video0: Permission denied"

```bash
sudo usermod -a -G video $USER
# Log out and log back in
```

## Getting Help

If your issue isn't listed here:

1. Check GitHub Issues: https://github.com/techgirldiaries/FaceDetect/issues
2. Provide the following information:
   - OS and version
   - Python version: `python --version`
   - OpenCV version: `python -c "import cv2; print(cv2.__version__)"`
   - Full error message from terminal
   - Command used to run the application
3. Create a new issue with details

## Debug Mode

For detailed debugging, run with Python in verbose mode:

```bash
python -v main.py
```

This will show import paths and help identify module issues.
