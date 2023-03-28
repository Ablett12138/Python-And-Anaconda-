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

print('# ------------------------------    read_excel内置参数及其使用  ----------------------------------#')
data=pd.DataFrame({'id':[1,2,3,4,5,6],'姓名':['付紫平','付紫平','付紫平','fzp','fzp','fzp']})
data.to_excel('read_excel内置参数及其使用.xlsx')
data = pd.read_excel('read_excel内置参数及其使用.xlsx',header=0,index_col='id')
print(data)
data.columns=['id','姓名'] # 给每个列重复设置表头
data=data.set_index('id') # 只在index上面改,不要生成新的
print(data.columns) # 查看列名列表， index和columns是分开的
print(data)
data.to_excel('date_excele.xlsx') # 写入到Excel文件
# 注意：必需先装xlrd模块，否则报错mportError: Missing optional dependency 'xlrd'
# 二、查看前几行数据
print(data.head()) # 默认是5行，指定行数写小括号里
# 三、查看数据的形状，返回（行数、列数）
print(data.shape)
# 四、 查看列名列表
print(data.columns)
# 五、查看索引列
print(data.index)
# 六、查看每一列数据类型
print(data.dtypes)

print('# ------------------------------    一维数组Series  ----------------------------------#')
# Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。
# 3.1.1 仅有数据列表即可产生最简单的Series
数据= pd.Series([520,'付紫平',1314,'2023-03-28']) # 左侧是索引，右侧是数据
print(数据)
print(数据.index) # 获取索引，返回索引的（起始值，结束值，步长）
print(数据.values) # 获取数据，返回值序列，打印元素值的列表

# 3.1.3 使用Python字典创建Series
字典={'姓名':'付紫平','性别':'男','年龄':'23','地址':'中国计量大学'}
数据=pd.Series(字典)
print(数据)
print(数据.index) # 返回key

# 3.1.4 根据标签索引查询数据
print(数据) # 查询整个字典
print(数据['姓名']) # 通过key可以查对应的值
type(数据['年龄']) # 通过key可以查对应值的类型
print(数据[['姓名','年龄']]) # 通过多个key查对应的值
type(数据[['姓名','年龄']]) # 注意：他不返回值的类型，而返回Series

# 3.1.5 键和值存在两个列表中，创建Series
# Series只是一个序列，可能是一行，也可能是一列，现在无法确定
# 用行的方法，把Series加入DataFrame，就是行，反之就是列。
import pandas as pd
列表1 = ['姓名','性别','年龄']
列表2 = ['付紫平','男',20]
数据 = pd.Series(列表2,index=列表1) # 指定谁是索引
print(数据)

# 常用方法
# 数据.index #查看索引
# 数据.values #查看数值
# 数据.isnull() #查看为空的，返回布尔型
# 数据.notnull()
# 数据.sort_index() #按索引排序
# 数据.sort_values() #按数值排序

