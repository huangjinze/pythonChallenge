'''choose the letter in mess.txt'''

import string

def my_solution():
    text = open('mess.txt', 'r').read()

    # 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

    # filter(function, sequence)：对sequence中的item依次执行function(item)，
    # 将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回
    s = filter(lambda x: x in string.ascii_letters, text)

    print(list(s))

def std_solution():
# 我们要从一大堆混乱的字符中找出出现次数最少的字符，
# 诀窍是考虑文本mess.txt中出现次数低于平均水平的字符，
# 我们唯一掌握的信息就是字符是非频繁的，
# 是与url类型兼容的（比如回车符号以及空格符就不再考虑范围内）

# 读取文本内容；
# 定义一个字典，里面存储每个字符以及对应出现的频数；
# 计算出字符平均稀有情况（所有字符数量/字符数量）；
# 循环输出稀有性低于平均水平的的字符。
    s = ''.join([line.rstrip() for line in open('mess.txt')])

    occ = {}

    for c in s:
        occ[c] = occ.get(c, 0) + 1
        avgOC = len(s) // len(occ)
    # python 中 // 是取整数的意思
    print(occ['$'])

    print(''.join([c for c in s if occ[c] < avgOC]))

def std_solution_repeat():
    # 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
    # [x * x for x in range(1, 11)]
    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    string = ''.join([line.rstrip() for line in open('mess.txt')])
    occ = {}

    for word in string:
        occ[word] = occ.get(word, 0) + 1
        avgOC = len(string) // len(occ[word])
        print(avgOC)

    print(''.join([c for c in occ if occ[c] < avgOC]))

if __name__ == '__main__':
    std_solution()