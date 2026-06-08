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
        
        
    def show_comparison(self, original: np.ndarray, annotated: np.ndarray, severity: str):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        ax1.imshow(original)
        ax1.set_title("Original Fabric")
        ax1.axis("off")

        ax2.imshow(annotated)
        ax2.set_title("Defect Analysis")
        ax2.axis("off")

        plt.suptitle(f"FabricCheck — {severity}")
        plt.tight_layout()
        plt.show()    