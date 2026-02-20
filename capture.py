import cv2
from datetime import datetime
from pathlib import Path

class CaptureManager:
    def __init__(self, base_dir="d:\\Repos\\GitHub\\FaceDetect"):
        """Initialises capture manager with output directories."""
        self.base_dir = Path(base_dir)
        self.captures_dir = self.base_dir / "captures"
        self.recordings_dir = self.base_dir / "recordings"
        
        # Create directories if they don't exist
        self.captures_dir.mkdir(parents=True, exist_ok=True)
        self.recordings_dir.mkdir(parents=True, exist_ok=True)
        
        self.video_writer = None
        self.is_recording = False
        self.current_recording_path = None
    
    def capture_photo(self, frame):
        """
        Saves a snapshot of the current frame.
        
        Args:
            frame: The frame to save
        
        Returns:
            Path to saved image or None if failed
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"capture_{timestamp}.jpg"
        filepath = self.captures_dir / filename
        
        try:
            cv2.imwrite(str(filepath), frame)
            print(f"Snapshot saved: {filepath}")
            return filepath
        except Exception as e:
            print(f"Failed to save snapshot: {e}")
            return None
    
    def start_recording(self, frame_width, frame_height, fps=20.0):
        """
        Starts video recording.
        
        Args:
            frame_width: Width of frames to record
            frame_height: Height of frames to record
            fps: Frames per second for recording
        
        Returns:
            True if recording started successfully, False otherwise
        """
        if self.is_recording:
            print("Recording already in progress")
            return False
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording_{timestamp}.avi"
        self.current_recording_path = self.recordings_dir / filename
        
        # Define codec and create VideoWriter
        fourcc_fn = getattr(cv2, "VideoWriter_fourcc", None)
        if fourcc_fn is None:
            print("VideoWriter_fourcc not available in this OpenCV build")
            return False
        
        fourcc = fourcc_fn(*'XVID')
        self.video_writer = cv2.VideoWriter(
            str(self.current_recording_path),
            fourcc,
            fps,
            (frame_width, frame_height)
        )
        
        if self.video_writer.isOpened():
            self.is_recording = True
            print(f"Recording started: {self.current_recording_path}")
            return True
        else:
            print("Failed to start recording")
            self.video_writer = None
            return False
    
    def write_frame(self, frame):
        """
        Writes a frame to the current recording.
        
        Args:
            frame: The frame to write
        
        Returns:
            True if successful, False otherwise
        """
        if not self.is_recording or self.video_writer is None:
            return False
        
        try:
            self.video_writer.write(frame)
            return True
        except Exception as e:
            print(f"Error writing frame: {e}")
            return False
    
    def stop_recording(self):
        """
        Stops the current recording.
        
        Returns:
            Path to saved video or None if not recording
        """
        if not self.is_recording:
            return None
        
        if self.video_writer is not None:
            self.video_writer.release()
            self.video_writer = None
        
        saved_path = self.current_recording_path
        self.current_recording_path = None
        self.is_recording = False
        
        print(f"Recording stopped: {saved_path}")
        return saved_path
    
    def cleanup(self):
        """Ensures all resources are released."""
        if self.is_recording:
            self.stop_recording()
