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

print('# ------------------------------    DataFrame是一个表格型的数据结构  ----------------------------------#')
# 每列可以是不同的值类型（数值、字符串、布尔值等）
# • 既有行索引index，也有列索引columns
# • 可以被看做由Series组成的字典
# DataFrame是一个表格型的数据结构
# 创建DataFrame最常用的方法，参考读取CSV、 TXT、 Excel、 MySQL等

数据=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(数据)

# a列0行的表现方法

print(数据['a'][0] )

# a. 数据.loc方法：根据行，列的标签值查询
# b. 数据.iloc方法：根据行，列的数字位置查询

# loc就根据这个index来索引对应的行。
print(数据.loc[0]['a'] )
# iloc并不是根据index来索引，而是根据行号来索引，行号从0开始，逐次加1。
print(数据.iloc[0][0] )

# 输出 a列和b列
print(数据[['a','b']])


# 3.2.1 多个字典序列创建DataFrame

字典 = {
'姓名':['孙兴华','李小龙','叶问'],
'年龄':[20,80,127],
'功夫':['撸铁','截拳道','咏春']
}
数据 = pd.DataFrame(字典)
print(数据)
print(数据.dtypes) # 返回每一列的类型
print(数据.columns) # 返回列索引，以列表形式返回： [列名1，列名2， …]
print(数据.index) # 返回行索引，（起始，结束，步长）
# • 如果只查询一列，返回的是pd.Series
# 3.2.2 从DataFrame中查询出Series
print(数据['姓名']) # 返回索引和这一列数据
# • 如果只查询一行，返回的是pd.Series
type(数据['姓名']) # 类型返回Series
print(数据.loc[1]) # 这时，它的索引是列名
print(数据.loc[1]['姓名']) #指定行和列查找
# • 如果查询多列，返回的是pd.DataFrame
type(数据.loc[1]) # 类型返回Series
print(数据[['姓名','年龄']]) # 返回索引和这两列数据
# • 如果查询多行，返回的是pd.DataFrame
type(数据[['姓名','年龄']]) # 类型返回DataFrame
print(数据.loc[1:3]) # 返回前3行，包括结束值
type(数据.loc[1:3]) # 类型返回DataFrame


# 3.2.3 将多个Series加入DataFrame
# 注： 3个数据的index他有对齐的功能，例如把数据3的index改成2， 3， 4，没有值的地方会显示nan
数据1 = pd.Series(['叶问','李小龙','孙兴华'],index=[1,2,3],name='姓名')
数据2 = pd.Series(['男','男','男'],index=[1,2,3],name='性别')
数据3 = pd.Series([127,80,20],index=[1,2,3],name='年龄')
表1 = pd.DataFrame({数据1.name:数据1,数据2.name:数据2,数据3.name:数据3})
print(表1)
表2 = pd.DataFrame([数据1,数据2,数据3])
print(表2)

#             常用方法
数据.head( 5 ) #查看前5行
数据.tail( 3 ) #查看后3行
数据.values #查看数值
数据.shape #查看行数、列数
数据.fillna(0) #将空值填充0
数据.replace( 1, -1) #将1替换成-1
数据.isnull() #查找数据中出现的空值
数据.notnull() #非空值
数据.dropna() #删除空值
# 数据.unique() #查看唯一值
数据.reset_index() #修改、删除，原有索引，详见例1
数据.columns #查看数据的列名
数据.index #查看索引
数据.sort_index() #索引排序
# 数据.sort_values() #值排序
pd.merge(数据1,数据1) #合并
pd.concat([数据1,数据2]) #合并，与merge的区别，自查
# pd.pivot_table( 数据 ) #用df做数据透视表（类似于Excel的数透）

print('# ------------------------------   merge函数的使用  ----------------------------------#')
# 首先merge的操作非常类似sql里面的join，实现将两个Dataframe根据一些共有的列连接起来，当然，在实际场景中，这些共有列一般是Id，
# 连接方式也丰富多样，可以选择inner(默认)，left,right,outer 这几种模式，分别对应的是内连接，左连接，右连接，全外连接


