# Функция на вход принимает список и возвращает новый список без первого и последнего элемента
def create_new_list(sourceList):
    if isinstance(sourceList, list):
        print(sourceList)
        resultList = []
        for j in sourceList[1:len(sourceList) - 1]:
            resultList.append(j)
        print(resultList)
        return resultList
    else:
        print("Некорректное значение")


create_new_list([10, 20, 30, 40])
