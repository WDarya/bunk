# a = [[1,2,3,4],[5,6,7,8],[9,1,6,8],[6,5,3,1]]
# print(*a,sep="\n")
#
# n = len(a)
# min_sum = float('inf') # Изначально устанавливаем значение бесконечности
# diagonal_sum1 = 0
# diagonal_sum2 = 0
# for i in range(1, n):
#     diagonal_sum1 = sum(a[j + i][j] for j in range(n - i))
#     diagonal_sum2 = sum(a[j][j+i] for j in range(n - i))
#     print("Нижняя ",diagonal_sum1)
#     print("Верхняя ",diagonal_sum2)
#     if diagonal_sum1 < min_sum:
#         min_sum = diagonal_sum1
#     if diagonal_sum2 < min_sum:
#         min_sum = diagonal_sum2
# print(min_sum)
print(320/9)