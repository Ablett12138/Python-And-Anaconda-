#---------------------  包 ------------------#
import pandas as pd
import xlrd
import numpy as np

# -----------------------------    新建空白Excel文件    -------------------------------#
path = 'create_csv.csv'
data=pd.DataFrame({'id':[1,2,3],'姓名':['我','我','我']})
data.to_csv(path)
print('create_excele.csv成功')

# ------------------------------    新建文件同时写入数据  ----------------------------------#
import pandas as pd
path = 'date_excele.xlsx'
data=pd.DataFrame({'id':[1,2,3],'姓名':['我','我','我']})
# 写入excle
data.to_excel(path)
print('date_excele.xlsx成功')

# ------------------------------    将id设置为索引  ----------------------------------#
路径 = 'set_index.xlsx'
数据=pd.DataFrame({'id':[1,2,3],'姓名':['叶问','李小龙','孙兴华']}) # 写入的数据
数据=数据.set_index('id') # 将id设置为索引
数据.to_excel(路径) # 将数据写入Excel文件
print(数据)

# ------------------------------    读取csv与txt文本文件  ----------------------------------#
path='my_text.txt'
print('# ------------------------------    读取csv与txt文本文件  ----------------------------------#')
#sep=','==设置分隔符为‘,’.
#如果分割符很多的话可以替换‘ ’中的内容
# 空格隔开
data1 = pd.read_csv(path)
# 逗号隔开
data2 = pd.read_table(path,sep=',')
# 默认前五行
print(data1.head(1))
print(data2.head(1))
# 查看数据的形状，返回（行数、列数）
print('*'*30)
print(data1.shape)
# 查看列名列表
print('*'*30)
print(data1.columns)
# 查看索引列
print('*'*30)
print(data1.index)
# 查看每一列数据类型
print('*'*30)
print(data1.dtypes)

print('# ------------------------------    read_csv内置参数及其使用  ----------------------------------#')
# 参数              描述
# sep           分隔符或正则表达式 sep='\s+'
# header        列名的行号，默认0（第一行），如果没有列名应该为None
# names         列名，与header=None一起使用
# index_col     索引的列号或列名，可以是一个单一的名称或数字，也可以是一个分层索引
# skiprows      从文件开始处，需要跳过的行数或行号列表
# encoding      文本编码，例如utf-8
# nrows         从文件开头处读入的行数 nrows=3
# 注意！！！：在有列名的情况下不能使用：header=None   
path='read_txt.txt'
data = pd.read_csv(path,sep=',',header=None,names=['name','age','address','tel','date'],encoding='utf-8',nrows=3)
# 修改索引
data=data.set_index('date')
print(data)
data.to_csv('read_csv.csv')
print('*'*30)
#读取保存的数据
data=pd.read_csv('read_csv.csv',encoding='utf-8',index_col='date')
print(data)
print('*'*30)
data.to_csv('read_csv.csv')
data=pd.read_csv('read_csv.csv',encoding='utf-8',index_col='date')
print(data)