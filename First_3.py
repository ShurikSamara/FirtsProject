def delete_empty_tuple():
    sourceList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(sourceList)  # Вывод исходного списка
    resultList = [i for i in sourceList if len(i) != 0]
    print(resultList)  # Вывод результирующего списка


delete_empty_tuple()
