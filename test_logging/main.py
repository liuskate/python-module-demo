#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import log
from util import module_b

if __name__ == "__main__":
    logger = log.init_log("./log/test", __name__)
    logger.info("Hello main")

    classb = module_b.ClassB()
    classb.method()
