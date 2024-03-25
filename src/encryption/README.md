# для Энигмы:
## Перевод:
        python3 enigma_program.py -pk Solution1/key -x Solution1/cihep.txt -o Solution1/translate.txt --translate True -s Solution1/seed
## Шифрация:
        python3 enigma_program.py -pk key -x key -o passwd -sft seed

# для дешифратора:
## Для ананлиза слов:
        python3 decryptor_replace_one_letter.py -fta Solution2/alphabet_for_program -x Solution2/encode.txt -o Solution2/tranlsate.txt -dc ">" -e Solution2/key
## Без анализа слов:
        python3 decryptor_replace_one_letter.py -fta Solution2/alphabet_for_program -x Solution2/encode.txt -o Solution2/tranlsate.txt -e Solution2/key
## Без эспорта ключа:
        python3 decryptor_replace_one_letter.py -fta Solution2/alphabet_for_program -x Solution2/encode.txt -o Solution2/tranlsate.txt




# Какой вывод в консоль вы обязаны получить:
-------------------------------------------------------------------------------
Частота:

{'>': 0.12852664576802508, '2': 0.12539184952978055, 'a': 0.07993730407523511, 'А': 0.07366771159874608, '7': 0.06269592476489028, 'О': 0.05799373040752351, 'r': 0.054858934169279, '1': 0.054858934169279, 'Р': 0.047021943573667714, 'Ф': 0.03605015673981191, 'Е': 0.032915360501567396, 'Х': 0.02821316614420063, 'Д': 0.02664576802507837, '9': 0.025078369905956112, 'У': 0.023510971786833857, ' ': 0.02037617554858934, '3': 0.014106583072100314, 't': 0.012539184952978056, 'b': 0.012539184952978056, '<': 0.012539184952978056, '0': 0.0109717868338558, 'Я': 0.007836990595611285, 'Ы': 0.007836990595611285, '8': 0.007836990595611285, 'М': 0.006269592476489028, 'Й': 0.006269592476489028, 'Ь': 0.004702194357366771, 'Л': 0.004702194357366771, 'Б': 0.004702194357366771, 'c': 0.004702194357366771, 'К': 0.003134796238244514, 'И': 0.001567398119122257}
-------------------------------------------------------------------------------

Замены:

['>', '2', 'a', 'А', '7', 'О', 'r', '1', 'Р', 'Ф', 'Е', 'Х', 'Д', '9', 'У', ' ', '3', 't', 'b', '<', '0', 'Я', 'Ы', '8', 'М', 'Й', 'Ь', 'Л', 'Б', 'c', 'К', 'И']
['_', 'О', 'Е', 'Т', 'И', 'А', 'С', 'Н', 'В', 'Л', 'Р', 'М', 'П', 'Д', 'К', 'Я', 'Г', 'Ч', 'Ж', 'Ы', 'Б', 'Ю', 'Ь', 'Й', 'Ц', 'Щ', 'Э', 'Х', 'У', 'З', 'Ф', 'Ш']

{'>': '_', '2': 'О', 'a': 'Е', 'А': 'Т', '7': 'И', 'О': 'А', 'r': 'С', '1': 'Н', 'Р': 'В', 'Ф': 'Л', 'Е': 'Р', 'Х': 'М', 'Д': 'П', '9': 'Д', 'У': 'К', ' ': 'Я', '3': 'Г', 't': 'Ч', 'b': 'Ж', '<': 'Ы', '0': 'Б', 'Я': 'Ю', 'Ы': 'Ь', '8': 'Й', 'М': 'Ц', 'Й': 'Щ', 'Ь': 'Э', 'Л': 'Х', 'Б': 'У', 'c': 'З', 'К': 'Ф', 'И': 'Ш'}
-------------------------------------------------------------------------------


Расшифровка:

