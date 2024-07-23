calls = 0


def count_calls():
    global calls
    calls += 1


def string_info():
    global calls
    string = str(input('Ведите строку: '))
    a = (len(string), string.upper(), string.lower())
    print(a)
    count_calls()
    return


def is_contains():
    global calls
    string = str(input('Ведите строку: '))
    list_ = list(map(str, input('Введите список: ').split()))
    print(string, list_)
    string1 = string.lower()
    list1 = str(" , ".join(list_)).lower()
    if string1 in list1:
        print(True)
    else:
        print(False)
    count_calls()
    return


string_info()
string_info()
is_contains()
is_contains()
is_contains()

print(calls)
