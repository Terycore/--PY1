def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_

    str_ = str_.lower().split(' ')
    str_ = ''.join(str_)
    strr_ = {}
    for i in str_:
        if i.isalpha() and i not in strr_:
            strr_[i] = str_.count(i)
    return strr_


main_str = """Данное предложение будет разбиваться на отдельные слова. В качестве разделителя для встроенного метода 
split будет выбран символ пробела. На выходе мы получим список отдельных слов. Далее нужно отсортировать слова в 
алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!! """
print(get_count_char(main_str))
a = get_count_char(main_str)


def get_count2(strr_):
    new = {}
    b = sum(strr_.values())
    for j in strr_:
        new[j] = int((strr_[j] / b) * 100)
    return new


print(get_count2(a))
