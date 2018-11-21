# import  sys
# sys.path.append("./module")
# import unittest
# from module.new_count import B
# b=B()
# print(b.add(4,5))
from module.count import count
import  unittest
class TestAdd(unittest.TestCase):
    def setUp(self):
        self.a = count()
    def test_add(self):
        result = self.a.add(3,5)
        self.assertEquals(result,6)

    def tearDown(self):
        print('end')

class TestSub(unittest.TestCase):
    def setUp(self):
        self.b = count()

    def test_sub(self):
        result=self.b.sub(7,3)
        self.assertEquals(result,4)

    def tearDown(self):
        print('end')

if __name__ == '__main__':
    # unittest.main()
    suit=unittest.TestSuite()
    suit.addTest(TestAdd("test_add"))
    suit.addTest(TestSub("test_sub"))
    runner= unittest.TextTestRunner()
    runner.run(suit)

