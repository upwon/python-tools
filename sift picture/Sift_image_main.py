
import os
import fnmatch
import shutil
import pandas as pd
import numpy as np

# 核心代码，设置显示的最大列、宽等参数，消掉打印不完全中间的省略号(打印Excel表时使用)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

import sys

sys.setrecursionlimit(1000000)  # 例如这里设置为一百万

#源路径 与目的路径设置  用于
path=r'E:\Program_Project\Pycharm\excel\image\ACAI900S'  # 改在你想遍历的地方
path_dest="D:\\PingFangkeji\\SCT2\\201807\\temp\\bad_image"     #存放坏箱的文件夹
path_dest_goodbox="D:\\PingFangkeji\\SCT2\\201807\\temp\\good_image"  #存放正常箱子的

def CreatBadimage_Txt(badbox_name,excelname):
    txtdir=os.path.abspath(os.path.dirname(excelname))          #获得该Excel表格当前的目录
    file_write_obj = open(txtdir+"\\"+"Bad_Box.txt", 'w')       #创建 txt
    for var in badbox_name:
        file_write_obj.writelines(var)                          #写入内容
        file_write_obj.write('\n')
    file_write_obj.close()                                      #关闭
    print("成功保存Bad_Box.txt至"+txtdir+"\n")

def CreatGoodimage_Txt(goodbox_name,excelname):
    txtdir = os.path.abspath(os.path.dirname(excelname))
    file_write_obj = open(txtdir+"\\"+'./Good_Box.txt', 'w')
    goodbox_name=goodbox_name.replace("未识别")      #删除文件名为未识别的字符串
  #  goodbox_name = goodbox_name.sub("未识别")
    for var in goodbox_name:
        file_write_obj.writelines(var)
        file_write_obj.write('\n')
    file_write_obj.close()
    print("成功保存Good_Box.txt至本目录下\n")

def copy2(source_folder="",dest_folder=""):
    file_list = os.listdir(source_folder)           #列出文件夹下的
    for file_obj in file_list:
        file_path = os.path.join(source_folder, file_obj)

        file_name, file_extend = os.path.splitext(file_obj)
      #  new_name = file_name + '_bad' + file_extend      # 在文件名的最后加上’_bad'

      #  newfile_path = os.path.join(source_folder, new_name)
        if os.path.isdir(path_dest):                    # path参数存在且是一个文件夹
            print("存在文件夹")
        elif not os.path.exists(path_dest):
            os.makedirs(path_dest)
            print("不存在文件夹，已创建")
        shutil.copy(file_path, dest_folder)
    print("复制完毕")

def copy1(source_folder="",dest_folder=""):
    file_list = os.listdir(source_folder)           #列出文件夹下的
    for file_obj in file_list:
        file_path = os.path.join(source_folder, file_obj)

        file_name, file_extend = os.path.splitext(file_obj)
       # new_name = file_name + '_bad' + file_extend      # 在文件名的最后加上’_bad'

      #  newfile_path = os.path.join(source_folder, new_name)
        if os.path.isdir(path_dest_goodbox):                    # path参数存在且是一个文件夹
            print("存在文件夹")
        elif not os.path.exists(path_dest_goodbox):
            os.makedirs(path_dest_goodbox)
            print("不存在文件夹，已创建")
        shutil.copy(file_path, dest_folder)
    print("复制完毕")


def copybadinmae(path,badbox_name,):
    num = 0
    #path_image = "E:\\Program_Project\\Pycharm\\excel\\image\\ACAI900S\\图片"
    path_image=path
    list_bad_dir = []
    for parent, dirnames, filenames in os.walk(path_image):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in dirnames:  # 输出文件夹信息
            print("parent is:" + parent)
            print("dirname is\t" + dirname)

            print(parent + "\\" + dirname)  # 打印全部目录
            current_filename = parent + "\\" + dirname
            #  filename=[]

            #  filename.append(dirname)
            #  print("文件名为：",filename)
            print("dirname文件名为", dirname)
            for i in badbox_name:                   #坏箱的 文件夹的名字
                print("坏箱文件夹名字为：" + i)
                print("dirname is", dirname)
                if i == dirname:                    #如果和当前目录dirname文件夹的名字相同
                    print("发现相等")
                    print("bad_box打印为：\n")
                    print(parent + "\\" + dirname)
                    tempdir = parent + "\\" + dirname     #获得这个文件夹的完整路径
                    list_bad_dir.append(tempdir)                   #存放坏箱路径 过一会用于复制

                    num = num + 1                          #计数 存放坏箱文件夹的个数
    print(num)
    for dir in list_bad_dir:           #将文件夹下的图片用for遍历  然后打印出来
        copy2(dir, path_dest)
        print(dir)


