# coding:utf-8
import requests
from requests_html import HTMLSession
import re

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('请输入你要查询的京东商品')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show=None)  # 显示成明文形式
e.pack()


# 第5步，开始爬取，并输出




def search():  # 在文本框内容最后接着插入输入内容
    keyword = e.get()
    session = HTMLSession()
    r = session.get('https://search.jd.com/Search?keyword=' + keyword)
    link_list1 = r.html.find('.p-shop')
    link_list2 = r.html.find('.p-price')
    link_list3 = r.html.find('.p-icons')
    link_list4 = r.html.find('.p-name')
    k = 0
    print_text = ""
    var = ""
    file_title = keyword + ".txt"
    file = open(file_title,"w",encoding='UTF-8')
    for i in link_list1:

        text = re.sub('[\n\r]', '', link_list4[k].text)
        if(link_list2[k].text == ""):
            print("价格")
        else:
            text1 =  link_list2[k].text + '\n'
        if(link_list3[k].text == ""):
            print("没特殊标签")
        else:
            text1 = text1 + link_list3[k].text + '\n'
        if(text == ""):
            print("没形容语句")
        else:
            text1 = text1 + text + '\n'
        if(i.text == ""):
            print("没商店")
        else:
            text1 = text1 + i.text + '\n'
        text1 = text1 + '\n'
        k = k + 1
        file.write(text1);
    # 创建一个空列表
    file.close()
    tkinter.messagebox.showinfo(title='结果', message='已完成')


# 第6步，创建并放置按钮触
b1 = tk.Button(window, text='查询', width=10, height=2, command=search)
b1.pack()


# 第8步，主窗口循环显示
window.mainloop()