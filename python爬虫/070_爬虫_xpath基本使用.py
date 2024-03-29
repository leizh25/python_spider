# _*_ coding : utf-8 _*_
# @Time : 2024/2/8 21:03
# Author : LeiZhuzheng
# @File : 070_爬虫_lxml基本使用
# @Project : python爬虫

from lxml import etree

# xpath 解析

# (1) 本地文件                                                  etree.parse()
# (2) 服务器响应的数据  response.read().decode("utf-8")  ✅      etree.HTML()


# xpath解析本地文件
tree = etree.parse("070_爬虫_xpath的基本使用.html")

# tree.xpath("xpath路径")
# li_list = tree.xpath("//body//li")

# 查找所有有id的属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath("//ul/li[@id]/text()")


# 找到ID为l1的li标签   注意引号的问题
# li_list = tree.xpath("//ul/li[@id='l1']/text()")

# 查找id为l1的li标签的class的属性值
# li_list = tree.xpath("//ul/li[@id='l1']/@class")

# 查找id中包含字母l的li标签
# li_list = tree.xpath("//ul/li[contains(@id,'l')]/text()")

# 查找id值以l开头的li标签
# li_list = tree.xpath("//ul/li[starts-with(@id,'c')]/text()")

# 查找ID为li和class为c1的数据
# li_list = tree.xpath("//ul/li[@id='l1' and @class='c1']/text()")

li_list = tree.xpath("//ul/li[@id='l1']/text() | //ul/li[@id='l2']/text()")

# 判断列表的长度
print(li_list)
print(len(li_list))
