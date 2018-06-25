# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 随机请求头 载中间件
from faker import Faker
class JdPhoneDownloadmiddlewareRandomUseragent(object):
    def __init__(self):
        self.fake = Faker()

    def process_request(self,request,spider):
        # print(self.fake.user_agent())
        request.headers.setdefault('User-Agent',self.fake.user_agent())

# 对接selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
import time

class JdphoneDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        super().__init__()  # 调用超类的构造函数
        self.timeout = 20
        options = webdriver.ChromeOptions()
        # 设置中文
        # options.add_argument('lang=zh_CN.UTF-8')
        # 设置无图加载，提高速度
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        # 设置无头浏览器
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.wait = WebDriverWait(self.browser,self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        page = request.meta.get('page',1)
        try:
            self.browser.get(request.url)
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') #下拉到页面底部
            time.sleep(2)  # 等待所有元素加载完成
            if page > 1:
                input = self.wait.until(EC.presence_of_element_located((By.XPATH,'.//span[@class="p-skip"]/input'))) # 获取输入页面数框
                submit = self.wait.until(EC.element_to_be_clickable((By.XPATH,'.//span[@class="p-skip"]/a')))  # 获取确定按钮
                input.clear()
                input.send_keys(page)
                submit.click()
                self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)
            # 如果当 str(page),即当前页码出现在高亮文本的时候，就代表页面成功跳转
            self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH,'.//span[@class="p-num"]/a[@class="curr"]'),str(page)))
            # 等待加载完所有的商品list 然后进一步解析
            self.wait.until(EC.presence_of_element_located((By.XPATH,'.//ul[@class="gl-warp clearfix"]/li')))
            return HtmlResponse(url=request.url,body=self.browser.page_source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url,status=500,request=request)