>Р>rОХ2Х>ДЕ2rА2Х>РОЕ7О1Аa>Х29aФ7Е2РО17aХ> РФ aАr>2Мa1УО>РaЕ2 А12rА7>Д2 РФa17 >УОb9232>r7ХР2ФО>АО0Ф7МО>РaЕ2А12rАa8>Д2 РФa17 >УОb9232>r7ХР2ФО>2r12РО11О>1О>Д29rtaАa>tОrА2А>7Л>РrАЕatОaХ2rА7>1Оc<РОaАr>Х29aФЫЯ>ДaЕР232>ДЕ70Ф7ba17 >7Ф7>aЙa>ДaЕР232>Д2Е9УО>АО0Ф7МО>Бt7А<РОЯЙО>02Фaa>rФ2b1<a>cОР7r7Х2rА7>1ОДЕ7ХaЕ>Д2РФa17a>291232>r7ХР2ФО>Д2rФa>УОУ232А2>9ЕБ3232>7ХaЯА>r22АРaАrАРa112>РА2Е28>7>02Фaa>Д2Е 92У>r>Д2Х2ЙЫЯ>ЬА7Л>РaЕ2А12rАa8>Х2baА>0<АЫ>Р<t7rФa1О>Ь1АЕ2Д7>7>Д2rАЕ2a1>92rАОА2t12>ЬККaУА7Р1<8>У29>Д2cР2ФЯЙ78>rbОАЫ>АaУrА>1О7ФБtИО >rЕa91>9Ф71О>У29О>7>r22АРaАrАРa112>rАaДa1Ы>rbОА7 >92rА73ОaАr >Х29aФХ7>Р>У2А2Е<Л>2Мa1У7>РaЕ2 А12rА7>УОУ>Х2b12>02Фaa>А2t1<

_В_САМОМ_ПРОСТОМ_ВАРИАНТЕ_МОДЕЛИРОВАНИЕМ_ЯВЛЯЕТС_ОЦЕНКА_ВЕРОЯТНОСТИ_ПОЯВЛЕНИЯ_КАЖДОГО_СИМВОЛА_ТАБЛИЦА_ВЕРОТНОСТЕЙ_ПОЯВЛЕНИЯ_КАЖДОГО_СИМВОЛА_ОСНОВАННА_НА_ПОДСЧЕТЕ_ЧАСТОТ_ИХ_ВСТРЕЧАЕМОСТИ_НАЗЫВАЕТС_МОДЕЛЬЮ_ПЕРВОГО_ПРИБЛИЖЕНИЯ_ИЛИ_ЕЩЕ_ПЕРВОГО_ПОРДКА_ТАБЛИЦА_УЧИТЫВАЮЩА_БОЛЕЕ_СЛОЖНЫЕ_ЗАВИСИМОСТИ_НАПРИМЕР_ПОВЛЕНИЕ_ОДНОГО_СИМВОЛА_ПОСЛЕ_КАКОГОТО_ДРУГОГО_ИМЕЮТ_СООТВЕТСТВЕННО_ВТОРОЙ_И_БОЛЕЕ_ПОРЯДОК_С_ПОМОЩЬЮ_ЭТИХ_ВЕРОТНОСТЕЙ_МОЖЕТ_БЫТЬ_ВЫЧИСЛЕНА_ЭНТРОПИ_И_ПОСТРОЕН_ДОСТАТОЧНО_ЭФФЕКТИВНЫЙ_КОД_ПОЗВОЛЮЩИЙ_СЖАТЬ_ТЕКСТ_НАИЛУЧШАЯ_СРЕДН_ДЛИНА_КОДА_И_СООТВЕТСТВЕННО_СТЕПЕНЬ_СЖАТИЯ_ДОСТИГАЕТСЯ_МОДЕЛМИ_В_КОТОРЫХ_ОЦЕНКИ_ВЕРОЯТНОСТИ_КАК_МОЖНО_БОЛЕЕ_ТОЧНЫ
-------------------------------------------------------------------------------

Анализ: (кол-во символов, кол-во слов, частота всех слов)

4, 1, 0.1111111111111111
['АЫ>Р']
['ТЬ_В']

17, 1, 0.1111111111111111
['РОЯЙО>02Фaa>rФ2b1']
['ВАЮЩА_БОЛЕЕ_СЛОЖН']
(venv) ni@vi:~/Projects/isb/lab_1$ python3 DecryptorReplaceOneLetter.py -fta alphabet_for_program.txt -x encode.txt -dc ">" -o translate.txt
-------------------------------------------------------------------------------


