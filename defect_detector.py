import cv2
import numpy as np

class DefectDetector:
    
    def to_grayscale(self, img_array: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    def reduce_noise(self, gray: np.ndarray) -> np.ndarray:
        return cv2.GaussianBlur(gray, (5, 5), 0)

    def threshold(self, blurred: np.ndarray) -> np.ndarray:
        _, binary = cv2.threshold(
            blurred, 0, 255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )
        return binary