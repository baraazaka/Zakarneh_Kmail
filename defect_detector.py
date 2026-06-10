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
    def classify_severity(self, defects: list, image_area: int) -> str:
        total_defect_area = sum(cv2.contourArea(c) for c in defects)
        defect_ratio = (total_defect_area / image_area) * 100
        num_defects = len(defects)

        if num_defects == 0:
            return "Good — No defects detected"
        elif num_defects <= 2 and defect_ratio < 2.0:
            return "Low — Minor defects"
        elif num_defects <= 5 or defect_ratio <= 5.0:
            return "Medium — Moderate defects"
        else:
            return "High — Severe defects"

    def get_bounding_boxes(self, contours: list) -> list:
        return [cv2.boundingRect(c) for c in contours]