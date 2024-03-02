from typing import List
from .Roter import Roter

class Enigma:
    

    @staticmethod
    def rotorsAreTuned(roters: List[Roter]) -> None:
        if len(roters) < 1:
            raise Exception("Don't have roters? Добавь роторы б")
        
        standartAlphabetSize = len(roters[0].alphabet)
        
        if standartAlphabetSize < 2:
            raise Exception("Это не алфавиты, д. Измени размер алфавита для ротеров их размер <2")

        listRaise = []

        for roter in roters:

            listRaise = len(roter.alphabet)
            if len(roter.alphabet) != standartAlphabetSize:
                raise Exception(f"Настрой правильно ротеры, сейчас размеры: {listRaise}")
            
        for indexRoter in range(len(roters) - 1):

            if roters[indexRoter].startPositionRoter != roters[indexRoter + 1].alphabet:
                raise Exception(f"Конечный путь ротера {indexRoter + 1} не совпадает с приездом ротера {indexRoter + 2}. Измени startPosition первого ротера или alphabet второго ротера")
            
        
            
    
    def __init__(self, roters: List[Roter]):
        
        Enigma.rotorsAreTuned(roters)
                   
        self._roters = roters

        return
    
    def putRotorsInStartPosition(self) -> None:
        
        for rotor in self._roters:
            rotor.putStartPosition()

    @staticmethod
    def encrypt(text: str, roters: List[Roter], step: int = 1) -> str:

        Enigma.rotorsAreTuned(roters)

        if not set(text).issubset(set(roters[0].alphabet)):
            raise Exception("Символы текста не находятся в ротере. Давай другой текст д")
        
        cihep = ""

        for c in text:

            tmpCharacter = c
            spinNextRotor = True

            for indexRotor in range(len(roters)):
                
                if spinNextRotor:
                    if roters[indexRotor].step == len(roters[indexRotor].alphabet) - 1 and step > 0:
                        spinNextRotor = True
                    elif roters[indexRotor].step == 1 and step < 0:
                        spinNextRotor = True
                    else:
                        spinNextRotor = False

                    tmpCharacter = roters[indexRotor].encrypt(tmpCharacter, step)
                else:
                    tmpCharacter = roters[indexRotor].encryptWithoutStep(tmpCharacter)
            
            cihep += tmpCharacter
        
        return cihep

    @staticmethod
    def translate(text: str, rotersEncryptAndStartPosition: List[Roter], stepForEncryptAndStartPosition: int = 1) -> list:

        Enigma.rotorsAreTuned(rotersEncryptAndStartPosition)

        reversedRotors = []

        for rotor in rotersEncryptAndStartPosition[::-1]:
            reversedRotors.append(rotor.reverseRoterSafeStep())

        return Enigma.encrypt(text, reversedRotors, -stepForEncryptAndStartPosition)



