import  unittest
from  time import  sleep
from selenium import  webdriver
class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Chrome()
        self.dr.get('https://www.baidu.com')

    def tearDown(self):
        self.dr.quit()

    def test_search_a(self):
        dr=self.dr
        dr.find_element_by_id("kw").send_keys("selenium")
        dr.find_element_by_id("su").click()
        sleep(1)


if __name__=='__main__':
    unittest.main()

