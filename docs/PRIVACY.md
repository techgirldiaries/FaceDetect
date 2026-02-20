# Privacy and Consent

## Camera Consent

### First-run consent

On first launch, FaceDetect requests camera access consent via terminal prompt:

```
--------------------------------------------------------------
FaceDetect - Camera Access Consent
--------------------------------------------------------------
This application requires access to your camera to detect faces.
All processing is done locally on your device.
No data is transmitted or stored externally.
--------------------------------------------------------------

Do you consent to camera access? (yes/no):
```

### Consent storage

Your consent choice is stored in:

```
%APPDATA%\FaceDetect\settings.json  (Windows)
~/FaceDetect/settings.json          (macOS/Linux)
```

### Revoking consent

Delete the settings file to trigger consent prompt again on next launch.

## Privacy Modes

### Local processing only

- All face detection runs locally on your device
- No network requests or cloud processing
- No data transmission to external servers

### Privacy filtering

Use the `p` key to toggle privacy modes during runtime:

1. **None** — Standard face detection with bounding boxes
2. **Blur** — Gaussian blur applied to detected face regions
3. **Pixelate** — Pixelation mosaic applied to detected face regions

### Recording with privacy

When privacy mode is active:

- Captured photos include the privacy filter
- Recorded videos include the privacy filter on all frames
- Original unfiltered frames are never saved

## Data Storage

### What is stored

- Consent status (boolean flag in settings.json)
- User settings (camera index, model preferences)
- Captured photos (only when you press `c`)
- Recorded videos (only when you press `r`)

### What is NOT stored

- Continuous video feed
- Face embeddings or biometric data
- Personal identifiable information
- Usage analytics or telemetry

## Compliance Notes

- **GDPR**: Local processing, explicit consent, user control over data
- **COPPA**: No data collection from users
- **CCPA**: No sale or sharing of personal information

For privacy policy questions, see LICENSE.md for usage terms.
