

# https://www.runoob.com/manual/pythontutorial3/docs/html/introduction.html
# 练习

# this is the first comment
spam = 1 # and this is the second comment
         # ... ad now a third!
text = "# This is not a comment because it's inside quotes."

print(spam)
print(text)

# 3.1 将Python当作计算器
print('========================================')
# 3.1.1 数字
print('----------------------------------------')
# (1) 除法/返回浮点数
a = 8 / 5
print(a, type(a))

b = 8 / 4
print(b, type(b))

# (2) 整数除法//和求余%
c = 8 // 5
d = 8 % 5
print(c, type(c))
print(d, type(d))

# (3) 向负无穷取整：单边
e = -8 // 5
f = -8 % 5
print(e, type(e))
print(f, type(f))

# (4) 幂
g = 5 ** 2
print(g, type(g)) # 类型为int

h = 4 ** 0.5
print(h, type(h))

# (5) 复数
i = 3+5j
print(i, type(i))

# 3.1.2 字符串
print('----------------------------------------')
# (1) 常用字符串
str_a = 'spam eggs'
str_b = 'doesn\'t'
str_c = '"Yes," he said.'
str_d = '"Isn\'t," she said.'

print(str_a, type(str_a))
print(str_b, type(str_b))
print(str_c, type(str_c))
print(str_d, type(str_d))

str_e = 'First line.\nSecond line.'
print(str_e, type(str_e))

# (2) 原始字符串
str_f = 'C:\some\name'
print(str_f, type(str_f))
# print(r(str_f), type(r(str_f))) # 错误
print(r'C:\some\name')

# (3) 多行
str_g = """\
Usage: thingy [OPTIONS]
    -h              Display this usage message
    -H hostname     Hostname to connect to
"""
print(str_g, type(str_g))

# (4) +连接；*重复；相邻自动连接
str_h = 3 * 'un' + 'ium' ' haha'
print(str_h, type(str_h))

# (5) 索引：获得单个字符
# +--------+---+---+---+---+---+---+
# | string | P | y | t | h | o | n |
# +--------+---+---+---+---+---+---+
# |        | 0 | 1 | 2 | 3 | 4 | 5 |
# + index  +---+---+---+---+---+---+
# |        |-0 |-5 |-4 |-3 |-2 |-1 |
# +--------+---+---+---+---+---+---+
str_i = 'Python'
print(str_i[0], type(str_i[0])) # str类型；一个字符就是长度为1的字符串
print(str_i[5], type(str_i[5]))
# print(str_i[6], type(str_i[6])) # 访问越界，错误
print(str_i[-1], type(str_i[-1])) # 从最右侧开始索引；当作循环链表来思考
print(str_i[-0], type(str_i[-0]))

# (6) 切片：获得子字符串，左闭右开区间;切片方向从左到右
print(str_i[:2], type(str_i[:2])) # [0,2)
print(str_i[:2]+str_i[2:], type(str_i[:2]+str_i[2:])) # [0,2) + [2,length) = [0,length)
print(str_i[4:], type(str_i[4:]))
print(str_i[-2:], type(str_i[-2:]))

print(str_i[4:42], type(str_i[4:42])) # 截断到尾部
print(str_i[42:], type(str_i[42:])) # 空串

# (7) 不可修改
str_j = 'J' + str_i[1:]
print(str_j, type(str_j))

# (8) 返回字符串长度
print(len(str_j), type(len(str_j)))
print(len(str_i[42:]), type(len(str_i[42:])))

# 3.1.3 列表
print('----------------------------------------')
# (1) 定义列表
lst_a = [1, 4, 9, 16, 25]
print(lst_a, type(lst_a), id(lst_a[:]))

# (2) 切片和索引：新的（浅）拷贝副本
print(lst_a[:], type(lst_a[:]), id(lst_a[:]))

# (3) 连接
lst_b = lst_a + [36, 49, 64, 81, 100]
print(lst_b, type(lst_b), id(lst_b[:]))

# (4) 可修改
lst_c = [1, 8, 27, 65, 125]
print(lst_c, type(lst_c), id(lst_c))
lst_c[3] = 4 ** 3
print(lst_c, type(lst_c), id(lst_c))
lst_c.append(6**3);
print(lst_c, type(lst_c), id(lst_c))

lst_d = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(lst_d, type(lst_d), id(lst_d))
print(lst_d[2:5], type(lst_d[2:5]), id(lst_d[2:5])) # 右值：切片会发生拷贝
lst_d[2:5] = [] # 左值：被修改，不发生拷贝
print(lst_d, type(lst_d), id(lst_d))
lst_d[:] = []
print(lst_d, type(lst_d), id(lst_d))
print(len(lst_d),type(len(lst_d)))

# (5) 嵌套
lst_e = ['a', 'b', 'c']
lst_f = [1, 2, 3]
lst_g = [lst_e, lst_f]
print(lst_e, type(lst_e), id(lst_e))
print(lst_f, type(lst_f), id(lst_f))
print(lst_g, type(lst_g), id(lst_g))
print(lst_g[0], type(lst_g[0]), id(lst_g[0])) # lst_g[0] == lst_e
print(lst_g[1], type(lst_g[1]), id(lst_g[1])) # lst_g[1] == lst_f
print(lst_g[1][1])

