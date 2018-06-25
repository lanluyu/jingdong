jdPhone说明文档
==
介绍
 - 
jdPhone是一个基于Scrapy-Selenium的爬取京东手机搜索页面信息的爬虫，由于京东的限制，只爬取了100页手机的详情。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7/Selenium 3.11.0<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Faker(随机切换User-Agent)<br>

爬取结果
-
在京东网站上总共爬取了5890条有关手机商品的有效信息。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![手机详情截图](https://github.com/lanluyu/jingdong/blob/master/phone.PNG)