def copygoodinmae(path,goodbox_name,):
    num = 0
    #path_image = "E:\\Program_Project\\Pycharm\\excel\\image\\ACAI900S\\图片"
    path_image=path
    list_good_dir = []
    for parent, dirnames, filenames in os.walk(path_image):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in dirnames:  # 输出文件夹信息
            print("parent is:" + parent)
            print("dirname is\t" + dirname)

            print(parent + "\\" + dirname)  # 打印全部目录
            current_filename = parent + "\\" + dirname
            #  filename=[]

            #  filename.append(dirname)
            #  print("文件名为：",filename)
            print("dirname文件名为", dirname)
            for i in goodbox_name:                   #坏箱的 文件夹的名字
                print("坏箱文件夹名字为：" + i)
                print("dirname is", dirname)
                if i == dirname:                    #如果和当前目录dirname文件夹的名字相同
                    print("发现相等")
                    print("good_box打印为：\n")
                    print(parent + "\\" + dirname)
                    tempdir = parent + "\\" + dirname     #获得这个文件夹的完整路径
                    list_good_dir.append(tempdir)                   #存放正常箱子路径 过一会用于复制

                    num = num + 1                          #计数 存放坏箱文件夹的个数
    print("存放正常箱子的文件夹共有:%d",num)
    for dir in list_good_dir:           #将文件夹下的图片用for遍历  然后打印出来
        copy1(dir, path_dest_goodbox)
        print(dir)

def main():
    print("注意：改程序会将图片筛选并复制到D盘的D:\\PingFangkeji\\SCT2\\201807\\temp\\bad_image，"
          "和D盘下的D:\\PingFangkeji\\SCT2\\201807\\temp\\good_image 请先创建好文件夹")
    excelname=input(r"请输入Excel文件路径及名称：")
    if excelname=="":
        print("程序退出，您未输入Excel表格路径及名称\n示例输入：D:\\abc.xlsx\n")
        exit()
    df = pd.read_excel(excelname)               #读取Excel表格
    print(df.dtypes)
    df1=df[(df["烂柜"]=='Y')|(df["危柜"]=='Y')]              #筛选Excel表中的烂柜和危柜
    print(df1)
    print("\n\n\n*************************\n\n")
    badbox_name=df1["箱号"]                    #df1.loc[df1["箱号"]]    获取箱号这一列  得到文件夹的名字
    print(badbox_name,excelname)

    df_good=df[(df["烂柜"]=='N')|(df["危柜"]=='N')]         #筛选出好的
    goodbox_name=df_good["箱号"]                           #  获取箱号这一列  得到文件夹的名字



    print("开始遍历")
    for x in badbox_name:
        print("打印badbox_name")
        print(x)
    CreatBadimage_Txt(badbox_name,excelname)          #创建TXT文件 存放烂柜危柜的文件夹的名称
    CreatGoodimage_Txt(goodbox_name,excelname)        #创建TXT文件 存放好的集装箱的文件夹的名称

    path_image=os.path.abspath(os.path.dirname(excelname))+"\\"+"图片"     #Excel同级目录的 /图片 目录
    print("path_image:"+path_image)
    copybadinmae(path=path_image,badbox_name=badbox_name)                 #复制坏箱到目的文件夹
    copygoodinmae(path=path_image,goodbox_name=goodbox_name)              #复制好的箱子到目的文件夹

    path_image_bad = path_dest + "\\" + "XML_of_bad_image"
    os.makedirs(path_image_bad)         #创建一个文件夹 放xml文件

    path_image_good = path_dest_goodbox + "\\" + "XML_of_good_image"
    os.makedirs(path_image_good)                                     #创建一个文件夹 放xml文件

    print("\n\n操作完毕")
    os.system("pause")
    print("\n\n请关闭窗口")




# file_write_obj = open('./Bad_Box.txt', 'w')
# for var in badbox_name:
#     file_write_obj.writelines(var)
#     file_write_obj.write('\n')
# file_write_obj.close()
# print("成功保存残损集装箱的文件名至本目录下的Bad_Box.txt\n")


if __name__ =='__main__':
    main()