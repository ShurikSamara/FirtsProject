def search_common_letters(str_1, str_2):
    list_common_letters = []
    for i in str_1:
        for j in str_2:
            if i == j:
                list_common_letters.append(j)
                print(j)
    print(list_common_letters)


search_common_letters("abccd", "dabr")