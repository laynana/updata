#测试显示功能的脚本
from base.base_driver import int_driver
# from page.display_page import Dispaly
from page.page import Page


class Testdispaly:
    def setup(self):
        #实例化 int_driver 的对象
        self.driver = int_driver()

        #实例化一个page  这个一个大的入口
        self.page = Page(self.driver)

        #实例化 Dispaly_page 的对象  后要传一个driver的参数
        # self.dispaly = Dispaly_page(self.driver)

    #调用Dispaly_page的 点击和输入的动作
    def test_display_input(self):
        #显示
        self.page.display.click_dispaly()
        #搜索
        self.page.display.click_search()
        #输入
        self.page.display.send_keys_input("hello")
        #返回
        self.page.display.click_back()

    def teardown(self):
        self.driver.quit()