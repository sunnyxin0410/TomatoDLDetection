import os

import cv2
import numpy as np


def nosie_image(image):
    image = np.array(image / 255, dtype=float)
    nosie = np.random.normal(0, 0.001 ** 0.5, image.shape)  # 噪声参数
    out = image + nosie
    if out.min() < 0:
        low_clip = -1
    else:
        low_clip = 0
    out = np.clip(out, low_clip, 1.0)
    nosied = np.uint8(out * 255)
    return nosied


# 获得文件夹下所有文件
# filePath = 'E:/yolox/img/'
# filenames = os.listdir(filePath)
# image_path = "img/3.jpg"
# imagenames = os.path.basename(image_path)
# # 指定保存的文件夹
# outputPath = 'E:/yolox/img_out/'
#
# cnt = 1
# for filename in imagenames:
#     # 读取图像
#     print(image_path + filename)
#     img = cv2.imread(image_path + filename)
#     # img = cv2.imread('insects/train/cutworm/cutworm-1.jpg')
#     img1 = nosie_image(img)
#     # 保存图像
#     cv2.imwrite(outputPath + filename, img1)
#     # print(outputPath+filename)
image_path = "img/3.jpg"

# 检查指定路径是否为文件
if os.path.isfile(image_path):
    # 获取图像文件名
    filename = os.path.basename(image_path)

    # 指定保存的文件夹
    outputPath = 'E:/yolox/img_out/'

    # 读取图像
    img = cv2.imread(image_path)
    # img = cv2.imread('insects/train/cutworm/cutworm-1.jpg')
    img1 = nosie_image(img)  # 假设 nosie_image 函数已定义

    # 保存图像
    cv2.imwrite(outputPath + filename, img1)
    print("Processed image saved to:", outputPath + filename)
else:
    print("Error: The specified path is not a file.")