Частота:

{'>': 0.12852664576802508, '2': 0.12539184952978055, 'a': 0.07993730407523511, 'А': 0.07366771159874608, '7': 0.06269592476489028, 'О': 0.05799373040752351, 'r': 0.054858934169279, '1': 0.054858934169279, 'Р': 0.047021943573667714, 'Ф': 0.03605015673981191, 'Е': 0.032915360501567396, 'Х': 0.02821316614420063, 'Д': 0.02664576802507837, '9': 0.025078369905956112, 'У': 0.023510971786833857, ' ': 0.02037617554858934, '3': 0.014106583072100314, 't': 0.012539184952978056, 'b': 0.012539184952978056, '<': 0.012539184952978056, '0': 0.0109717868338558, 'Я': 0.007836990595611285, 'Ы': 0.007836990595611285, '8': 0.007836990595611285, 'М': 0.006269592476489028, 'Й': 0.006269592476489028, 'Ь': 0.004702194357366771, 'Л': 0.004702194357366771, 'Б': 0.004702194357366771, 'c': 0.004702194357366771, 'К': 0.003134796238244514, 'И': 0.001567398119122257}
-------------------------------------------------------------------------------

Замены:

['>', '2', 'a', 'А', '7', 'О', 'r', '1', 'Р', 'Ф', 'Е', 'Х', 'Д', '9', 'У', ' ', '3', 't', 'b', '<', '0', 'Я', 'Ы', '8', 'М', 'Й', 'Ь', 'Л', 'Б', 'c', 'К', 'И']
['_', 'О', 'Е', 'Т', 'И', 'А', 'С', 'Н', 'В', 'Л', 'Р', 'М', 'П', 'Д', 'К', 'Я', 'Г', 'Ч', 'Ж', 'Ы', 'Б', 'Ю', 'Ь', 'Й', 'Ц', 'Щ', 'Э', 'Х', 'У', 'З', 'Ф', 'Ш']

{'>': '_', '2': 'О', 'a': 'Е', 'А': 'Т', '7': 'И', 'О': 'А', 'r': 'С', '1': 'Н', 'Р': 'В', 'Ф': 'Л', 'Е': 'Р', 'Х': 'М', 'Д': 'П', '9': 'Д', 'У': 'К', ' ': 'Я', '3': 'Г', 't': 'Ч', 'b': 'Ж', '<': 'Ы', '0': 'Б', 'Я': 'Ю', 'Ы': 'Ь', '8': 'Й', 'М': 'Ц', 'Й': 'Щ', 'Ь': 'Э', 'Л': 'Х', 'Б': 'У', 'c': 'З', 'К': 'Ф', 'И': 'Ш'}
-------------------------------------------------------------------------------


Расшифровка:

>Р>rОХ2Х>ДЕ2rА2Х>РОЕ7О1Аa>Х29aФ7Е2РО17aХ> РФ aАr>2Мa1УО>РaЕ2 А12rА7>Д2 РФa17 >УОb9232>r7ХР2ФО>АО0Ф7МО>РaЕ2А12rАa8>Д2 РФa17 >УОb9232>r7ХР2ФО>2r12РО11О>1О>Д29rtaАa>tОrА2А>7Л>РrАЕatОaХ2rА7>1Оc<РОaАr>Х29aФЫЯ>ДaЕР232>ДЕ70Ф7ba17 >7Ф7>aЙa>ДaЕР232>Д2Е9УО>АО0Ф7МО>Бt7А<РОЯЙО>02Фaa>rФ2b1<a>cОР7r7Х2rА7>1ОДЕ7ХaЕ>Д2РФa17a>291232>r7ХР2ФО>Д2rФa>УОУ232А2>9ЕБ3232>7ХaЯА>r22АРaАrАРa112>РА2Е28>7>02Фaa>Д2Е 92У>r>Д2Х2ЙЫЯ>ЬА7Л>РaЕ2А12rАa8>Х2baА>0<АЫ>Р<t7rФa1О>Ь1АЕ2Д7>7>Д2rАЕ2a1>92rАОА2t12>ЬККaУА7Р1<8>У29>Д2cР2ФЯЙ78>rbОАЫ>АaУrА>1О7ФБtИО >rЕa91>9Ф71О>У29О>7>r22АРaАrАРa112>rАaДa1Ы>rbОА7 >92rА73ОaАr >Х29aФХ7>Р>У2А2Е<Л>2Мa1У7>РaЕ2 А12rА7>УОУ>Х2b12>02Фaa>А2t1<

