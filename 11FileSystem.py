
# coding: utf-8

# In[1]:


#11-1：处理文件中数据的例子
def file_hdl(name='python.txt'):
    f = open(name)
    res = 0
    i = 0
    for line in f:
        i += 1
        print('第%s行的数据为：' % line.strip(),line)
        res += int(line)
        
    print('这些数的和为：',res)
    f.close()
    
if __name__ == '__main__':
    file_hdl()


# In[4]:


#fileinput模块的使用
import fileinput
def demo_fileinput():
    with fileinput.input(['fpa.txt','fpb.txt']) as lines: #fileinput.input()返回能够用于迭代一个或多个文件中所有行的对象
        for line in lines:
            print('总第%d行,' % fileinput.lineno(),
                 '文件%s中第%d行：' %
                 (fileinput.filename(),fileinput.filelineno()))
            print(line.strip())
            
if __name__ == '__main__':
    demo_fileinput()


# In[5]:


#获取当前路径
import os
print('当前目录是:',os.getcwd())


# In[6]:


#获取指定目录中的内容
os.listdir()


# In[7]:


#创建目录
os.mkdir('test2')
os.listdir()


# In[8]:


#删除目录
os.rmdir('test2')
os.listdir()


# In[9]:


#判断是否是目录
os.path.isdir('test')


# In[10]:


#判断是否是文件
os.path.isfile('test')


# In[11]:


#遍历当前目录
for i in os.walk('.\\'):
    print(i)


# In[14]:


#由文件名批量获取姓名和考号
import os

filenames = []

for a,b,files in os.walk('test'):
    if files:
        filenames.append([file[:-4] for file in files])
        
fname = 'testexam'

i = 0
for files in filenames:
    f = open(fname + str(i) + '.xls','w')
    for name in files:
        f.write(name[-2]+'\t'+name[:-2]+'\n')
    f.close()
    i += 1
print('成功生成！')
    

