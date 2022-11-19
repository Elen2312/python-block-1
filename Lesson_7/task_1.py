# # Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# # __init__()), который должен принимать данные (список списков) для формирования матрицы.
# # Подсказка: матрица — система некоторых математических величин, расположенных в виде
# # прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m = ''
        for i in range(len(self.matrix)):
            m += '\t'.join(map(str, self.matrix[i])) + '\n'
        return m

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return 'Матрицы разного размера'
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


m1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
m2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
