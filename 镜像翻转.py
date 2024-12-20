from PIL import Image
import os

# 获得文件夹下所有文件
filePath = 'yolov5/img/'
filenames = os.listdir(filePath)

# 指定保存的文件夹
outputPath = 'yoloxv5/img/'

# 迭代所有图片
for filename in filenames:
    im = Image.open(filePath + filename)
    im_rotate = im.transpose(Image.FLIP_LEFT_RIGHT)
    im_rotate.save(outputPath + filename)
