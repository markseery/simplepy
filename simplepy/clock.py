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
import datetime

class Clock:

    def __init__(self):
        pass

    def nowDateTime(self): return datetime.datetime.now()
    def nowYear(self): return self.nowDateTime().year
    def nowMonth(self): return self.nowDateTime().month
    def nowDay(self): return self.nowDateTime().day
    def nowHour(self): return self.nowDateTime().hour
    def nowMinute(self): return self.nowDateTime().minute
    def nowSecond(self): return self.nowDateTime().second
    def nowMicroSecond(self): return self.nowDateTime().microsecond

    def isBetween(self,start,end,test):
        if (test > start) and (test < end): return True
        else: return False