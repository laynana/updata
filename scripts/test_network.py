#测试脚本 更多子功能 下的 2g 和 3g
#导入base模块
from base.base_driver import int_driver
# from page.network_page import Network
from page.page import Page


class Test_network():
    def setup(self):
        # 实例 int_driver
        self.driver = int_driver()
        #实例化一个page   这个一个大的入口
        self.page = Page(self.driver)

        # 2G的功能
    def test_network_2g(self):

        self.page.network.clicl_more()
        self.page.network.click_mobile()
        self.page.network.click_first()
        self.page.network.click_2G()

        # 3G的功能

    def test_network_3g(self):
        self.page.network.clicl_more()
        self.page.network.click_mobile()
        self.page.network.click_first()
        self.page.network.click_3G()
        # 关闭 功能

    def teardown(self):
        self.driver.quit()





#没有添加一个page大的入口时候的代码
# class Test_network():
#     def setup(self):
#         #实例 int_driver
#         self.driver = int_driver()
#
#         #实例化Net_work 之后要传一个driver的参数
#         # self.network_page = Network(self.driver)
#
#         #2G的功能
#     def test_network_2g(self):
#
#         self.network_page.clicl_more()
#         self.network_page.click_mobile()
#         self.network_page.click_first()
#         self.network_page.click_2G()
#
#         #3G的功能
#     def test_network_3g(self):
#         self.network_page.clicl_more()
#         self.network_page.click_mobile()
#         self.network_page.click_first()
#         self.network_page.click_3G()
#         #关闭 功能
#     def teardown(self):
#         self.driver.quit()