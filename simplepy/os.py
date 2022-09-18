##########################################################################
#
#   Copyright / License notice 2022
#   --------------------------------
#
#   Permission is hereby granted, free of charge,
#       to any person obtaining a copy of this software
#       and associated documentation files (the “Software”),
#       to deal in the Software without restriction, including
#       without limitation the rights to use, copy, modify, merge,
#       publish, distribute, sublicense, and/or sell copies of the Software,
#       and to permit persons to whom the Software is furnished to do so,
#       subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#       in all copies or substantial portions of the Software.
#
##########################################################################

import simplepy
from threading import Thread
import time

class OS:

    def __init__(self):
        pass

    def threadPool(self,func,arguments):
        num_threads = len(arguments)
        while True:
            for i in range(num_threads):
                worker = Thread(target=func, args=(arguments[i],))
                worker.setDaemon(True)
                worker.start()
                time.sleep(1)