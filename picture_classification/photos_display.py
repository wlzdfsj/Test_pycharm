import os
import pandas as pd
from PIL import ImageDraw,ImageFont
from PIL import Image
import math

src_path='D:\证件照\照片墙排版\class_names'
#['18级网络工程', '18级计算机科学与技术']
class_names=os.listdir(src_path)

#存放图片字典{'18级网络工程':[‘202211.jpg’，‘202212.jpeg’，...],'18级计算机科学与技术':[‘202211.jpg’，‘202212.jpeg’，...]}
image_file={}
for file in class_names:
    image_file[file]=os.listdir(os.path.join(src_path, file))

#读取excel文件信息
df=pd.read_excel('D:\证件照\照片墙排版\students_info.xlsx')
#获取学号为202244的学生姓名
#print(df[df['学号']==202244]['姓名'])

for class_name in class_names:
    #1.创建空白画布
    new_image = Image.new('RGB', (860, 560), (255, 255, 255))
    #2.创建可以在图片上（画布）添加文字的对象
    drawer = ImageDraw.Draw(new_image)
    #定义字体
    font_classname = ImageFont.truetype('simsun.ttc', 20, encoding='utf-8')
    font_studentsname = ImageFont.truetype('simsun.ttc', 15, encoding='utf-8')
    #3.获取所有图片
    iamges_list=image_file[class_name]
    images_num=len(iamges_list)
    #每行排版6张图片 row*col
    col=6
    row=math.ceil(images_num/col)
    #4.向画布中添加文字
    drawer.text((20,10),class_name,fill='black',font=font_classname)
    #5.计算图片张贴起始位置
    start_left=20
    start_up=50
    num=0
    for image in iamges_list:
        image_path=os.path.join(src_path,class_name,image)
        img=Image.open(image_path)
        img=img.resize((120,150))
        #6.计算每张图片张贴的起始位置
        position=(start_left+num%6*140,start_up+math.floor(num/6)*170)
        #7.画布上张贴图片
        new_image.paste(img,position)
        #8.写入图片对应的学生姓名
        stu_id=image.split('.')[0]
        stu_id=int(stu_id)
        stu_name=df[df['学号'] == stu_id]['姓名']
        stu_name=stu_name.item()
        #计算学生姓名写入的起始位置
        name_pos=(start_left+num%6*140+40,start_up+math.floor(num/6)*170+150)
        drawer.text(name_pos, stu_name, fill='black', font=font_studentsname)

        if num<images_num:
            num+=1
        else:
            break

    #9.每个班级绘制一张画布
    new_image.save(class_name+'.jpg')