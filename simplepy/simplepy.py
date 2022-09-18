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
#
#   Class Details
#   -------------
#
#       Name: Simplepy
#       Author: Mark Seery
#
#   Notes
#   -----
#
#   In general, Simplepy class does not do much work itself,
#       it calls other classes that do all the work.
#
#   The goal is to achieve a level of simplicity for the
#       programmer using Simplepy, by providin one class
#       to which all the calls are made, without having
#       to keep track of the classes actually doing the work
#
##########################################################################

import simplepy
from simplepy.os import OS
from simplepy.core import Core
from simplepy.networking import Networking
from simplepy.convert import Convert
from simplepy.clock import Clock

from functools import reduce

class Simplepy:
    logInfo = simplepy.core.Core().logInfo
    logWarn = simplepy.core.Core().logWarn
    

    # lambda functions
    add = lambda self, x, y: x + y
    increment = lambda self, x: x + 1
    sqr = lambda self, x: x * x
    isOdd = lambda self, x: (x % 2 != 0)
    isEven = lambda self, x: (x % 2 == 0)
    

    #isGreaterThan = lambda self,x,y: x > y

    #   Initialize class
    def __init__(self):
        pass

    # Simple filter routines
    def filterEvens(self,li): return list(filter(self.isEven, li))
    def filterOdds(self,li): return list(filter(self.isOdd, li))

    # Simple list routines
    def mapList(self,li): return map(lambda x, y: x*y, li)
    def reduceList(self,li): return reduce(lambda x, y: x*y, li)
    def printList(self,li): return list(map(lambda x:print(x),li))

    # os calls
    def threadPool(self,func,arguments): return OS().threadPool(func,arguments)

    # clock calls
    def isBetween(self,start,end,test): return Clock().isBetween(start,end,test)
    def nowHour(self): return Clock().nowHour()

    # log calls
    def log(self,type,logMessage,className): return Core().log(type, logMessage, '__main__')

    # networking calls
    def isUrlReachable(self,url): return Networking().isUrlReachable(url)

    def sendMail(self,service,sender,receivers,subject,text,html,user,password):
        return Networking().sendMail(service,sender,receivers,subject,text,html,user,password)

    # conversions
    def jsonToDict(self,fileName,key=""): return Convert().jsonToDict(fileName,key)


