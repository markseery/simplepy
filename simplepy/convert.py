#import subprocess
#test = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
#test = subprocess.Popen(["ping", "-W", "2", "-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
#output = test.communicate()[0]
#print(output)

from simplepy.core import Core

class Convert:
    className = ""
    myClass = ''
    util = Core()

    def __init__(self):
        self.myClass = str(__class__)
        Core().log(Core.logInfo,'Initializing: ' + str(__class__),self.myClass)

    def printRequirements(self):
        print("Pandas")

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