
# coding: utf-8

# In[1]:


#12-1：创建一个简单的窗口
# -*- coding:utf-8 -*-
import tkinter
root = tkinter.Tk()
root.mainloop()


# In[2]:


#12-2:具有标签和按钮组件的主窗口
# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
label = tkinter.Label(root, text="Hello, tkinter!")
label.pack()
button1 = tkinter.Button(root, text="Button1")
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(root, text="Button2")
button2.pack(side=tkinter.RIGHT)
root.mainloop()


# In[3]:


#12-3：在主窗口中创建各种不同按钮
# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
button1 = tkinter.Button(root,
                        anchor = tkinter.E,
                        text = "Button1",
                        width = 40,
                        height = 5)
button1.pack()
button2 = tkinter.Button(root,
                        text = "Button2",
                        bg = "Blue")
button2.pack()
button3 = tkinter.Button(root,
                        text = "Button3",
                        width = 14,
                        height =1)
button3.pack()
button4 = tkinter.Button(root,
                        text = "Button4",
                        width = 60,
                        height = 5,
                        state = tkinter.DISABLED)
button4.pack()
root.mainloop()


# In[6]:


#12-4：在主窗口中显示创建的各种不同类型的文本框
# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root,
                      show = '*')
entry1.pack()
entry2 = tkinter.Entry(root,
                      show = '#',
                      width = 50)
entry2.pack()
entry3 = tkinter.Entry(root,
                      bg = 'red',
                      fg = 'blue')
entry3.pack()
entry4 = tkinter.Entry(root,
                      selectbackground = 'red',
                      selectforeground = 'gray')
entry4.pack()
entry5 = tkinter.Entry(root,
                      state = tkinter.DISABLED)
entry5.pack()
edit1 = tkinter.Text(root,
                    selectbackground = 'red',
                    selectforeground = 'gray')
edit1.pack()
root.mainloop()


# In[7]:


#12-5：在主窗口显示创建的各种不同类型的标签组件
#
import tkinter
root = tkinter.Tk()
label1 = tkinter.Label(root,
                      anchor = tkinter.E,
                      bg = 'blue',
                      fg = 'red',
                      text = 'Python',
                      width = 30,
                      height = 5)
label1.pack()
label2 = tkinter.Label(root,
                      text = 'Python GUI\ntkinter',
                      justify = tkinter.LEFT,
                      width = 30,
                      height = 5)
label2.pack()
label3 = tkinter.Label(root,
                      text = 'Python GUI\ntkinter',
                      justify = tkinter.RIGHT,
                      width = 30,
                      height = 5)
label3.pack()
label4 = tkinter.Label(root,
                      text = 'Python GUI\ntkinter',
                      justify = tkinter.CENTER,
                      width = 30,
                      height = 5)
label4.pack()
root.mainloop()


# In[11]:


#12-6：添加菜单的主窗口
# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Open')
submenu.add_command(label='Save')
submenu.add_command(label='Close')
menu.add_cascade(label='File', menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Copy')
submenu.add_command(label='Paste')
submenu.add_separator()
submenu.add_command(label='Cut')
menu.add_cascade(label='Edit', menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='About')
menu.add_cascade(label='Help', menu=submenu)

root.config(menu=menu)
root.mainloop()


# In[12]:


#12-7：弹出式菜单（快捷或右键菜单）的主窗口
# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
menu = tkinter.Menu(root, tearoff=0)
menu.add_command(label='Copy')
menu.add_command(label='Paste')
menu.add_separator()
menu.add_command(label='Cut')

def popupmenu(event):
    menu.post(event.x_root, event.y_root)
root.bind("<Button-3>", popupmenu)
root.mainloop()


# In[13]:


#12-8：单选框和复选框
# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root,
                           variable = r,
                           value = '1',
                           text = 'Radio1')
radio.pack()
radio = tkinter.Radiobutton(root,
                           variable = r,
                           value = '2',
                           text = 'Radio2')
radio.pack()
radio = tkinter.Radiobutton(root,
                           variable = r,
                           value = '3',
                           text = 'Radio3')
radio.pack()
radio = tkinter.Radiobutton(root,
                           variable = r,
                           value = '4',
                           text = 'Radio4')
radio.pack()
c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root,
                           text = 'Checkbutton',
                           variable = c,
                           onvalue = 1,
                           offvalue = 2)
check.pack()
root.mainloop()
print(r.get())
print(c.get())

