class Word:
    def __init__(self, english : list[str], french : str, manyDefinitions = False):
        self.__french = french
        self.__english = english
        self.multipleDefinitions = manyDefinitions

    def getFrench(self):    return self.__french    
    def getEnglish(self):	return self.__english