import os
import shutil
#批量修改文件夹中图片名称
class Picture_Rename():
    def __init__(self):
        self.path = 'pictures/original'  #表示需要命名处理的文件夹
        self.save_path='pictures/new'#保存重命名后的图片地址
    def rename(self):
        filelist = os.listdir(self.path) #获取文件夹下面所有文档路径
        total_num = len(filelist) #获取文件长度（个数）
        i = 1  #表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.jpg') or item.endswith('.jpeg') or item.endswith('.png'):  #统一修改后缀
                original_dir = os.path.join(os.path.abspath(self.path), item)#当前文件中图片的原始地址original_dir = {str} 'D:\\Pycharm\\Pycharm_space\\Test02\\pictures\\original\\06e1941b017644f410177770a7e34dbf.png'
                new_dir = os.path.join(os.path.abspath(self.save_path), ''+str(i) + '.jpg')#把图片重命名并放入新的文件夹下面
                try:
                    shutil.copy(original_dir, new_dir)  #将图片复制到新的文件夹下面
                    print ('converting %s to %s ...' % (original_dir, new_dir))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i-1))

if __name__ == '__main__':
    demo = Picture_Rename()
    demo.rename()

