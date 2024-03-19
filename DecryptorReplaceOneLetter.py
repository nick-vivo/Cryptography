import argparse

from src.Encryption.decryption.D_ReplaceOneLetter import D_ReplaceOneLetter as DCrypt

CONST_LETTERS_MAX_IN_ENCODE = 20

def generateCommand(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--alphabet', type=str, help='Alphabet for decryption')
    group.add_argument('-fta', '--fileForTxtAlphabet', type=str, help='Path to the file with alphabet for decryption .txt')

    parser.add_argument('-x', '--encodeFile', type=str, help='Path to the cipher file')
    parser.add_argument('-o', '--fileForExport', type=str, help='Output file name (will overwrite existing)')
    parser.add_argument('-dc', '--characterDelimetrInCihep', type=str, help='Character delimiter in the cipher')
    parser.add_argument('-e', '--exportKeyJson', type=str, help="Export key to file")

    return

def outBasicInfo(decryptor: DCrypt, text: str, alphabet: str, forWatch: dict, translate: str) -> None:
    print("\n-------------------------------------------------------------------------------")
    print("Frequency:\n")
    print(decryptor.analysisTextAndSortFrequency())

    print("-------------------------------------------------------------------------------")
    print("\n\nReplacements:")
    print()
    print(list(forWatch.keys()))
    print(list(forWatch.values()))
    print(forWatch)

    print("-------------------------------------------------------------------------------")
    print("\n\nText:")
    print(text)

    print("-------------------------------------------------------------------------------")
    print("\n\nDecryption:")
    print(translate)

    return

def outPlusInfo(parser: argparse.ArgumentParser, decryptor: DCrypt, translate: str, forWatch: dict):
    args = parser.parse_args()

    if args.characterDelimetrInCihep and len(args.characterDelimetrInCihep) == 1:
        print("-------------------------------------------------------------------------------")
        print("\nAnalysis: (number of characters, number of words, frequency of all words)")
        for i in range(1, CONST_LETTERS_MAX_IN_ENCODE):
            length = decryptor.countWordSizeInText([args.characterDelimetrInCihep], i)
            if length != 0:
                average = decryptor.wordSizeInTextFrequency([args.characterDelimetrInCihep], i)
                print(f"\n{i}, {length}, {average}")
                print(decryptor.splitTextBySize([args.characterDelimetrInCihep], i))
                print(DCrypt.splitTextBySize_s(translate, [forWatch[args.characterDelimetrInCihep]], i))

def main():
    parser = argparse.ArgumentParser(description='Program for decrypting with Enigma using a key')

    generateCommand(parser)

    args = parser.parse_args()

    if args.alphabet:
        goodAlphabet = args.alphabet
    elif args.fileForTxtAlphabet:
        with open(args.fileForTxtAlphabet, "r") as f:
            goodAlphabet = f.read()

    with open(args.encodeFile, 'r') as file:
        text = file.read()
    text = text.replace("\n", "")

    decryptor = DCrypt(text)

    forWatch = decryptor.getTranslateDictFrequency(goodAlphabet)
    translate = decryptor.decryptionSortFrequency(goodAlphabet)

    outBasicInfo(decryptor, text, goodAlphabet, forWatch, translate)

    outPlusInfo(parser, decryptor, translate, forWatch)

    if args.exportKeyJson:
        decryptor.export_KeyJSON(goodAlphabet, args.exportKeyJson)

    with open(args.fileForExport, 'w') as file:
        file.write(translate)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)