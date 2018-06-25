jdPhone说明文档
==
介绍
 - 
jdPhone是一个基于Scrapy-Selenium的爬取京东手机搜索页面信息的爬虫，由于京东的限制，只爬取了100页手机的详情。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Selenium 3.11.0
* Faker(随机切换User-Agent)<br>

### 其它
* 由于京东的防爬限制，这里采用了模拟浏览器的工具Selenium结合Scrapy框架爬取京东。Selenium采用了headless mode无头模式和无图片模式提升了爬取速度。但是在获取AJAX动态加载的页面信息和全部网页时，依然受限于电脑性能和网页响应速度，还是设置了等待页面渲染时间，以定位需要的页面元素。整个爬虫的爬取的速度不快，而且京东也限制了整个搜索页面最大100页，总共5890条信息，但相对于手机信息，应该也够用了。

爬取结果
-
在京东网站上总共爬取了5890条有关手机商品的有效信息。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![手机详情截图](https://github.com/lanluyu/jingdong/blob/master/phone.PNG)
