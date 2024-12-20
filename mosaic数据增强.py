import cv2
import numpy as np


def mosaic(image):
    # 获取图像尺寸
    height, width = image.shape[:2]
    # 将图像分割成四个区域
    half_height = height // 2
    half_width = width // 2
    # 计算每个区域的平均颜色
    topLeft = np.mean(image[:half_height, :half_width], axis=(0, 1)).astype(np.uint8)
    topRight = np.mean(image[:half_height, half_width:], axis=(0, 1)).astype(np.uint8)
    bottomLeft = np.mean(image[half_height:, :half_width], axis=(0, 1)).astype(np.uint8)
    bottomRight = np.mean(image[half_height:, half_width:], axis=(0, 1)).astype(np.uint8)
    # 将每个区域的像素值设置为平均颜色
    image[:half_height, :half_width] = topLeft
    image[:half_height, half_width:] = topRight
    image[half_height:, :half_width] = bottomLeft
    image[half_height:, half_width:] = bottomRight
    return image


# 读取图像
input_image = cv2.imread('input_image.jpg')

# 调用mosaic函数进行数据增强预处理
output_image = mosaic(input_image)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', input_image)
cv2.imshow('Mosaic Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
