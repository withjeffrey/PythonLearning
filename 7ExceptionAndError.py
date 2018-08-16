
# coding: utf-8

# In[1]:


#7-1：拼写错误NameError
for i in range(3):
    printt(i)


# In[2]:


#7-2：异常处理
def testTry(index,flag=False):
    stulst = ['John','Jenny','Tom']
    if flag:
        try:
            astu = stulst[index]
        except IndexError:
            print('IndexError')
        return 'Try Test Finished!'
    else:
        astu = stulst[index]
        return 'No Try Test Finished!'
print('Right params testing start...')
print(testTry(1,True))
print(testTry(1,False))
print('Error params testing start...')
print(testTry(4,True))
print(testTry(4,False))


# In[3]:


#7-3：运用finally语句块来确保文件使用后能关闭该文件
def testTryFinally(index):
    stulst = ['John','Jenny','Tom']
    af = open('my.txt','wt+')
    try:
        af.write(stulst[index])
    except:
        pass
    finally: #无论程序是否产生异常，都关闭文件
        af.close()
        print('File already had beed closed!')
print('No IndexError...')
testTryFinally(1)
print('IndexError...')
testTryFinally(4)


# In[4]:


#7-4：程序中若捕获所有异常，程序运行引发什么异常都不会中断
def testTryAll(index,i):
    stulst = ['John','Jenny','Tom']
    try:
        print(len(stulst[index])/i)
    except: #捕获所有异常
        print('Error!')
        
print('Try all...Right')
testTryAll(1,2)
print('Try all...one Error')
testTryAll(1,0) #除零异常
print('Try all...two Error')
testTryAll(4,0) #除零异常+越界异常


# In[5]:


#7-5：程序捕获了部分异常，当运行时引发了不能被捕获的异常时仍然中断
def testTryOne(index,i):
    stulst = ['John','Jenny','Tom']
    try:
        print(len(stulst[index])/i)
    except IndexError: #指明IndexError异常
        print('Error!')

print('Try one...Right')
testTryOne(1,2)
print('Try one...one Error')
testTryOne(4,2)
print('Try one...one Error')
testTryOne(1,0)


# In[6]:


#7-6：使用代码抛出异常，没有捕获该异常，导致后面代码不能运行
def testRaise():
    for i in range(5):
        if i==2:
            raise NameError
        print(i)
    print('end...')
testRaise()


# In[8]:


#7-7：代码抛出异常，捕获该异常，程序运行不会中断
def testRaise2():
    for i in range(5):
        try:
            if i==2:
                raise NameError
        except NameError:
            print('Raise a NameError!')
        print(i)
    print('end...')
testRaise2()


# In[9]:


#7-8：使用assert抛出异常，捕获该异常
def testAssert():
    for i in range(3):
        try:
            assert i<2
        except AssertionError:
            print('Raise an AssertionError!')
        print(i)
    print('end...')
testAssert()


# In[10]:


#自定义一个异常类，引发异常
class RangeError(Exception):
    
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return self.value
    
raise RangeError('Range Error!')


# In[ ]:


#7-10：交互模式下pdb模型调试
import pdb
pdb.run("""
for i in range(3):
    print(i)
""")


# In[ ]:


#7-11：交互模式下pdb模块调试函数
import pdb

def sum(maxint):
    s = 0
    for i in range(maxint):
        s += i
    return s

pdb.runcall(sum,10)


# In[ ]:


#7-12：使用doctest模块的testmod函数进行基本的单元测试
#python -m doctest -7-12.py
import pdb
def grade(sum):
    """ 
    >>> grade(100)
    '优秀'
    >>> grade(80)
    '良好'
    >>> grade(60)
    '及格'
    >>> grade(10)
    '不及格'
    """
    if sum > 90:
        return '优秀'
    if sum > 80:
        return '良好'
    if sum > 60:
        return '及格'
    if sum < 60:
        return '不及格'

if name == '__main__': #当模块直接运行时，代码直接运行；如果是导入则不运行
    import doctest
    doctest.testmod()

#也可以把测试用例写入txt文件，然后用下面的语句执行
#import doctest
#doctest.testfile('mytest.txt')
#txt文件开头写入from test import grade

