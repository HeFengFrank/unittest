import  unittest
import test_baidu
test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__=='__main__':
    print("hello everbody")
    runner=unittest.TextTestRunner()
    runner.run(discover)