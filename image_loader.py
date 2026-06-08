import os
import numpy as np
from PIL import Image

class ImageLoader:
    
    def load_image(self, path: str) -> Image.Image:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: The image file at '{path}' was not found.")
        
        img = Image.open(path)
        return img.convert("RGB")