class Word:
    def __init__(self, english : list[str], french : str):
        self.__english = english
        self.__french = french

    def getFrench(self):    return self.__french    
    def getEnglish(self):	return self.__english