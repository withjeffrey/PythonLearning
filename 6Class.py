
# coding: utf-8

# In[3]:


#6-1：类的定义与实例化
class MyClass:
    "MyClass help."
    
myclass = MyClass() 
print(myclass.__doc__) #输出类说明
help(myclass) #显示类帮助信息


# In[4]:


#6-2：类的方法的定义与使用
class SmplClass:
    def info(self):
        print('my class')
    def mycacl(self,x,y):
        return x + y
sc = SmplClass()
sc.info()
print(sc.mycacl(3,4))


# In[6]:


#6-3：__init__()方法用于类实例化时初始化相关数据
class DemoInit:
    def __init__(self,x,y=0):
        self.x = x
        self.y = y
        
    def mycacl(self):
        return self.x + self.y

dia = DemoInit(3)
print(dia.mycacl())

dib = DemoInit(3,7)
print(dib.mycacl())


# In[1]:


#例子6-4：在类中调用类自身的方法和全局函数的实例
def coord_chng(x,y):
    return (abs(x),abs(y))

class Ant:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.disp_point()
    
    def move(self,x,y):
        x,y = coord_chng(x,y)
        self.edit_point(x,y)
        self.disp_point()
        
    def edit_point(self,x,y):
        self.x += x
        self.y += y
        
    def disp_point(self):
        print("current position: (%d,%d)" % (self.x,self.y))

ant_a = Ant()
ant_a.move(2,4)
ant_a.move(-9,6)
        


# In[2]:


#例子6-5：类中定义的类属性和实例属性的定义及使用
#有时为了不让某个属性或方法在类外被调用或修改，可以使用双下划线的名称
#对实例的修改，会导致所有实例的类属性的值发生变化
class Demo_Property:
    class_name = "Demo_Property" #类属性
    
    def __init__(self,x=0):
        self.x = x #实例属性
    
    def class_info(self): #类方法，输出信息
        print("类变量值：",Demo_Property.class_name)
        print("实例变量值：",self.x)
    
    def chng(self,x): #类方法，修改实例属性
        self.x = x
    
    def chng_cn(self,name): #类方法，修改类属性
        Demo_Property.class_name = name
    
dpa = Demo_Property() #实例化类
dpb = Demo_Property()
print("初始化两个实例")
dpa.class_info()
dpb.class_info()
print("修改实例属性")
print("修改dpa实例属性")
dpa.chng(3)
dpa.class_info()
dpb.class_info()
print("修改dpb实例属性")
dpb.chng(10)
dpa.class_info()
dpb.class_info()
print("修改类属性")
print("修改dpa类属性")
dpa.chng_cn('dpa')
dpa.class_info()
dpb.class_info()
print('修改dpb类属性')
dpb.chng_cn('dpb')
dpa.class_info()
dpb.class_info()


# In[3]:


#例子6-6：定义类方法和静态方法（类的方法的另外两种类别）
class DemoMthd:
    
    @staticmethod
    def static_mthd():
        print("调用了静态方法！")
        
    @classmethod
    def class_mthd(cls):
        print("调用了类方法！")
DemoMthd.static_mthd()
DemoMthd.class_mthd()
dm = DemoMthd()
dm.static_mthd()
dm.class_mthd()


# In[4]:


#例子6-7：类的继承
class Ant:
    
    def __init__(self,x=0,y=0,color='black'):
        self.x = x
        self.y = y
        self.color = color
    
    def crawl(self,x,y):
        self.x = x
        self.y = y
        print('crawl...')
        self.info()
    
    def info(self):
        print('当前位置：(%d,%d)' % (self.x,self.y))
        
    def attack(self):
        print('用嘴咬！')
        
class FlyAnt(Ant):
    
    def attack(self): #attack()方法被重载了
        print('用尾针！')
        
    def fly(self,x,y):
        print('fly...')
        self.x = x
        self.y = y
        self.info()
        
flyant = FlyAnt(color='red')
flyant.crawl(3,5)
flyant.fly(10,14)
flyant.attack()


# In[9]:


#例子6-8：多重继承
class PrntA:
    
    namea = 'PrntA'
    
    def set_value(self,a):
        self.a = a
    
    def set_namea(self,namea):
        PrntA.namea = namea
        
    def info(self):
        print('PrntA:%s,%s' % (PrntA.namea,self.a))
        
class PrntB:
    
    nameb = 'PrntB'
    
    def set_nameb(self,nameb):
        PrntA.nameb = nameb
        
    def info(self):
        print('PrntB:%s' % (PrntB.nameb,))
        
class Sub(PrntA,PrntB):
    pass

class Sub2(PrntB,PrntA):
    pass

class Sub3(PrntA,PrntB):
    
    def info(self): #info()方法被重载了
        PrntA.info(self)
        PrntB.info(self)
        
print('使用第一个子类：')
sub = Sub()
sub.set_value('aaaa')
sub.info()
sub.set_nameb('BBBB')
sub.info()
print('使用第二个子类：')
sub2 = Sub2()
sub2.set_value('aaaa')
sub2.info()
sub2.set_nameb('BBBB')
sub2.info()
print('使用第三个子类：')
sub3 = Sub3()
sub3.set_value('aaaa')
sub3.info()
sub3.set_nameb('BBBB')
sub3.info()

