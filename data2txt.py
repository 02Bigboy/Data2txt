# -*- coding: utf-8 -*-
"""
这个程序的目的是，读取指定文件夹的文件，并把对应文件夹的路径，文件名，标签弄在一个
txt文件里面
规范格式：
D://3.研究生工作//上课//深度学习与模式识别//PACS//test//cartoon/dog/pic_357.jpg 0
"""
import os.path as osp
import os
log_path = "./homework/"
if not osp.exists(log_path):
        os.mkdir(log_path)       # 创建一个路径及文件夹
# out_file = open(log_path + 'PACS_test' + '.txt', 'w')  # 创建一个txt文件
data_root = u'D://3.研究生工作//上课//深度学习与模式识别//PACS//test//'    # 数据集路径
data_names = os.listdir(data_root)  # 读取样本，得到域的文件名
for idx, domain in enumerate(data_names):  # enumerate是为了得到索引
        out_file = open(log_path + domain + '.txt', 'w', encoding="utf-8")  # 创建一个txt文件,加上这个encoding就不会出现中文乱码了
        class_data_name = os.listdir(data_root+domain+'/')  # 得到每个域下的标签名字
        class_data_name.sort()
        for idx2, class_name in enumerate(class_data_name):  # 得到标签及其索引
                sample_name = os.listdir(data_root + domain + '/'+class_name+'/')  # 得到每个类下的样本名字
                sample_name.sort()
                for filename in sample_name:
                        out_file.write(data_root+domain+'/'+class_name + '/' + filename + " " + str(idx2) + '\n')
                        out_file.flush()


