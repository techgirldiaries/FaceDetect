# Keyboard Controls

## Main Controls

| Key | Action  | Description                                                   |
| --- | ------- | ------------------------------------------------------------- |
| `q` | Quit    | Exit application and close camera                             |
| `c` | Capture | Save current frame as JPG to `captures/` folder               |
| `r` | Record  | Toggle video recording on/off (saves to `recordings/` folder) |
| `p` | Privacy | Cycle through privacy modes: none → blur → pixelate → none    |

## Privacy Modes

### None (default)

- No privacy filtering applied
- Faces visible with bounding boxes

### Blur

- Detected faces blurred using Gaussian blur
- Reduces face identifiability
- Applied to preview and recordings

### Pixelate

- Detected faces pixelated (mosaic effect)
- Strong anonymisation
- Applied to preview and recordings

## On-Screen Indicators

### Always visible

- **Faces: N** — Number of detected faces (top-left, green)
- **FPS: X.X** — Current frames per second (top-left, green)

### Conditional

- **REC ●** — Recording in progress (red)
- **Privacy: [mode]** — Active privacy mode (yellow)

## Output Locations

### Captured photos

```sh
captures/capture_YYYYMMDD_HHMMSS.jpg
```

### Recorded videos

```sh
recordings/recording_YYYYMMDD_HHMMSS.avi
```

Both folders are created automatically in the project directory.
