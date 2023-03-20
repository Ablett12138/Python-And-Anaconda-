#----------- 包 --------------#
import numpy as np


#------------------   创建numpy数组的3种方法   -------------#
a = np.array([1,2,3,4,5],dtype='float32') #指定数组类型
b = np.array(range(1,6),dtype='float32')
#推荐写法
c = np.arange(1,10,6)    #1-10 步长为6
print(a)
print(b)
print(c)
# array的属性：
# • shape：返回一个元组，表示 array的维度 [形状，几行几列] （2， 3）两行三列，（2， 2， 3）两个两行三列
# • ndim：返回一个数字，表示array的维度的数目
# • size：返回一个数字，表示array中所有数据元素的数目
# • dtype：返回array中元素的数据类型

print(a.dtype) # int32或int64
print(type(a)) # <class 'numpy.ndarray'>
print(a.shape) # 返回大小
print(a.ndim)  # 返回维度

#------------------   创建numpy统一数组的方法   -------------#
# 参数：
# shape：整数或者整型元组定义返回数组的形状；可以是一个数（创建一维向量），也可以是一个元组（创建多维向量）
# dtype : 数据类型，可选定义返回数组的类型。
# order : {‘C’, ‘F’}, 可选规定返回数组元素在内存的存储顺序：C（C语言） -rowmajor；F（Fortran）column-major。
# np.ones(shape,dtype=None,order='C')
a=np.ones(3) # 返回 array([1. 1. 1.])
b=np.ones((2,3))
b=np.ones((5,6), dtype='int') # 返回 五行六列



# 参数：
# a：用a的形状和数据类型，来定义返回数组的属性
# dtype ： 数据类型，可选
# order顺序 ： {'C'，'F'，'A'或'K'}，可选,覆盖结果的内存布局。
# subok ： bool，可选。True：使用a的内部数据类型，False：使用a数组的数据类型，默认为True
# 返回：与a相同形状和数据类型的数组，并且数组中的值都为1
c=np.ones_like(a,dtype=float,order='C',subok=True)
print(a)
print(b)
print(c)


# 参数：
# shape：整数或者整型元组定义返回数组的形状；可以是一个数（创建一维向量），也可以是一个元组（创建多维向量）
# dtype : 数据类型，可选定义返回数组的类型。
# order : {‘C’, ‘F’}, 可选规定返回数组元素在内存的存储顺序：C（C语言） -rowmajor；F（Fortran）column-major。
# np.zeros(shape,dtype=None,order='C')
a=np.zeros(10) #返回：[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
b=np.zeros((2,4),dtype='int')
# 返回：与b相同形状和数据类型的数组，并且数组中的值都为0
c=np.zeros_like(b,dtype=float)
print(a)
print(b)
print(c)


# 参数：
# shape：整数或者整型元组定义返回数组的形状；可以是一个数（创建一维向量），也可以是一个元组（创建多维向量）
# fill_value：标量（就是纯数值变量）
# dtype : 数据类型，可选定义返回数组的类型。
# order : {‘C’, ‘F’}, 可选规定返回数组元素在内存的存储顺序：C（C语言） -rowmajor；F（Fortran）column-major。
# np.full(shape,fill_value,dtype=None,order='C')
a=np.full((3,3),520,dtype='float32',order='C')
# 返回：与a相同形状和数据类型的数组，并且数组中的值都为fill_value
b=np.full_like(a,520,dtype='int')
print(b)

#------------------   创建numpy多维数组的方法   -------------#
