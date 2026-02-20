import cv2
import numpy as np

def blur_faces(frame, faces, blur_strength=51):
    """
    Applies Gaussian blur to detected face regions.
    
    Args:
        frame: The input image frame
        faces: List of face bounding boxes (x, y, w, h)
        blur_strength: Kernel size for Gaussian blur (must be odd)
    
    Returns:
        Frame with blurred faces
    """
    if blur_strength % 2 == 0:
        blur_strength += 1
    
    for (x, y, w, h) in faces:
        # Extract face region
        face_region = frame[y:y+h, x:x+w]
        
        # Apply Gaussian blur
        if face_region.size > 0:
            blurred = cv2.GaussianBlur(face_region, (blur_strength, blur_strength), 0)
            frame[y:y+h, x:x+w] = blurred
    
    return frame

def pixelate_faces(frame, faces, pixel_size=10):
    """
    Applies pixelation effect to detected face regions.
    
    Args:
        frame: The input image frame
        faces: List of face bounding boxes (x, y, w, h)
        pixel_size: Size of pixelation blocks
    
    Returns:
        Frame with pixelated faces
    """
    for (x, y, w, h) in faces:
        # Extract face region
        face_region = frame[y:y+h, x:x+w]
        
        if face_region.size > 0 and w > 0 and h > 0:
            # Resize down and then up to create pixelation
            small_width = max(1, w // pixel_size)
            small_height = max(1, h // pixel_size)
            
            small = cv2.resize(face_region, (small_width, small_height), interpolation=cv2.INTER_LINEAR)
            pixelated = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
            
            frame[y:y+h, x:x+w] = pixelated
    
    return frame

def apply_privacy_mode(frame, faces, mode="blur"):
    """
    Applies privacy filter to faces based on selected mode.
    
    Args:
        frame: The input image frame
        faces: List of face bounding boxes (x, y, w, h)
        mode: Privacy mode - "blur", "pixelate", or "none"
    
    Returns:
        Frame with privacy filter applied
    """
    if mode == "blur":
        return blur_faces(frame, faces)
    elif mode == "pixelate":
        return pixelate_faces(frame, faces)
    else:
        return frame
