from main.exception import DifferentLengthOfVectorsException, VectorException


class Vector:

    def __check_length(x, y):
        if len(x) != len(y):
            raise DifferentLengthOfVectorsException()

    @staticmethod
    def sum(x, y):
        Vector.__check_length(x, y)
        result = x[:]

        for i in range(len(x)):
            result[i] += y[i]

        return result

    @staticmethod
    def difference(x, y):
        Vector.__check_length(x, y)
        result = x[:]

        for i in range(len(x)):
            result[i] = result[i] - y[i]

        return result

    @staticmethod
    def multiply(x, number):
        result = x[:]

        for i in range(len(x)):
            result[i] *= number

        return result


x = [0, 5, 7, -1]
y = [5, -7, 3, 4]

try:
    print(Vector.sum(x, y))
    print(Vector.difference(x, y))
    print(Vector.multiply(x, 2))
except VectorException as e:
    print(e.message)
