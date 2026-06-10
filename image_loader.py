import os
import numpy as np
from PIL import Image

class ImageLoader:
    
    def load_image(self, path: str) -> Image.Image:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: The image file at '{path}' was not found.")
        
        img = Image.open(path)
        return img.convert("RGB")

    def resize_image(self, image, max_size: int = 512):
        img_copy = image.copy()
        img_copy.thumbnail((max_size, max_size), Image.LANCZOS)
        return img_copy

    def to_numpy(self, image: Image.Image) -> np.ndarray:
        return np.array(image)