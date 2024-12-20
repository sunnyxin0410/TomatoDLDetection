from PIL import Image, ImageDraw
import numpy as np
import random

def apply_cutout(image, num_patches=1, patch_size=50):
    img = np.array(image)
    h, w = img.shape[:2]
    for _ in range(num_patches):
        cx, cy = random.randint(0, w), random.randint(0, h)
        x1 = max(cx - patch_size // 2, 0)
        y1 = max(cy - patch_size // 2, 0)
        x2 = min(cx + patch_size // 2, w)
        y2 = min(cy + patch_size // 2, h)
        img[y1:y2, x1:x2] = 0
    return Image.fromarray(img)
def apply_cutout_to_local_image(image_path, save_path, num_patches=1, patch_size=50):
    image = Image.open(image_path).convert("RGB")
    augmented_image = apply_cutout(image, num_patches, patch_size)
    augmented_image.save(save_path)
if __name__ == "__main__":
    image_path = "img/2.jpg"  # 读取图像路径
    save_path = "img_out/2.jpg"   # 保存图像路径
    apply_cutout_to_local_image(image_path, save_path, num_patches=1, patch_size=200)