_В_САМОМ_ПРОСТОМ_ВАРИАНТЕ_МОДЕЛИРОВАНИЕМ_ЯВЛЯЕТС_ОЦЕНКА_ВЕРОЯТНОСТИ_ПОЯВЛЕНИЯ_КАЖДОГО_СИМВОЛА_ТАБЛИЦА_ВЕРОТНОСТЕЙ_ПОЯВЛЕНИЯ_КАЖДОГО_СИМВОЛА_ОСНОВАННА_НА_ПОДСЧЕТЕ_ЧАСТОТ_ИХ_ВСТРЕЧАЕМОСТИ_НАЗЫВАЕТС_МОДЕЛЬЮ_ПЕРВОГО_ПРИБЛИЖЕНИЯ_ИЛИ_ЕЩЕ_ПЕРВОГО_ПОРДКА_ТАБЛИЦА_УЧИТЫВАЮЩА_БОЛЕЕ_СЛОЖНЫЕ_ЗАВИСИМОСТИ_НАПРИМЕР_ПОВЛЕНИЕ_ОДНОГО_СИМВОЛА_ПОСЛЕ_КАКОГОТО_ДРУГОГО_ИМЕЮТ_СООТВЕТСТВЕННО_ВТОРОЙ_И_БОЛЕЕ_ПОРЯДОК_С_ПОМОЩЬЮ_ЭТИХ_ВЕРОТНОСТЕЙ_МОЖЕТ_БЫТЬ_ВЫЧИСЛЕНА_ЭНТРОПИ_И_ПОСТРОЕН_ДОСТАТОЧНО_ЭФФЕКТИВНЫЙ_КОД_ПОЗВОЛЮЩИЙ_СЖАТЬ_ТЕКСТ_НАИЛУЧШАЯ_СРЕДН_ДЛИНА_КОДА_И_СООТВЕТСТВЕННО_СТЕПЕНЬ_СЖАТИЯ_ДОСТИГАЕТСЯ_МОДЕЛМИ_В_КОТОРЫХ_ОЦЕНКИ_ВЕРОЯТНОСТИ_КАК_МОЖНО_БОЛЕЕ_ТОЧНЫ
-------------------------------------------------------------------------------

Анализ: (кол-во символов, кол-во слов, частота всех слов)

1, 6, 0.07228915662650602
['Р', '7', 'r', '7', '7', 'Р']
['В', 'И', 'С', 'И', 'И', 'В']

2, 2, 0.024096385542168676
['1О', '7Л']
['НА', 'ИХ']

3, 4, 0.04819277108433735
['7Ф7', 'aЙa', 'У29', 'УОУ']
['ИЛИ', 'ЕЩЕ', 'КОД', 'КАК']

4, 3, 0.03614457831325301
['ЬА7Л', '0<АЫ', 'У29О']
['ЭТИХ', 'БЫТЬ', 'КОДА']

5, 13, 0.1566265060240964
['rОХ2Х', '02Фaa', 'Д2rФa', '7ХaЯА', '02Фaa', 'Х2baА', 'rbОАЫ', 'АaУrА', 'rЕa91', '9Ф71О', 'Х2b12', '02Фaa', 'А2t1<']
['САМОМ', 'БОЛЕЕ', 'ПОСЛЕ', 'ИМЕЮТ', 'БОЛЕЕ', 'МОЖЕТ', 'СЖАТЬ', 'ТЕКСТ', 'СРЕДН', 'ДЛИНА', 'МОЖНО', 'БОЛЕЕ', 'ТОЧНЫ']

