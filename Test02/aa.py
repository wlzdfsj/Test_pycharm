from PIL import Image, ImageDraw

# 创建一个画布，用来存放排列后的图片
canvas = Image.new('RGB', (1000, 600), 'white')
# 读取图片
im1 = Image.open('pictures/new/1.jpg')
im2 = Image.open('pictures/new/2.jpg')
im3 = Image.open('pictures/new/3.jpg')
im4 = Image.open('pictures/new/4.jpg')
img1_cut=im1.crop((0,0,150,150))
img2_cut=im2.crop((0,0,150,150))
img3_cut=im3.crop((0,0,150,150))
img4_cut=im4.crop((0,0,150,150))


# 将图片粘贴到画布上，实现排列
canvas.paste(img1_cut, (0, 0))
canvas.paste(img2_cut, (200, 0))
canvas.paste(img3_cut, (400, 0))
canvas.paste(img4_cut, (600, 0))

# 保存结果图片
canvas.save('result.jpg')