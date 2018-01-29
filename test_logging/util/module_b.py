import log

logger = log.init_log("./log/test", __name__)
logger.info("Hello module b")

class ClassB(object):
    def __init__(self):
        pass
    
    def method(self):
        print 'ClassB.method'
        return True
