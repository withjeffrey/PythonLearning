
# coding: utf-8

# In[1]:


#8-1：导入模块
import math
from math import sqrt
import math as shuxue

print('调用math.sqrt:\t',math.sqrt(2))
print('直接调用sqrt:\t',sqrt(2))
print('调用shuxue.sqrt:\t',shuxue.sqrt(2))


# In[3]:


#自定义模块并导入和调用其中的函数
#模块文件
#文件名称：module_test.py
print('导入的测试模块的输出')

name = 'moduel_test'
def m_t_pr():
    print('模块module_test中的m_t_pr()函数')
    
#调用自己编写的模块
#文件名：8-2.py
import module_test
module_test.m_t_pr()
print('使用module_test模块中的变量：',module_test.name)


# In[4]:


import sys #导入sys模块
sys.path.append('D:\\lx\\module') #添加模块查找路径


# In[6]:


#pyc是py编译成字节码后的文件，可以使用compile模块进行编译
#import py_compile
#py_compile.compile('a8_2.py','a8_2.pyc')


# In[7]:


#在Python中，每个程序运行时都有一个__name__属性
#如果程序作为模块导入，则__name__属性被设置为模块名
#如果程序独立运行，则__name__属性被设置为__main__
#可以使用内建函数dir输出模块中的变量名和函数名


# In[13]:


#一个包结构，包其实就是一个文件夹或目录，包含一个__init__.py文件
#当前目录下pcka子目录中__init__.py文件的内容
name = 'pcka'
print('__init__.py中输出：',name)

def pck_test_fun():
    print('pcka包中的方法pck_test_fun')

#主程序文件
import pcka
print('输出pcka包中变量name:',pcka.name)
print('调用pcka包中函数:',end='')
pcka.pck_test_fun()


# In[22]:


import random
random.random() #生成0-1之间的随机数
random.randint(0,10) #生成0-10之间随机整数
random.choice((1,2,3,4))
alst = [1,2,3,4,5,6]
random.shuffle(alst) #该函数返回值是None
alst


# In[26]:


import time
import datetime
import calendar
time.time() #获取自初始时间至现在的秒数
datetime.datetime.now()
datetime.datetime.utcnow()

