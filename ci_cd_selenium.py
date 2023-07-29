from seleniumbase import BaseCase
import time
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.facebook.com/")
        self.type("//input[@name='email']","khanhngoc981856729@gmail.com")
        self.type("//input[@name='pass']","856729ngoc")
        time.sleep(200)
        