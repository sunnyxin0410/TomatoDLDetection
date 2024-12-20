# 图像灰度化批量

from PIL import Image
import os
input_dir = 'img/'
# 输入文件夹
out_dir = 'img/'
# 输出文件夹注意？转义字符使用///在不在其中
a = os.listdir(input_dir)
for i in a:
    print(i)
    I = Image.open(input_dir + i)
    L = I.convert('L')
    L.save(out_dir + i)  # 自动重命名/替换