# 3.2 编程的第一步
print('========================================')

# (1) 生成Fibonacci数列
a, b = 0, 1
# while
# 任何非0整数都为true；0为false
# 条件可为字符串或列表，任意序列：长度不为零的为true，空序列为false
# Tab缩进；空行结束
while b < 10:
    print(b, end=',')
    a, b = b, a+b #, 多重赋值，右边表达式从左到右计算
print()

# 4 深入Python流程控制
print('========================================')
# 4.1 if
print('----------------------------------------')
if_x = int(input('Please enter an integer: '))
if if_x < 0:
    if_x = 0
    print('Negative changed to zero.')
elif if_x == 0:
    print('Zero')
elif if_x == 1:
    print('Single')
else:
    print('More')

# 4.2 for
print('----------------------------------------')
# (1) for用法
for_a = ['cat', 'window', 'defenestrate']
for w in for_a:
    print(w, len(w))

# (2) 循环条件中使用被修改序列的副本
for w in for_a[:]: # 使用拷贝进行循环
    if len(w) > 6:
        for_a.insert(0, w);
print(for_a)

# 4.3 range()函数
print('----------------------------------------')
for i in range(len(for_a)-1, 0, -2):
    print('list['+str(i)+'] = ', end='')
    print(for_a[i])
print(range(5), type(range(5))) # range类型，可迭代的对象

# 4.4 break, continue以及循环中的else子句
print('----------------------------------------')

# 搜索素数
prime = []
for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            print(n, 'equals', i, '*', n//i)
            break;
    else:
        prime.append(n)

print(prime)

# 4.5 pass语句
print('----------------------------------------')
# while True:
#     pass # 等待Ctrl-C中断

# 定义最小类
class MyEmptyClass:
    pass

print(MyEmptyClass, type(MyEmptyClass))

# 4.6 定义函数
print('----------------------------------------')


# 定义生成Fibonacci数列的函数
# 变量引用：局部符号表 > 包含函数的局部符号表 > 全局符号表

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while b <= n:
        print(b, end=' ')
        a, b = b, a+b
    print()


fib(13)

# 实参传值调用：值指的是对象的引用，而不是该对象的值
# 修改全局变量

fun_x = 100;
print(fun_x, type(fun_x), id(fun_x))


def myfun(x):
    """My test function."""
    print(x, type(x), id(x))
    x = 20
    print(x, type(x), id(x))
    global fun_x
    print(fun_x, type(fun_x), id(fun_x))
    fun_x = 200


myfun(10)
print(fun_x, type(fun_x), id(fun_x))


# 4.7 深入Python函数定义
print('----------------------------------------')

# 4.7.1 默认参数值


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


ok = ask_ok('Do you really want to quit?')
print(ok, type(ok))

ok = ask_ok('OK to overwrite the file?', 2)
print(ok, type(ok))

ok = ask_ok('Delete this file?', 2, 'Come on, only yes or no!')
print(ok, type(ok))

# 默认值在函数定义作用域被解析
i = 5
def f(arg=i):
    print(arg)

i = 6
f()

# 默认值在调用中可变


def f2(a, L=[]): # 此处L是一个对象引用，内容可以发生改变
    """参数L会在执行过程中被累积"""
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))


# 默认值不在后续调用中累积


def f3(a, L=None): # None是一个特殊的NoneType对象
    if L is None:
        L = []
    L.append(a)
    return L


print(f3(1))
print(f3(2))
print(f3(3))

# 4.7.2 关键词参数

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage. the", type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')


def cheeseshop(kind, *arguments, **keywords):
    """
    打印信息
    :param kind:
    :param arguments: 元组，包含所有没有出现在形式参数列表中的参数值
    :param keywords: 字典，包含所有未出现的关键字参数
    :return:
    """
    print("-- DO you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys()) # 若不排序，打印顺序未定义
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very. VERY runny. sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 4.7.3 可变参数列表


def write_multiple_items(file, separator, *args):
    """
    将多项内容写到文件
    :param file: 文件名
    :param separator: 分隔符
    :param args: 可变参数，写入的内容
    :return:
    """
    file.write(separator.join(args))


def concat(*args, sep='/'):
    return sep.join(args)


it_a = concat('earth', 'mars', 'venus')
print(it_a, type(it_a))

it_b = concat('earth', 'mars', 'venus', sep='.')
print(it_b, type(it_b))


# 4.7.4 参数列表的拆分
lst_x = list(range(3, 6))
print(lst_x, type(lst_x))

args = [3, 6]
lst_y = list(range(*args))
print(lst_y, type(lst_y))


# 4.7.5 Lambda形式：短小的匿名函数


def make_incrementor(n):
    """参考C中宏定义"""
    return lambda x: x + n # 返回一个函数，类型为class function


f = make_incrementor(42)
print(f, type(f))
ff = f(1)
print(ff, type(ff))


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) # 作为小函数传参
print(pairs, type(pairs))


# 4.7.6 文档字符串

def my_f():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    :return: None
    """
    pass


print(my_f.__doc__)

# 4.7.7 函数注解


def my_ff(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("Annotations:", my_ff.__annotations__)
    print("Arguments:", ham, eggs)


my_ff('wonderful')

# 5 数据结构
print('========================================')

