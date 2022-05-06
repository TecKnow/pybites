class Matrix:

    @staticmethod
    def _matrix_multiply(A, B):
        return [[sum(a * b
                     for a, b in zip(A_row, B_col))
                 for B_col in zip(*B)]
                for A_row in A]

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, _o):
        if isinstance(_o, Matrix) or hasattr(_o, "values"):
            _o = _o.values
        return Matrix(self._matrix_multiply(self.values, _o))

    def __rmatmul__(self, _o):
        if isinstance(_o, Matrix) or hasattr(_o, "values"):
            _o = _o.values
        return Matrix(self._matrix_multiply(self.values, _o))

    def __imatmul__(self, _o):
        if isinstance(_o, Matrix):
            _o = _o.values
        self.values = self._matrix_multiply(self.values, _o)
        return self
