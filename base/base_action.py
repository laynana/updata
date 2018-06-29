#二次封装点击和输入的方法  让display_page和 network_page 去掉用
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver():
    # 声明driver
    def __init__(self, driver):
        self.driver = driver


    # 根据某个特征去查找 并点击   自定义一个click和send_keys的二次封装方法 给上面调用
    def click(self, feature):
        self.find_element(feature).click()

    # 根据某个特征去查找 并输入
    def send_input(self, feature, text):
        self.find_element(feature).send_keys(text)

    #在find_element二次封装方法在添加webdriverwiat 防止手机在卡顿的时候找不到元素
    def find_element(self, feature):
        wait = WebDriverWait(self.driver, 5,1)
        return wait.until(lambda x :x.find_element(feature[0], feature[1]))


#给方法是在element的基础上添加了一个s 可以方便找多个元素的时候调用
    def find_elements(self, feature):
        wait = WebDriverWait(self.driver, 5,1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))





            # 二次封装find_element 自定义一个方法  给上面去调用
    # def find_element(self, feature):
    #     return self.driver.find_element(feature[0], feature[1])
