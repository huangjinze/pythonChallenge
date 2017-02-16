import urllib
from urllib import parse
from urllib import request
import re
data = {}
number = '82304'

def first_version():
    for i in range(400):
        print(number)

        data['nothing'] = number

        url_value = urllib.parse.urlencode(data)
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
        full_url = url + '?' + url_value

        foo = urllib.request.urlopen(full_url)
        data1 = foo.read().decode('utf-8')

        value = data1.split(" ")
        number = [k for k in value if k.isdigit()][0]
        # for k in value :
        #     if k.isdigit():
        #         number = k

def second_version(number):
    while True:
        data['nothing'] = number

        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
        url_value = urllib.parse.urlencode(data)
        new_url = url+'?'+url_value
        foo = urllib.request.urlopen(new_url)

        page_data = foo.read().decode("utf-8")

        search = re.compile(" (\d*)$")
        match = search.findall(page_data)

        if match:
            number = match[0]
        else:
            search_html = re.compile("\.html$")
            if search_html.findall(new_url):
                break
            else:
                number = int(number)
                number /= 2

        print(number)
            #判断page_data里面有没有数字，
            # 有数字，number为新数字，
            # 无数字，则判断是不是以html结尾的，
                # 是：结束
                # 否：前一个数字/2
if __name__ == '__main__':
    second_version(number)

