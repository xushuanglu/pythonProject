# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

def hello(str):
    print({str})


class MyClass:
    """11"""
    i = 12345
    def f(self):
        return 'hello world'

# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


import keyword
import sys
import socket

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(keyword.kwlist)

    host = socket.gethostname()
    print("host:" + host)



    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart


    x = Complex(3.0, -4.5)
    print(x.r, x.i)  # 输出结果：3.0 -4.5

    # 实例化类
    x = MyClass()
    # 访问类的属性和方法
    print("MyClass 类的属性 i 为：", x.i)
    print("MyClass 类的方法 f 输出为：", x.f())

    str = '123456789'
    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(str[0])  # 输出字符串第一个字符
    print(str[2:5])  # 输出从第三个开始到第五个的字符
    print(str[2:])  # 输出从第三个开始后的所有字符
    print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(str * 2)  # 输出字符串两次
    print(str + '你好')  # 连接字符串

    print('------------------------------')

    print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


    # input("\n\n按下 enter 键后退出。")

    x = 'runoob';
    sys.stdout.write(x + '\n')

    #基本数据类型
    counter = 100
    miles = 1000.0
    name = "aaaaaaaaaaaa".capitalize()

    print(counter)   #赋值整数型变量
    print(miles)     #赋值小数型变量
    print(name)      #字符串

    #Python 有5个标准的数据类型
    a = 111
    print(isinstance(a,int))

    #List数据类型
    print("List数据类型===================================================>")
    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']

    print(list)  # 输出完整列表
    print(list[0])  # 输出列表第一个元素
    print(list[1:3])  # 从第二个开始输出到第三个元素
    print(list[2:])  # 输出从第三个元素开始的所有元素
    print(tinylist * 2)  # 输出两次列表
    print(list + tinylist)  # 连接列表


    #元组
    tuple = ('abcd',786,2.23,'runoob',70.2)
    tinytuple = (123,'runoob')

    print("******************************************************************")
    print(tuple)  # 输出完整元组
    print(tuple[0])  # 输出元组的第一个元素
    print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
    print(tuple[2:])  # 输出从第三个元素开始的所有元素
    print(tinytuple * 2)  # 输出两次元组
    print(tuple + tinytuple)  # 连接元组


    #Python逻辑运算符

    print("******************************************************************")
    a = 10
    b = 20

    if (a and b):
        print("1 - 变量 a 和 b 都为 true")
    else:
        print("1 - 变量 a 和 b 有一个不为 true")

    if (a or b):
        print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("2 - 变量 a 和 b 都不为 true")

    # 修改变量 a 的值
    a = 0
    if (a and b):
        print("3 - 变量 a 和 b 都为 true")
    else:
        print("3 - 变量 a 和 b 有一个不为 true")

    if (a or b):
        print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("4 - 变量 a 和 b 都不为 true")

    if not (a and b):
        print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        print("5 - 变量 a 和 b 都为 true")



    #Python成员运算符
    print("******************************************************************")
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    if (a in list):
        print("1 - 变量 a 在给定的列表中 list 中")
    else:
        print("1 - 变量 a 不在给定的列表中 list 中")

    if (b not in list):
        print("2 - 变量 b 不在给定的列表中 list 中")
    else:
        print("2 - 变量 b 在给定的列表中 list 中")

    # 修改变量 a 的值
    a = 2
    if (a in list):
        print("3 - 变量 a 在给定的列表中 list 中")
    else:
        print("3 - 变量 a 不在给定的列表中 list 中")


    #Python身份运算符
    print("******************************************************************")
    a = 20
    b = 20

    if (a is b):
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")

    if (id(a) == id(b)):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30
    if (a is b):
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")

    if (a is not b):
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")


    #访问字典里的值
    print("----------------------------------------------------------------")
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    var1 = 100
    if var1:
        print("1 - if 表达式条件为 true")
        print(var1)
    var2 = 0
    if var2:
        print("2 - if 表达式条件为 true")
        print(var2)
    print("Good bye!")

    #循环
    print("*******************************************************")
    a = 1
    while a < 10:
        print(a)
        a += 2

    #for循环
    print("*******************************************************")
    languages = ["C", "C++", "Perl", "Python"]
    for x in  languages:
        print(x)

    for i in range(10):
        print(i)

    #迭代器
    print("迭代器:*******************************************************")
    list = [1,2,3,4,5,6]
    it = iter(list)
    print(next(it))
    print(next(it))

    it = iter(list)  # 创建迭代器对象
    for x in it:
        print(x, end=" ")

    print("迭代器:*******************************************************")
    hello('study python')

    #生成器
    print("生成器:*******************************************************")
    f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

    # 调用printinfo 函数
    printinfo(1, a=2, b=3)

    # while True:
    #     try:
    #         print(next(f), end=" ")
    #     except StopIteration:
    #         sys.exit()


    # 类定义
    class people:
        # 定义基本属性
        name = ''
        age = 0
        # 定义私有属性,私有属性在类外部无法直接进行访问
        __weight = 0

        # 定义构造方法
        def __init__(self, n, a, w):
            self.name = n
            self.age = a
            self.__weight = w

        def speak(self):
            print("%s 说: 我 %d 岁。" % (self.name, self.age))


    # 单继承示例
    class student(people):
        grade = ''

        def __init__(self, n, a, w, g):
            # 调用父类的构函
            people.__init__(self, n, a, w)
            self.grade = g

        # 覆写父类的方法
        def speak(self):
            print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


    s = student('ken', 10, 60, 3)
    s.speak()


    class Solution(object):
        def twoSum(self, nums, target):
            l = len(nums)
            print(nums)
            ans = []
            for i in range(l - 1):
                for j in range(i + 1, l):
                    if nums[i] + nums[j] == target:
                        ans.append(i)
                        ans.append(j)
                        print([i, j])
                        break
            return ans


    print("Content-type:text/html")
    print()  # 空行，告诉服务器结束头部
    print('<html>')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<title>Hello Word - 我的第一个 CGI 程序！</title>')
    print('</head>')
    print('<body>')
    print('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
    print('</body>')
    print('</html>')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
