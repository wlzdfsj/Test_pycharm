from PIL import Image
import os
'''获取图片进行裁剪'''
'''
for i in range(1,10):
    img_dir="pictures/new/"+str(i)+".jpg"
    img=Image.open(img_dir)
    pic_cut=img.crop((0,0,200,200))
    new_img="九宫格"+str(i)+".jpg"
    new_img_path=os.path.join("cut_picture",new_img)
    print(new_img_path)
    pic_cut.save(new_img_path)
'''
'''拼接图片'''
# 创建白色背景图
bg_img = Image.new('RGB', (640, 640), (255, 255, 255))
for i in range(3):  #绘制三行三列九宫格
    for j in range(3):
        if(i==1):
            img = Image.open("cut_picture/九宫格" + str(j + 4) + ".jpg") #获取图片
        elif(i==2):
            img = Image.open("cut_picture/九宫格" + str(j + 7) + ".jpg")
        else:
            img=Image.open("cut_picture/九宫格"+str(j+1)+".jpg")
        bg_img.paste(img, (10+j*210, 10+i*210))  #在画布上拼接所有图片

bg_img.save("cut_picture/result.jpg")