数据1= pd.DataFrame({'姓名':['叶问','李小龙','孙兴华','李小龙','叶问','叶问'],'出手次数1':np.arange(6)})
数据2 = pd.DataFrame({'姓名':['黄飞鸿','孙兴华','李小龙'],'出手次数2':[1,2,3]})
数据3 = pd.merge(数据1,数据2)
print(数据3)
数据3 = pd.merge(数据1,数据2,on='姓名',how='inner')
print(数据3)

数据3 = pd.merge(数据1,数据2,on='姓名',how='left')
print(数据3)

数据3 = pd.merge(数据1,数据2,on='姓名',how='right')
print(数据3)


数据3 = pd.merge(数据1,数据2,on='姓名',how='outer')
print(数据3)

print('# ------------------------------   join函数的使用  ----------------------------------#')
# 其实通过这一个小例子大家也就明白了，join无非就是合并，默认是横向，还有一个点需要注意的是，我们其实可以通过join实现和merge一样的效果，但是为了
# 避免混淆，我不会多举其他的例子了，因为我个人认为一般情况下还是用merge函数好一些
左字典={'姓名1':['叶问','李小龙','孙兴华'],'年龄1':[127,80,20]}
右字典={'姓名2':['大刀王五','霍元甲','陈真'],'年龄2':[176,152,128]}
左 = pd.DataFrame(左字典)
右 = pd.DataFrame(右字典)
print(左.join(右))

print('# ------------------------------   concat函数的使用  ----------------------------------#')
arr = np.arange(9).reshape((3,3))
print(arr)
# 按照axis=1轴拼接 -- 列
arr1 = np.concatenate([arr,arr],axis=1)
print(arr1)
# 按照axis=0轴拼接 -- 行
arr2 = np.concatenate([arr,arr],axis=0)
print(arr2)

# 分别创建了两个没有重复Index的Series,然后用concat默认的把它们合并在一起，这时生成的依然是Series类型，
数据1 = pd.Series([0,1,2],index=['A','B','C'])
数据2 = pd.Series([3,4],index=['D','E'])
数据3 = pd.concat([数据1,数据2])
print(数据3)
# 如果我们把axis换成1，那生成
# 的就是Dataframe,像下面一样
数据4 = pd.concat([数据1,数据2],axis=1,sort =True) # sort=Ture是默认的，pandas总是默认index排序，默认axis=0
print(数据4)


# 1.相同字段收尾连接
# frames = [df1, df2, df3]
# result = pd.concat(frames)

# 2.要在相接的时候在加上一个层次的key来识别数据源自于哪张表，可以增加key参数
# result = pd.concat(frames, keys=['x', 'y', 'z'])

# 3.当axis = 1的时候，concat就是行对齐，然后将不同列名称的两张表合并
# result = pd.concat([df1, df4], axis=1)

# 4.加上join参数的属性，如果为’inner’得到的是两表索引的交集，如果是outer，得到的是两表的并集。
# result = pd.concat([df1, df4], axis=1, join='inner')

# 5.如果有join_axes的参数传入，可以指定根据那个轴来对齐数据
# 例如根据df1表对齐数据，就会保留指定的df1表的轴，然后将df4的表与之拼接
# result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])

print('# ------------------------------   合并的同时增加区分数据组的键  ----------------------------------#')
# 1.要在相接的时候在加上一个层次的key来识别数据源自于哪张表，可以增加key参数
# result = pd.concat(frames, keys=['x', 'y', 'z'])

# 2.传入字典来增加分组键  ----====---等价于 # result = pd.concat(frames, keys=['x', 'y', 'z'])
# pieces = {'x': df1, 'y': df2, 'z': df3}
# result = pd.concat(pieces)



print('# ------------------------------   append函数的使用  ----------------------------------#')
# 1.append是series和dataframe的方法，使用它就是默认沿着列进行凭借（axis = 0，列对齐）
# result = df1.append(df2)

# 2.如果两个表的index都没有实际含义，使用ignore_index参数，置true，合并的两个表就是根据列字段对齐，然后合并。最后再重新整理一个新的index。

# 3.append方法可以将 series 和 字典的数据作为dataframe的新一行插入
# s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
# result = df1.append(s2, ignore_index=True)

# 4.如果遇到两张表的列字段本来就不一样，但又想将两个表合并，其中无效的值用nan来表示。那么可以使用ignore_index来实现
# dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4}, {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]
# result = df1.append(dicts, ignore_index=True)
