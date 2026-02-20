import cv2

class FaceDetector:
    def detect(self, image):
        raise NotImplementedError()

class HaarCascadeFaceDetector(FaceDetector):
    def __init__(self, cascade_path, scale_factor, min_neighbors, min_size):
        self.classifier = cv2.CascadeClassifier(cascade_path)
        if self.classifier.empty():
            raise RuntimeError(
                f"Failed to load cascade classifier from: {cascade_path}"
            )

        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.min_size = min_size

    def detect(self, image):
        greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.classifier.detectMultiScale(
            greyscale,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_size,
        )
        return faces

def create_detector(model_name, scale_factor, min_neighbors, min_size):
    if model_name == "haar":
        cv2_data = getattr(cv2, "data", None)
        if cv2_data is None or not hasattr(cv2_data, "haarcascades"):
            raise RuntimeError(
                "OpenCV haarcascade data path is unavailable in this build"
            )
        cascade_path = (
            cv2_data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        return HaarCascadeFaceDetector(
            cascade_path,
            scale_factor,
            min_neighbors,
            min_size,
        )

    if model_name == "dnn":
        raise RuntimeError("DNN detector requires model and config paths")

    raise ValueError(f"Unsupported model: {model_name}")

def draw_detections(image, faces, box_colour, box_thickness):
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            box_colour,
            box_thickness,
        )
    return image
