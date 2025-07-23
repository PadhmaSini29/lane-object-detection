import torch
import cv2

class ObjectDetector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.model.conf = 0.4  # confidence threshold

    def detect(self, img):
        # Convert BGR to RGB
        results = self.model(img[..., ::-1])
        return results

    def draw_boxes(self, img, results):
        for *box, conf, cls in results.xyxy[0]:
            x1, y1, x2, y2 = map(int, box)
            label = f'{self.model.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.putText(img, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        return img
