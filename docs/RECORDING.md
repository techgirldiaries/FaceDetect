# Recording and Capture Features

## Photo Capture

### How to capture

Press `c` during runtime to save a snapshot of the current frame.

### Output format

- Format: JPEG
- Location: `captures/` folder (created automatically)
- Filename: `capture_YYYYMMDD_HHMMSS.jpg`
- Example: `capture_20260220_143052.jpg`

### Notes

- Captured photo includes all overlays (face boxes, FPS counter, etc.)
- If privacy mode is active, the captured photo will include the privacy filter
- Terminal shows confirmation message with file path

## Video Recording

### How to record

Press `r` to start recording. Press `r` again to stop.

### Output format

- Format: AVI (XVID codec)
- Location: `recordings/` folder (created automatically)
- Filename: `recording_YYYYMMDD_HHMMSS.avi`
- Example: `recording_20260220_143115.avi`

### Recording indicator

When recording is active:

- Red `REC ●` indicator appears on screen (below FPS counter)
- All overlays and filters are recorded

### Notes

- Recording captures frame-by-frame at actual runtime FPS (not constant)
- If privacy mode is active during recording, all frames include the privacy filter
- Recording automatically stops when you quit the application
- Terminal shows start/stop confirmation messages with file path

## Privacy-Safe Recording

### Applying privacy to recordings

1. **Before starting recording**: Press `p` to enable blur or pixelate mode
2. **Start recording**: Press `r`
3. **All subsequent frames** in the video will have faces anonymised

### Toggling during recording

You can press `p` during an active recording to change privacy modes. The mode change applies immediately to subsequent frames.

## Storage Management

### Default locations

```text
project_root/
├── captures/          # Photo snapshots
└── recordings/        # Video recordings
```

### Disk space considerations

- Photos: ~50-500 KB each (depends on resolution)
- Videos: ~1-5 MB per minute (depends on resolution and FPS)

### Cleanup

Manually delete files from `captures/` and `recordings/` folders as needed. FaceDetect does not automatically delete or rotate saved files.

## Troubleshooting

### "Failed to save snapshot"

- Check write permissions for `captures/` folder
- Ensure sufficient disk space

### "Failed to start recording"

- Check write permissions for `recordings/` folder
- Ensure OpenCV VideoWriter codec (XVID) is available
- Try installing `opencv-contrib-python` if recording fails

### Video file won't play

- Install a codec pack (e.g., K-Lite Codec Pack on Windows)
- Try VLC Media Player which supports XVID natively
- Consider converting to MP4 using FFmpeg:

```bash
  ffmpeg -i recording_YYYYMMDD_HHMMSS.avi output.mp4
```
