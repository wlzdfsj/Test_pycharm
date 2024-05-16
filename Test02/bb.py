from PIL import Image
import os

# 读取图片
im = Image.open("pictures/new/1.jpg")

# 获取图片的尺寸
x, y = im.size

# 计算白色背景的尺寸
# 10是两个空隙的长度总和
bg_x = x + 10
bg_y = y + 10

# 创建白色背景图
bg_img = Image.new('RGB', (bg_x, bg_y), (255, 255, 255))

# 计算每次裁剪的长度
interval_x = x // 3
interval_y = y // 3

# 裁剪九张输入的图片
for i in range(3):
    for j in range(3):
     # 从左往右，从上到下进行裁剪
     im_crop = im.crop((j*interval_x, i*interval_y, (j+1)*interval_x, (i+1)*interval_y))
     # 将裁剪的图片粘贴到白色背景图上
     # 5是每个空隙的长度
     bg_img.paste(im_crop, (j*(interval_x+5), i*(interval_y+5)))

# 展示制作好的图片
bg_img.show()

# 保存九宫格图片
dir_path = os.path.dirname("pictures/new/1.jpg")
img_name = '九宫格_'+ os.path.basename("pictures/new/1.jpg")
new_img_path = os.path.join("cut_picture", img_name)
bg_img.save(new_img_path)