import os
from PIL import Image
from yolo import YOLO
if __name__ == "__main__":
    yolo = YOLO()
    path = "img/p1.JPG"  # 输入图片的路径
    img = path
    portion = os.path.split(img)  # 读取图片的文件名称
    img_save_path = "img/res"+portion[1]  # 输出图片的路径和名称
    try:
        image = Image.open(img) # 打开图片
    except:
        print('Open Error! Try again!')

    else:
        r_image = yolo.detect_image(image)  # 处理图片
        r_image.save(img_save_path)  # 储存图片
