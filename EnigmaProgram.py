import argparse

import src.Encryption.encryption.Enigma as En


def main():


    parser = argparse.ArgumentParser(description='Программма для шифрации Энигмой по ключу')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-k', '--key', type=str, help='Ключ для текста(случайный набор символов)')
    group.add_argument('-pk', '--pathKey', type=str, help='Путь к файлу для текста')

    parser.add_argument('-x', '--fileToText', type=str, help='Путь к файлу текста')
    parser.add_argument('-o', '--fileForExport', type=str, help='Название файла вывода(перезапишет существующий)')
    parser.add_argument('--translate', type=bool, default=False, help='Шифровать текст')
    parser.add_argument('-e', '--exportKeyTxt', type=str, help="Экспорт ключа в файл")

    args = parser.parse_args()

    with open(args.fileToText, 'r') as f:
        text = f.read()

    if args.key:
        key = args.key
    elif args.pathKey:
        with open(args.pathKey, 'r') as f:
            key = f.read()
    
    en = En.Enigma.createEnigmaIntoKey(key=key)

    if args.translate:
        cihep = en.translateUpdateRotors(text)
    else:
        cihep = en.encryptUpdateRotors(text)

    if args.exportKeyTxt:
        with open(args.exportKeyTxt, 'w') as file:
            file.write(args.exportKeyTxt)

    with open(args.fileForExport, 'w') as file:
        file.write(cihep)


if __name__ == "__main__":
    main()

