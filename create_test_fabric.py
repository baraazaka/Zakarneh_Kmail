import numpy as np
from PIL import Image, ImageDraw
import random

def create_fabric_image(output_path="fabric_sample.png", num_defects=4):
    # الخطوة 1: إنشاء خلفية رمادية موحدة (تحاكي قماش نظيف)
    width, height = 400, 400
    noise = np.random.randint(200, 230, (height, width, 3), dtype=np.uint8)
    img = Image.fromarray(noise)
    draw = ImageDraw.Draw(img)

    # الخطوة 2: إضافة بقع داكنة عشوائية لتمثيل العيوب
    for _ in range(num_defects):
        x = random.randint(20, width - 60)
        y = random.randint(20, height - 60)
        w = random.randint(10, 50)
        h = random.randint(10, 40)
        color = random.randint(30, 100)   # لون داكن = عيب
        draw.ellipse([x, y, x + w, y + h], fill=(color, color, color))

    img.save(output_path)
    print(f"Test fabric image saved: {output_path}  ({num_defects} defects)")

if __name__ == "__main__":
    create_fabric_image("fabric_sample.png", num_defects=4)
    create_fabric_image("fabric_clean.png",  num_defects=0)
    create_fabric_image("fabric_heavy.png",  num_defects=8)