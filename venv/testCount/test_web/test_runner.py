import  unittest
import test_baidu
test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__=='__main__':
    print("hello everbody")
    print("hello everbody2")
    runner=unittest.TextTestRunner()
    runner.run(discover)