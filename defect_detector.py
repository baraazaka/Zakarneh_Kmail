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
    def find_contours(self, binary: np.ndarray) -> list:
        contours, _ = cv2.findContours(
            binary,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )
        return list(contours)

    def filter_contours(self, contours: list, min_area: int = 50) -> list:
        return [c for c in contours if cv2.contourArea(c) >= min_area]