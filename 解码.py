# import cv2
# from PIL import Image
# import numpy as np
# # 读取图像文件
# image = cv2.imread('img/OIP-C 9.jpg')
#
# # 将图像转换为灰度图像
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # 打印图像矩阵的大小
# print("图像矩阵的大小:", gray_image.shape)
#
# # 打印图像矩阵
# print("图像矩阵:\n", gray_image)
#
# pixel_matrix = gray_image
# image = Image.fromarray(pixel_matrix.astype(np.uint8))
# image.save('output_image.jpg')
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 读取输入的图像
# input_image = Image.open("img/OIP-C 9.jpg")  # 请替换为您自己的图像文件路径
#
# # 将图像转换为灰度图像（可选）
# gray_image = input_image.convert("L")
#
# # 将图像转换为像素值矩阵
# pixel_matrix = np.array(gray_image)
#
# # 创建新的图像，将像素值大小显示在图像中
# plt.figure(figsize=(256, 180))  # 设置图像大小
# plt.imshow(pixel_matrix, cmap='gray')  # 使用灰度颜色映射
# for i in range(pixel_matrix.shape[0]):
#     for j in range(pixel_matrix.shape[1]):
#         plt.text(j, i, str(pixel_matrix[i, j]), ha='center', va='center', color='black')
# plt.axis('off')  # 关闭坐标轴显示
# plt.savefig('pixel_values_text_image.png', bbox_inches='tight', pad_inches=0)  # 保存图像到文件
# plt.close()
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 读取图像文件
image = Image.open("img/OIP-C 9.jpg")  # 请替换为您自己的图像文件路径

# 将图像转换为灰度图像（可选）
gray_image = image.convert("L")

# 将图像转换为二维矩阵
pixel_matrix = np.array(gray_image)

# 显示图像
plt.figure(figsize=(250, 180))
plt.imshow(pixel_matrix, cmap='gray')
plt.axis('off')
plt.show()
