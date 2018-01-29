# 1. 多个文件的 logger写入同一个 log文件
#   见 main.py  util.module_b.py 中都以 util/log.py 中的 init_log 方法初始化获取以__name__为名称的logger

# 2. 单元测试
#   所有单元测试用例需要放在根目录下的 test下
#   单元测试代码的文件名以 "test_"为后缀，以要测试的模块或者类名为前缀，e.g. module_b_test.py
#   运行在根目录下进行，e.g. python test/module_b_test.py

