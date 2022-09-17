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

from simplepy.core import Core
from simplepy.networking import Networking

class Simplepy:
    logInfo = Core().logInfo
    logWarn = Core().logWarn

    #   Initialize class
    def __init__(self):
        pass

    # log calls
    def log(self,type,logMessage,className):
        Core().log(Core().logInfo, logMessage, '__main__')

    # networking calls
    def sendMail(self,sender,receivers,subject,text,html,user,password):
        Networking().sendMail(sender,receivers,subject,text,html,user,password)

