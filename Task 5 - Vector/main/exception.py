class VectorException(Exception):
    def __init__(self):
        self.message = "Vector's error"


class DifferentLengthOfVectorsException(VectorException):
    def __init__(self):
        self.message = "Vectors have different length"
