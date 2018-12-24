'''
unittest是python内置的单元测试框架，具备编写用例、组织用例、执行用例、输出报告等自动化框架的条件。
使用unittest前需要了解该框架的五个概念:
即test case,test suite,testLoader，test runner,test fixture。
test case  ：一个完整的测试单元，执行该测试单元可以完成对某一个问题的验证，完整体现在：
               测试前环境准备(setUp)，执行测试代码(run)，以及测试后环境还原(tearDown)；
test suite  ：多个测试用例的集合，测试套件或测试计划；
testLoader  ：加载TestCase到TestSuite中的，其中loadTestsFrom__()方法用于寻找TestCase，
               并创建它们的实例，然后添加到TestSuite中，返回TestSuite实例；
test runner ：执行测试用例，并将测试结果保存到TextTestResult实例中，包括运行了多少测试用例，
               成功了多少，失败了多少等信息；
test fixture：一个测试用例的初始化准备及环境还原，主要是setUp() 和 setDown()方法

通过unittest类调用分析，可将框架的工作流程概况如下：
编写TestCase，由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，
最后将运行的结果保存在TextTestResult中。
参考文章：
http://blog.51cto.com/2681882/2123613


unittest提供了一些跳过指定用例的方法
@unittest.skip(reason)：强制跳转。reason是跳转原因
@unittest.skipIf(condition, reason)：condition为True的时候跳转
@unittest.skipUnless(condition, reason)：condition为False的时候跳转
@unittest.expectedFailure：如果test失败了，这个test不计入失败的case数目
https://www.cnblogs.com/eastonliu/p/9145231.html

'''


import unittest
import time
from pyunit.HTMLTestRunner import HTMLTestRunner   # 导入第三方HTMLTestRunner模块
from pyunit.myfun import add, minus, multi

'''
unittest的setup、teardown会在每个用例执行前后执行一次。
而对于多个用例只需执行一次setup，全部用例执行完成后，执行一次teardown，
针对该种场景，unittest的处理方法是使用setupclass、teardownclass，注意@classmethod的使用
'''


class TestMyfun(unittest.TestCase):     # 定义的测试用例方法类需要继承unittest.TestCase

    @classmethod
    def setUpClass(cls):        # setUp(self)
        print('每个用例执行前会调用setUp方法准备环境')

    @classmethod
    def tearDownClass(cls):     # tearDown(self)
        print('每个用例执行后会调用tearDown方法进行环境清理')

# 测试用例方法是以test开头作为标识，用例的执行结果以assetxxx断言结果决定，如果断言返回为false，将抛出assetError异常
    def testMinus(self):
        self.assertEqual(5, minus(6, 1), '相减不等于期望值')
        self.assertEqual(1, minus(3, 2), '相减不等于期望值')
        print('testMinus is done.')
        time.sleep(1)

    # @unittest.skip("强制跳转，编写reason跳转原因，即测试用例不执行")
    # @unittest.skipIf(3>2, "condition表达式为True的时候跳转，即为True时测试用例不执行")
    @unittest.skipUnless(3<2, "condition为False的时候跳转，即为False时测试用例不执行")
    def testAdd(self):
        self.assertEqual(3, add(1, 2), '相加不等于期望值')
        self.assertEqual(4, add(1, 3), '相加不等于期望值')
        print('testAdd is done.')
        time.sleep(1)

    def testMulti(self):
        self.assertEqual(4, multi(2, 2), '相乘不等于期望值')
        try:
            self.assertEqual(7, multi(2, 3), '相乘不等于期望值')
        except Exception as e:
            print(e)
        print('testMulti is done.')
        time.sleep(1)


if __name__ == '__main__':

    tests = [TestMyfun("testMulti"), TestMyfun("testMinus"), TestMyfun("testAdd")]

    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner()  # 生成的报告格式为txt
    # filepath = './html_report.html'
    # ftp = open(filepath, 'wb')
    # runner = HTMLTestRunner(stream=ftp, title='testResult')
    runner.run(suite)

    # unittest.main()
