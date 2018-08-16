
# coding: utf-8

# In[7]:


#正则表达式是指用某种模式去匹配一类具有共同特征的字符串
#re模块是Python语言提供的处理正则表达式的标准库
import re
s = 'Lift can be good'
print(re.match('can',s)) #匹配模式为can，匹配字符串为s，无匹配标志；
                         #re.match()函数只从字符串中第一个字符开始匹配
print(re.search('can',s))
print(re.match('l.*',s))
print(re.match('l.*',s,re.I))
print(re.findall('[a-z]{1,3}',s))


# In[13]:


#re.sub()和re.subn()函数
import re
s = 'Life can be bad'
re.sub('bad','good',s)
re.sub('bad|be','good',s)
re.sub('bad|be','good',s,1)
re.subn('bad|be','good',s,1)
r = re.subn('bad|be','good',s)
print(r[0])
print(r[1])


# In[16]:


#re.split()
import re
s = 'Life can be bad'
re.split(' ',s)
r = re.split(' ',s,1)
for i in r:
    print(i)
re.split('b',s)


# In[25]:


#re.compile()，将正则表达式编译生成一个RegexObject对象实例，通过实例对字符串进行操作，提高处理或匹配速度
import re
re.compile('a*b',re.I|re.X)

