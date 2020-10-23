def delete_empty_tuple():
    aList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(aList) # Вывод исходного списка
    resultList = [i for i in aList if len(i) != 0]
    print(resultList) #Вывод результирующего списка


delete_empty_tuple()
