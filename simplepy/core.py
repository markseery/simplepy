

import inspect
import configparser
from datetime import datetime

class Core:
    className = ""
    configuration = {}
    myClass = ''
    logInfo = 'info'
    logWarn = 'warn'

    def __init__(self):
        self.setConfigDefaults()
        self.log(self.logInfo, 'Initializing: ' + str(__class__), self.myClass)
        self.readConfig()
        self.myClass = str(__class__)
        #self.log(self.logInfo,'Initializing: ' + str(__class__),self.myClass)
        #self.log(self.logInfo,'simplepy parameters: ' + str(self.configuration), self.myClass)
        #print("simplepy parameters: " , self.configuration)

    def setConfigDefaults(self):
        self.configuration['infologging']='no'

    def readConfig(self):
        config = configparser.ConfigParser()
        rc = config.read('./simplepy/simplepy.ini')
        if len(rc) == 0:
            print("Config file read not successful. Terminating progrgam")
            exit(-1)
        self.configuration = config._sections['PARAMETERS']

    def log(self,type,logMessage,className):
        if (type.upper()=='INFO') and (self.configuration['infologging'].upper()=="YES"):
            print(type," - ",datetime.now()," Log Message (",className,") :")
            print("  ", logMessage)

    def getName(self, className):
        # Use stack to get the name of classes, functions, etc.
        #   The right stack position depends on where is being called
        #   So a little fragile
        classFileName = inspect.stack()[1][1]
        lineNumber = inspect.stack()[1][2]
        functionName = inspect.stack()[1][3]
        caller = "Line: " + str(lineNumber) + " , " + className + "." + functionName + " , file: " + classFileName
        return caller

    def checkImport(self,importName,caller):
        try:
            __import__(importName)
            return(0)
        except Exception as e:
            print("Import check failed   :\n\t",caller)
            print("\t Error message    : ", e.args)
            print("\t Action recommend : ", importName , "can be installed")
            exit(-1)