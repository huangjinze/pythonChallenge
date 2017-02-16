
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

# 注意里面的单词EXACTLY，也就是说刚好是3个大写字母而不是4个大写字母，
# 因此为了确保，旁边三个大写字母两边必须分别是一个小写字母！
# 所以答案就很明显了，该单词的字母存在于由9个字母组成的字符串中，
# 排列形式是xXXXxXXXx。也就是说从网页源码的一大堆杂乱的字符串中
# 找出符合xXXXxXXXx这样排列的子字符串就可以得出需要的小写字母，
# 然后将那些满足条件的小写字母连接好就是通往答案的单词。

import string
import re
from functools import reduce

def my_solution1():
    text = open('mess').read()
    value = ''.join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text))
    print(value)

def string_module():
    s = open('mess').read()
    lwr = string.ascii_lowercase
    upr = string.ascii_uppercase

    for n in range(1, len(s)-7):
        if (s[n - 1] in lwr) and (s[n] in upr) and (s[n + 1] in upr) \
                and (s[n + 2] in upr) and (s[n + 3] in lwr) \
                and (s[n + 4] in upr) and (s[n + 5] in upr) \
                and (s[n + 6] in upr) and (s[n + 7] in lwr):
            print(s[n + 3])
# reduce(function, sequence[,initial])函数中有两个参数和一个可选参数；
# function参数是一个函数，sequence参数是一个序列，
# 使用reduce函数可以给函数function提供参数进行累加，参数来源于序列sequence的元素；
# 比如：reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])就是计算((((1+2)+3)+4)+5)；
# 也就是function的结果和`sequence中下一个序列元素作为function的参数；
# initial参数如果被给出，那么它将作为初始化结果，缺省情况下是空的。

# 作者声明了一个元组来存储相关信息，
# 1、chars_found：存储之前所有的符合条件的小写字母
# 2、state_lower：存储找到的满足XXXxXXX条件的小写字母
# 3、upper_count: 记录大写字母的数量
# coding:utf-8

def myfunction(state, c):
    if not c.isalpha():
        return state

    if state:
        chars_found, state_lower, count = state
    else:
        chars_found = ''
        state_lower = ''
        count = 0

    if c.islower():
        if count == 3:
            if state_lower:
                chars_found += state_lower

            state_lower = c
        else:
            state_lower = ''

        count = 0

    else:
        count += 1

    return chars_found , state_lower, count


if __name__ == '__main__':
    # my_solution1()
    # string_module()


    with open('mess') as f:
        s = f.read()
    print('start')
    record = open("record", 'w+')
    print(reduce(myfunction, s, ()))
