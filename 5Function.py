
# coding: utf-8

# In[14]:


#函数
#例子5-1：声明和调用函数
def hello():
    print("Hello, World!")

#例子5-2：声明和调用函数
def tpl_sum(T):
    result = 0
    for i in T:
        result += i
    return result

hello()
print("The sum of (1, 2, 3) is:", tpl_sum((1,2,3)))


# In[16]:


#例子5-3：带默认值参数的函数
def hello(name="World"):
    print("Hello, %s!" %name)

print("No parameter: ")
hello()
print("Has a parameter Jonson: ")
hello("Jeffrey")

#注意：如果参数列表同时包含默认值参数和参数，那么需要先声明无默认值参数，后声明默认值参数
def test(a, b=3):
    pass
print("\n")
#例子5-4：带有两个默认值参数的函数
def hello(hi="hi",name="World"):
    print("%s, %s!" % (hi, name))

print("One parameter: ")
hello("Jeffrey")
print("Two parameters: ")
hello("hi","Jeffrey")


# In[17]:


#位置参数，参数传递按照参数的位置顺序进行传递
def mult_test(a,b,c):
    return a*b*c
mult_test(2,c=5,b=3) #按位置和参数名传递参数


# In[22]:


#例子5-5：带可变长参数的函数
def change_para_num(*tpl):
    print(type(tpl))
    print(tpl)

change_para_num(1)
change_para_num(1,2,3)

print("\n")
#例子5-6：带默认值参数、位置参数、可变长参数的函数
def change_para_num(*tpl,a,b=0):
    print("tpl:",tpl)
    print("a:",a)
    print("b:",b)

change_para_num(1,2,3,a=5)
#change_para_num(1,2,3) Error

print("\n")
#例子5-7：收集关键字参数的函数
def change_para_dct(a,b=0,**adct):
    print("adct:",adct)
    print("a:",a)
    print("b:",b)
    
change_para_dct(1,k=3,b=2,c=3)

print("\n")
#例子5-8：带有大量默认参数的函数及其调用
def cube(name,**nature):
    all_nature = {"x":1,
                 "y":1,
                 "z":1,
                 "color":"white",
                 "weight":1}
    all_nature.update(nature)
    print(name,"the property of the cube:")
    print("volumn:",all_nature['x']*all_nature['y']*all_nature['z'])
    print("color:",all_nature['color'])
    print("weight:",all_nature['weight'])

cube('first')
cube('second',y=3,color='red')
cube('third',z=2,color='green',weight=10)


# In[23]:


#例子5-9：拆解元组的函数调用
def mysum(a,b):
    return a+b

print(mysum(*(3,4)))
print(mysum(**{'a':3,'b':4}))


# In[25]:


#例子5-10：可变和不可变元素作为函数参数
def change(aint,alst):
    aint = 0
    alst[0] = 0
    alst.append(4)

aint = 3
alst = [1,2,3]
change(aint,alst) #整数、浮点数、字符串、元组不可变，列表和字典可变
print(aint) #aint在函数内部修改时，函数外部的值不变
print(alst) #alst在函数内部修改时，函数外部的值改变


# In[28]:


#例子5-11：使用列表作为默认参数
def myfun1(lst=[]):
    lst.append('abc')
    print(lst)

myfun1()
myfun1()
myfun1()

print('\n')
def myfun2(lst=None):
    lst = [] if lst is None else lst
    lst.append('abc')
    print(lst)

myfun2()
myfun2()
myfun2()


# In[1]:


#例子5-12：全局作用域与局部作用域
def myfun():
    a = 0
    a += 3
    print(a)

a = 'external'
print(a)
myfun()
print(a)


# In[2]:


#例子5-13：global参数，在函数内使用全局变量
def myfun():
    global a
    a = 0
    a += 3
    print(a)

a = 'external'
print(a)
myfun()
print(a)


# In[3]:


#使用匿名函数
import math
s = lambda x1,y1,x2,y2:math.sqrt((x1-x2)**2+(y1-y2)**2)
s(1,2,3,4)


# In[8]:


#常用内建函数
#help(abs)
bin(20)
hex(20)
oct(20)
callable(abs)
chr(97)
ord('k')
##list(filter(lambda x:x % 2, [0,1,2,3,4]))
#list(map(lambda x:2*x, [0,1,2,3,4]))
#isinstance('abc',str)

