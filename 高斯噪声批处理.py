import os

import cv2
import numpy as np


def nosie_image(image):
    image = np.array(image / 255, dtype=float)
    nosie = np.random.normal(0, 0.001 ** 0.01, image.shape)  # 噪声参数
    out = image + nosie
    if out.min() < 0:
        low_clip = -1
    else:
        low_clip = 0
    out = np.clip(out, low_clip, 1.0)
    nosied = np.uint8(out * 255)
    return nosied

# 获得文件夹下所有文件
filePath = 'E:/yolox/img/'
filenames = os.listdir(filePath)
# # 指定保存的文件夹
outputPath = 'E:/yolox/img_out/'
cnt = 1
for filename in filenames:
    # 读取图像
    print(filenames + filename)
    img = cv2.imread(filenames + filename)
    # img = cv2.imread('insects/train/cutworm/cutworm-1.jpg')
    img1 = nosie_image(img)
    # 保存图像
    cv2.imwrite(outputPath + filename, img1)
    # print(outputPath+filename)