import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Annotator:

    def draw_boxes(self, img_array: np.ndarray, boxes: list, severity: str) -> np.ndarray:
        annotated = img_array.copy()

        for i, (x, y, w, h) in enumerate(boxes):
            cv2.rectangle(annotated, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(
                annotated, f"D{i+1}", (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1
            )

        cv2.putText(
            annotated, severity, (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2 
        )
        return annotated

    def save_annotated(self, img_array: np.ndarray, output_path: str):
        img = Image.fromarray(img_array)
        img.save(output_path)
        print(f"Annotated image saved: {output_path}")