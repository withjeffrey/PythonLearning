
# coding: utf-8

# In[1]:


#10-1：函数与其全局命名空间关系的实例
#说明：函数中引用的全局变量始终是定义该函数模块中的全局变量！
#foo.py
#name = "Foo module"

#def foo_fun():
#    print('函数foo_fun:')
#    print('变量name:',name)
    
#a10-1.py
#导入foo模块
from foo import foo_fun

name = 'Current module'
def bar():
    print('当前模块中函数bar:')
    print('变量name:',name)
    
def call_foo_fun(fun):
    fun()
    
if __name__ == '__main__':
    bar()
    print()
    foo_fun()
    print()
    call_foo_fun(foo_fun)


# In[2]:


#闭包是指Python中将组成函数的语句和这些语句的执行环境打包到一起所得到的对象
#10-2:嵌套函数例子
x = 14

def foo():
    x = 3
    def bar():
        print('x is %d' % x)
    bar() #调用嵌套的内层函数
    
if __name__ == '__main__':
    foo()


# In[4]:


#10-3：闭包达到延迟求值的实例
def delay_fun(x,y):
    def caculator():
        return x + y
    return caculator

if __name__ == '__main__':
    print('返回一个求和函数，并不求和')
    msum = delay_fun(3,4) #第一次调用返回嵌套函数，把参数x,y传入外层函数中
    print()
    print('调用并求和:')
    print(msum()) #第二次调用返回的函数时才执行计算并返回结果


# In[5]:


#10-4：闭包达到泛型函数定义的实例
def line(a,b):
    def aline(x):
        return a*x + b
    return aline

if __name__ == '__main__':
    line23 = line(2,3)
    line50 = line(5,0)
    print(line23(4))
    print(line50(2))


# In[7]:


#上下文管理器是指实现了上下文管理协议方法的对象
#上下文管理器的协议方法有__enter__(self)和__exit__(self,type,value,tb)
#10-5：自定义一个上下文管理器及其使用方法
class FileMgr:
    
    def __init__(self,filename):
        self.filename = filename
        self.f = None
        
    def __enter__(self):
        self.f = open(self.filename,encoding='utf-8')
        return self.f
    
    def __exit__(self,t,v,tb):
        if self.f:
            self.f.close()
            
if __name__ == '__main__':
    with FileMgr('a10-4.py') as f:
        for line in f.readlines():
            print(line,end='')


# In[8]:


#10-6：通过装饰器contextmanager实现一个上下文管理器
import contextlib

@contextlib.contextmanager
def my_mgr(s,e):
    print(s)
    yield s + ' ' + e
    print(e)
    
if __name__ == '__main__':
    with my_mgr('start','end') as val:
        print(val)


# In[10]:


#10-7：通过setattr()修改对象属性的实例
class DemoClass:
    class_val = 3
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.info()
        
    def info(self):
        print('类属性class_val: ',DemoClass.class_val)
        print('实例属性x: ',self.x)
        print('实例属性y: ',self.y)
        
if __name__ == '__main__':
    dc = DemoClass()
    if hasattr(DemoClass,'class_val'):
        setattr(DemoClass,'class_val',1000)
    if hasattr(dc,'x'):
        setattr(dc,'x','xxxxxxxx')
    if hasattr(dc,'y'):
        setattr(dc,'y','yyyyyyyy')
    dc.info()
    setattr(dc,'z','zzzzzzzz')
    print('添加的属性z',dc.z)


# In[11]:


#10-5：用字典构造分支程序
import random
#以下定义三个分支函数
def path_a():
    print('A')
    
def path_b():
    print('B')
    
def path_c():
    print('C')
    
if __name__ == '__main__':
    path_dict = {}
    path_dict['a'] = path_a
    path_dict['b'] = path_b
    path_dict['c'] = path_c
    paths = 'abc'
    for i in range(4):
        path = random.choice(paths)
        print('选择了路径：',path)
        path_dict[path]()


# In[12]:


#Python中带有双下划线的方法是类的专有方法
#自定义类，实现类的特别的运算方式
class Book:
    
    def __init__(self,name='Python从入门到精通'):
        self.name = name
        
    def __add__(self,obj):
        return self.name + ' add ' + obj.name
    
    def __len__(self):
        return len(self.name)

if __name__ == '__main__':
    booka = Book()
    bookb = Book('Java从入门到精通')
    print('len(booka):',len(booka))
    print('len(bookb):',len(bookb))
    print(booka + bookb)


# In[16]:


#Python语言属于动态类型语言，变量的类型是不确定。鸭子类型是动态类型的一种风格，一个对象有效的语义不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定
#10-10：鸭子类型的使用实例
class Duck:
    def __init__(self,name='duck'):
        self.name = name
        
    def quack(self):
        print('嘎嘎嘎...')
        
class Cat:
    def __init__(self,name='cat'):
        self.name = name
    
    def quack(self):
        print('喵喵喵...')
        
class Tree:
    def __init__(self,name='tree'):
        self.name = name
        
def duck_demo(obj):
    obj.quack()
        
if __name__ == '__main__':
    duck = Duck()
    cat = Cat()
    tree = Tree()
    duck_demo(duck)
    duck_demo(cat)
    duck_demo(tree)

