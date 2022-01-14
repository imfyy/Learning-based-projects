import requests
from lxml import etree
import re


#获取全球报价信息
def offer():
    off_sku = input('请输入要查询的sku')
    off_sku = 'https://stockx.com/api/products/' + off_sku + '/activity?limit=100&page=1&sort=createdAt&order=DESC&state=400&currency=USD&country=US'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    com_link = requests.get(url=off_sku, headers=headers).text
    ex = re.compile(r'.*?"amount":(?P<amount>.*?),.*?"shoeSize":(?P<shoeSize>.*?),')
    result = ex.finditer(com_link)
    for item in result:
        dic = item.groupdict()
        print(dic)

#获取输入的链接的商品信息
def extract_sku():
    input_com_link = input('请输入想获取的链接url:')

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    com_link = requests.get(url=input_com_link,headers=headers)
    sku_find = etree.HTML(com_link.text)

    #查询商品名字，货号，发售日期，以及商品的sku
    sku_name = sku_find.xpath('//*[@id="main-content"]/div/section[1]/div[2]/div[1]/h1/text()')
    article_num = sku_find.xpath('//*[@id="main-content"]/div/section[3]/div/div/div[1]/p/text()')
    sale_date = sku_find.xpath('//*[@id="main-content"]/div/section[3]/div/div/div[4]/p/text()')
    sku = str(sku_find.xpath('//*[@id="main-content"]/div/script[1]/text()'))
    ex = re.compile(r'{"@context":".*?"sku":"(.*?)"')
    result_sku = ex.findall(sku)

    print(f'商品名为：{sku_name},货号为：{article_num},发售日期为：{sale_date},sku为：{result_sku}')


#显示商品的交易记录
def sales():
    url = input('请输入sku值')
    url = 'https://stockx.com/api/products/' + url + '/activity?limit=100&page=1&sort=createdAt&order=DESC&state=480&currency=USD&country=US'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    res = requests.get(url,headers=headers).text
    ex = re.compile(r'.*?"amount":(?P<amount>.*?),.*?"createdAt":(?P<date>.*?),"shoeSize":(?P<shoeSize>.*?),')
    result = ex.finditer(res)
    for item in result:
        dic = item.groupdict()
        print(dic)

#主窗口，做了个循环因为要执行很多次
if __name__ == '__main__':
    while True:
        print('-------------------')
        print('请输入数字获取相应内容')
        print('-------------------')
        print('1、输入链接获取对应商品sku')
        print('2、查看sku对应的销售记录')
        print('3、查看sku对应的报价记录')
        print('4、结束程序')
        print('-------------------')
        num = int(input('请输入数字'))
        if num == 1:
            extract_sku()
        elif num == 2:
            sales()
        elif num == 3:
            offer()
        elif num == 4:
            break

