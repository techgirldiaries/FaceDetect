import cv2
from detect import FaceDetector

class DnnFaceDetector(FaceDetector):
    def __init__(self, model_path, config_path, confidence_threshold):
        self.net = cv2.dnn.readNet(model_path, config_path)
        self.confidence_threshold = confidence_threshold

    def detect(self, image):
        height, width = image.shape[:2]
        blob = cv2.dnn.blobFromImage(
            image,
            scalefactor=1.0,
            size=(300, 300),
            mean=(104.0, 177.0, 123.0),
            swapRB=False,
            crop=False,
        )
        self.net.setInput(blob)
        detections = self.net.forward()

        faces = []
        for index in range(detections.shape[2]):
            confidence = float(detections[0, 0, index, 2])
            if confidence < self.confidence_threshold:
                continue

            x1 = int(detections[0, 0, index, 3] * width)
            y1 = int(detections[0, 0, index, 4] * height)
            x2 = int(detections[0, 0, index, 5] * width)
            y2 = int(detections[0, 0, index, 6] * height)

            x1 = max(0, min(x1, width - 1))
            y1 = max(0, min(y1, height - 1))
            x2 = max(0, min(x2, width - 1))
            y2 = max(0, min(y2, height - 1))

            box_width = max(0, x2 - x1)
            box_height = max(0, y2 - y1)
            if box_width > 0 and box_height > 0:
                faces.append((x1, y1, box_width, box_height))

        return faces

def create_dnn_detector(
    model_name,
    dnn_model_path,
    dnn_config_path,
    dnn_confidence,
):
    if model_name != "dnn":
        return None

    if not dnn_model_path or not dnn_config_path:
        raise RuntimeError(
            "For --model dnn, set both --dnn-model-path and --dnn-config-path"
        )

    return DnnFaceDetector(
        dnn_model_path,
        dnn_config_path,
        dnn_confidence,
    )
