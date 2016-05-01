#coding=utf-8
from selenium import webdriver
import sys
import time

class DelSina:
    def __init__(self,url):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.get(url)

    def login(self,name,pwd):
        time.sleep(3)
        loginBtn = self.browser.find_element_by_xpath("//a[@node-type='loginBtn']")
        loginBtn.click()
        time.sleep(3)
        loginTab = self.browser.find_element_by_xpath("//a[@node-type='login_tab']")
        loginTab.click()
        time.sleep(3)
        nameInput = self.browser.find_element_by_xpath("//input[@node-type='username']")
        pwdInput = self.browser.find_element_by_xpath("//input[@node-type='password']")
        nameInput.send_keys(name)
        pwdInput.send_keys(pwd)
        time.sleep(3)
        submit = self.browser.find_element_by_xpath("//a[@node-type='submitBtn']")
        submit.click()

    def findBoxes(self):
        time.sleep(6)
        boxes = self.browser.find_elements_by_class_name("screen_box")
        return boxes

    def delWB(self,boxes):
        time.sleep(6)
        for box in boxes:
            time.sleep(2)
            menu = box.find_element_by_tag_name("a")
            menu.click()
            time.sleep(2)
            item = box.find_element_by_xpath("//a[@title='删除此条微博']")
            item.click()
            time.sleep(2)
            ok = box.find_element_by_xpath("//a[@node-type='ok']")
            ok.click()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    b = DelSina('http://weibo.com/u/2180821995?refer_flag=1001030102_&is_all=1')
    b.login('18761533592','z187159')
    boxes = b.findBoxes()
    print boxes
    while boxes != None:
        b.delWB(boxes)
        boxes = b.findBoxes()