#封装点击和输入的动作方法
from selenium.webdriver.common.by import By
from base.base_action import BaseDriver

#新建一个类，并继承base_action的方法
class Dispaly_page(BaseDriver):
    #把找到的元素抽取出来 用一个变量接收  方便调用
    dispaly_button = By.XPATH,"//*[contains(@text,'显示')]"
    search_button = By.ID,"com.android.settings:id/search"
    send_keys_button = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    #可以不用 声明 因为继承了BaseDriver的方法
    # def __init__(self, driver):
    #     self.driver = driver

    #封装找到显示 并点击的动作click
    def click_dispaly(self):
        self.click(self.dispaly_button)
        # self.driver.find_element(self.dispaly_button).click()

    #封装找到搜索 并点击的动作click
    def click_search(self):
        self.click(self.search_button)
        # self.driver.find_element(self.search_button).click()

    #封装 找到输入框 并输入数据的动作  send_keys
    def send_keys_input(self,content):          #设置一个动态传参content
        self.send_input(self.send_keys_button, content)
        # self.driver.find_element(self.send_keys_button).send_keys(content)

    #封装 找到返回按钮 并点击返回的动作 click
    def click_back(self):
        self.click(self.back_button)
        # self.driver.find_element(self.back_button).click()


