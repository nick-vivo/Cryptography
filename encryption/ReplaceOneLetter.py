
class ReplaceOneLetter:


    def __init__(self, originalDict: str, replaceDict: str):
        
        if len(originalDict) != len(replaceDict) or self.__checkDuplicatesInStr(originalDict) or self.__checkDuplicatesInStr(replaceDict):
            raise "fail"

        self._originalDict = dict(zip(originalDict, replaceDict))
        self._replaceDict = dict(zip(replaceDict, originalDict))
    
    def encrypt(self, string: str) -> str:

        if not self.__checkCharacters(string, self._originalDict):
            raise "fail"
        
        encryptik = ""

        for i in range(len(string)):
            encryptik += self._originalDict[string[i]]

        return encryptik

    def translate(self, string: str) -> str:

        if not self.__checkCharacters(string, self._replaceDict):
            raise "fail"
        
        encryptik = ""

        for i in range(len(string)):
            encryptik += self._replaceDict[string[i]]

        return encryptik

    def __checkDuplicatesInStr(self, strka: str) -> bool:
        
        return len(set(strka)) != len(strka)
    

    def __checkCharacters(self, forTranslate: str, dictionary: dict) -> bool:
        
        for i in forTranslate:
            
            if i not in dictionary.values():
                return False
            
        return True
        

        
