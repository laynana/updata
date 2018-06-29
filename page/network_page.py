#封装 更多子模块 下的 2G和 3G的点击和输入动作方法
from selenium.webdriver.common.by import By
from base.base_action import BaseDriver

#新建一个类，并继承base_action的方法
class Network_page(BaseDriver):
    # 把找到的元素抽取出来 用一个变量接收  方便调用
    more_button = By.XPATH,"//*[contains(@text,'更多')]"
    mobile_button = By.XPATH,"//*[contains(@text,'移动网络')]"
    first_button = By.XPATH,"//*[contains(@text,'首选网络类型')]"
    first_2G_button = By.XPATH,"//*[contains(@text,'2G')]"
    first_3G_button = By.XPATH,"//*[contains(@text,'3G')]"

    # 可以不用 声明 因为继承了BaseDriver的方法
    # def __init__(self, driver):
    #     self.driver = driver


    #封装找到更多 并点击
    def clicl_more(self):
        self.click(self.more_button)

    #封装找到移动网络 并点击
    def click_mobile(self):
        self.click(self.mobile_button)

    #封装 找到首选网络类型 并点击
    def click_first(self):
        self.click(self.first_button)

    #封装 找到2G 并点击
    def click_2G(self):
        self.click(self.first_2G_button)

    #封装 找到3G 并点击
    def click_3G(self):
        self.click(self.first_3G_button)






# 第二次更改过的
        # 封装找到更多 并点击
        # def clicl_more(self):
        #     self.driver.find_element(self.clicl_more()).click()
        #
        # # 封装找到移动网络 并点击
        # def click_mobile(self):
        #     self.driver.find_element(self.click_mobile()).click()
        #
        # # 封装 找到首选网络类型 并点击
        # def click_first(self):
        #     self.driver.find_element(self.click_first()).click()
        #
        # # 封装 找到2G 并点击
        # def click_2G(self):
        #     self.driver.find_element(self.first_2G_button).click()
        #
        # # 封装 找到3G 并点击
        # def click_3G(self):
        #     self.driver.find_element_by_xpath(self.first_3G_button).click()
        #
        #     # 二次封装 find_element 自定一个方法 给上面调用
        #     # 返回一个元组 因为element二次封装的方法传参必须是要一个元组，
        #     # 可以通过下标来指定两个参数     feature的意思是特征
        #
        # def find_element(self, feature):
        #     return self.driver.find_element(feature[0], feature[1])