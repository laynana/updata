#定义一个大的入口
#因为会有一些需求在页面中调用其他页面的动作，比如某些登录
#方便掉用其他页面的动作

from page.display_page import Dispaly_page
from page.network_page import Network_page


class Page():
    def __init__(self,driver):
        self.driver = driver

    #@property
    # 把一个方法当成一个属性来调用   方法内部也会执行
    # 在别的地方调用该方法的是时候可以不加括号
    @property
    def display(self):
        return Dispaly_page(self.driver)

    @property
    def network(self):
        return Network_page(self.driver)



    #当后面还有其他的界面模块的时候直接在这后面添加一个函数即可