6, 7, 0.08433734939759036
['2Мa1УО', 'tОrА2А', 'Д2Е9УО', '291232', 'РА2Е28', 'rbОА7 ', '2Мa1У7']
['ОЦЕНКА', 'ЧАСТОТ', 'ПОРДКА', 'ОДНОГО', 'ВТОРОЙ', 'СЖАТИЯ', 'ОЦЕНКИ']

7, 20, 0.24096385542168675
['ДЕ2rА2Х', ' РФ aАr', 'УОb9232', 'r7ХР2ФО', 'АО0Ф7МО', 'УОb9232', 'r7ХР2ФО', 'Х29aФЫЯ', 'ДaЕР232', 'ДaЕР232', 'АО0Ф7МО', 'rФ2b1<a', 'r7ХР2ФО', '9ЕБ3232', 'Д2Е 92У', 'Д2Х2ЙЫЯ', 'Ь1АЕ2Д7', 'rАaДa1Ы', 'Х29aФХ7', 'У2А2Е<Л']
['ПРОСТОМ', 'ЯВЛЯЕТС', 'КАЖДОГО', 'СИМВОЛА', 'ТАБЛИЦА', 'КАЖДОГО', 'СИМВОЛА', 'МОДЕЛЬЮ', 'ПЕРВОГО', 'ПЕРВОГО', 'ТАБЛИЦА', 'СЛОЖНЫЕ', 'СИМВОЛА', 'ДРУГОГО', 'ПОРЯДОК', 'ПОМОЩЬЮ', 'ЭНТРОПИ', 'СТЕПЕНЬ', 'МОДЕЛМИ', 'КОТОРЫХ']

8, 6, 0.07228915662650602
['РОЕ7О1Аa', 'Д29rtaАa', '1ОДЕ7ХaЕ', 'Д2РФa17a', 'УОУ232А2', 'Д2rАЕ2a1']
['ВАРИАНТЕ', 'ПОДСЧЕТЕ', 'НАПРИМЕР', 'ПОВЛЕНИЕ', 'КАКОГОТО', 'ПОСТРОЕН']

9, 6, 0.07228915662650602
['Д2 РФa17 ', 'Д2 РФa17 ', '2r12РО11О', '1Оc<РОaАr', 'Р<t7rФa1О', '1О7ФБtИО ']
['ПОЯВЛЕНИЯ', 'ПОЯВЛЕНИЯ', 'ОСНОВАННА', 'НАЗЫВАЕТС', 'ВЫЧИСЛЕНА', 'НАИЛУЧШАЯ']

10, 3, 0.03614457831325301
['Бt7А<РОЯЙО', '92rАОА2t12', 'Д2cР2ФЯЙ78']
['УЧИТЫВАЮЩА', 'ДОСТАТОЧНО', 'ПОЗВОЛЮЩИЙ']

11, 8, 0.0963855421686747
['РaЕ2 А12rА7', 'РaЕ2А12rАa8', 'ДЕ70Ф7ba17 ', 'cОР7r7Х2rА7', 'РaЕ2А12rАa8', 'ЬККaУА7Р1<8', '92rА73ОaАr ', 'РaЕ2 А12rА7']
['ВЕРОЯТНОСТИ', 'ВЕРОТНОСТЕЙ', 'ПРИБЛИЖЕНИЯ', 'ЗАВИСИМОСТИ', 'ВЕРОТНОСТЕЙ', 'ЭФФЕКТИВНЫЙ', 'ДОСТИГАЕТСЯ', 'ВЕРОЯТНОСТИ']

13, 1, 0.012048192771084338
['РrАЕatОaХ2rА7']
['ВСТРЕЧАЕМОСТИ']

14, 3, 0.03614457831325301
['Х29aФ7Е2РО17aХ', 'r22АРaАrАРa112', 'r22АРaАrАРa112']
['МОДЕЛИРОВАНИЕМ', 'СООТВЕТСТВЕННО', 'СООТВЕТСТВЕННО']