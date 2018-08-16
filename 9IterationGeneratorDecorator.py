
# coding: utf-8

# In[2]:


#迭代器可以看成实现了__iter()__和__next__()方法的类
#9-1：迭代器示例
class MyIterator:
    
    def __init__(self,x=2,xmax=100):
        self.__mul,self.__x = x,x
        self.__xmax = xmax
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__xmax:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration
            
if __name__ == '__main__':
    myiter = MyIterator()
    for i in myiter:
        print("迭代的元素为：",i)


# In[3]:


#9-2：产生迭代器的内建函数iter()
class Counter:
    def __init__(self,x=0):
        self.x = x
        
counter = Counter()

def used_iter():
    counter.x += 2
    return counter.x

for i in iter(used_iter,8):
    print("迭代的元素为:",i)
        


# In[4]:


#itertools模块的迭代工具函数
import itertools
for i in itertools.count(1,3): #从start开始，以step为步进计数迭代
    print(i)
    if i >= 10:
        break


# In[5]:


x = 0
for i in itertools.cycle(['a','b']): #无限循环迭代
    print(i)
    x += 1
    if x >= 6:
        break


# In[6]:


list(itertools.repeat(3,3))


# In[7]:


list(itertools.chain([1,3],[2,3]))


# In[8]:


list(itertools.compress([1,2,3,4],[1,[],True,3]))


# In[9]:


list(itertools.dropwhile(lambda x:x>6, [8,9,1,2,8,9]))


# In[10]:


list(itertools.takewhile(lambda x:x>10, [18,19,1,21,8,9]))


# In[11]:


for its in itertools.tee([0,1],2):
    for it in its:
        print(it)


# In[12]:


list(itertools.permutations('abc',2))


# In[13]:


list(itertools.combinations('abc',2))


# In[15]:


#生成器对象是通过使用关键字yield生成的函数对象
#9-3：生成器示例
def myYield(n):
    while n>0:
        yield n
        n -= 1

if __name__ == '__main__':
    for i in myYield(4):
        print(i)
    print()
    
    my_yield = myYield(3) #手动生成
    print(my_yield.__next__())
    print(my_yield.__next__())


# In[17]:


#9-4：生成器可以接收调用者传来的值并重新初始化生成器生成的值
def myYield(n):
    while n>0:
        rcv = yield n
        n -= 1
        if rcv is not None:
            n = rcv

if __name__ == '__main__':
    my_yield = myYield(3)
    print(my_yield.__next__())
    print(my_yield.__next__())
    print(my_yield.send(10))
    print(my_yield.__next__())


# In[18]:


#类似列表的生成器表达式
a = (i for i in range(5))
list(a)


# In[19]:


#9-5：一个生成器协程
def consumer():
    print('等待任务：')
    while True:
        data = (yield)
        print('收到任务：',data)
        
def producer():
    c = consumer()
    c.__next__()
    for i in range(3):
        print('发送任务：','任务%d' % i)
        c.send('任务%d' % i)
        
if __name__ == '__main__':
    producer()


# In[26]:


#装饰器是一种增加函数或类的功能的方法
#9-6：自定义一个装饰器并用来装饰一个自定义函数
def abc(fun):
    def wrapper(*args,**kwargs):
        print('开始运行：')
        fun(*args,**kwargs) #调用被装饰函数
        print('结束运行！')
    return wrapper
    
@abc
def demo_decoration(x):
    a = []
    for i in range(x):
        a.append(i)
    print(a)
    
@abc
def hello(name):
    print('Hello ',name)

if __name__ == '__main__':
    demo_decoration(5)
    print()
    hello('John')


# In[27]:


#9-7：类装饰器例子
def abc(myclass):
    class InnerClass:
        def __init__(self,z=0):
            self.z = 0
            self.wrapper = myclass()
            
        def position(self):
            self.wrapper.position()
            print('z axis:',self.z)
    return InnerClass

@abc
class coordination:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def position(self):
        print('x axis:',self.x)
        print('y axis:',self.y)

if __name__ == '__main__':
    coor = coordination()
    coor.position()

