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

#import subprocess
#test = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
#test = subprocess.Popen(["ping", "-W", "2", "-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
#output = test.communicate()[0]
#print(output)

import simplepy
import json

class Convert:
    className = ""
    myClass = ''


    def __init__(self):
        self.myClass = str(__class__)
        simplepy.simplepy.Simplepy().log("Info",'Initializing: ' + str(__class__),self.myClass)

    def printRequirements(self):
        print("Pandas")

    def jsonToDict(self,fileName,key=""): 
        file = open(fileName)
        jsonDict = json.load(file)

        print("Key: ", key)

        if key != "":
            print(jsonDict[key])
            return jsonDict[key]
        else:
            print(jsonDict)
            return jsonDict

    def csvToExcel(self,inName: str, outName: str):
        print('csv to excel: ', inName, " , " , outName)
        pass

    def dataFrameToExcel(self,inName: str, outName: str):
        pass

    def dataFrameToCSV(self,inName: str, outName: str):
        pass

    def getName(self):
        import inspect

        classFileName = inspect.stack()[1][1]
        lineNumber = inspect.stack()[1][2]
        functionName = inspect.stack()[1][3]
        caller = "Line: " + str(lineNumber) + " , " + str(__class__) + "." + functionName + " , file: " + classFileName
        return caller

    def excelToDataframe(self,inName: str, outName: str):
        #print("Core: " , self.util.getName(str(__class__)))
        df = None
        if (self.util.checkImport("Pandas",self.util.getName(str(__class__)))) != 0: exit(-1)

        try:
            df = pd.read_excel(inName)
        except Exception as e:
            print("Pandas read excel file failed for : ", inName, " , Error: "+ e.args)
        return df

    def printError(self,callName,importName):
        print(str(__class__),": ",callName," falied because ",importName," could not be imported and may not be imstalled")
