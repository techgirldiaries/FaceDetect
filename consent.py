import json
import os
from pathlib import Path

def get_config_path():
    """Returns the path to the settings configuration file."""
    appdata = os.getenv("APPDATA")
    if not appdata:
        appdata = os.path.expanduser("~")
    
    config_dir = Path(appdata) / "FaceDetect"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "settings.json"

def load_settings():
    """Loads settings from the config file."""
    config_path = get_config_path()
    if not config_path.exists():
        return {}
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_settings(settings):
    """Saves settings to the config file."""
    config_path = get_config_path()
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
    except IOError as e:
        print(f"Warning: Failed to save settings: {e}")

def check_consent():
    """
    Checks if the user has given consent to use the camera.
    Returns True if consent has been granted, False otherwise.
    """
    settings = load_settings()
    return settings.get("camera_consent_granted", False)

def request_consent():
    """
    Requests camera consent from the user via terminal.
    Returns True if granted, False otherwise.
    """
    print("\n" + "=" * 60)
    print("FaceDetect - Camera Access Consent")
    print("=" * 60)
    print("This application requires access to your camera to detect faces.")
    print("All processing is done locally on your device.")
    print("No data is transmitted or stored externally.")
    print("=" * 60)
    
    while True:
        response = input("\nDo you consent to camera access? (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            settings = load_settings()
            settings["camera_consent_granted"] = True
            save_settings(settings)
            print("Consent granted. Starting application...\n")
            return True
        elif response in ["no", "n"]:
            print("Consent denied. Application will exit.\n")
            return False
        else:
            print("Please answer 'yes' or 'no'.")

def revoke_consent():
    """Revokes camera consent."""
    settings = load_settings()
    settings["camera_consent_granted"] = False
    save_settings(settings)

def ensure_consent():
    """
    Ensures consent has been granted before proceeding.
    If not, requests it. Returns True if granted, False otherwise.
    """
    if check_consent():
        return True
    return request_consent()
