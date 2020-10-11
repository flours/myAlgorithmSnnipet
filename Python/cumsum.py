# 1 dimention cumlative sum
class cumsum:
    # initValue is int or list
    def __init__(self, initValue):
        self.N = 0
        if isinstance(initValue, int):
            self.data = [0] * initValue
            self.N = initValue
        elif isinstance(initValue, list):
            self.data = [0] * (len(initValue) + 1)
            for i in range(len(initValue)):
                self.data[i + 1] = self.data[i] + initValue[i]
            self.N = len(initValue)
        else:
            raise "Type Error:initValue can int or list"

    def getSum(self, right):
        return self.data[right + 1]

    def rangeSum(self, left, right):
        return self.data[right] - self.data[left]

    # Attention!! O(N) operation
    def add(self, index, value):
        for i in range(index + 1, self.N + 1):
            self.data[i] += value


class cumsum2D:
    # apply 2D list
    def __init__(self, l):
        H = len(l)
        W = len(l[0])
        self.data = [[0] * (W + 1) for i in range(H + 1)]
        for i in range(1, H+1):
            for j in range(1, W + 1):
                self.data[i][j] += self.data[i][j - 1]
                self.data[i][j] += l[i - 1][j - 1]
            for j in range(1, W + 1):
                self.data[i][j] += self.data[i - 1][j]

    def rangeSum(self, left, right, top, down):
        return self.data[down][right] - self.data[top][right] - self.data[down][left] + self.data[top][left]


if __name__ == '__main__':
    array = [1, 1, 3, 5, 4, 78, 7]
    cs = cumsum(array)
    print(cs.data)
    print(cs.getSum(2))
    print(cs.rangeSum(1, len(array)))
    cs.add(2, 4)
    print(cs.rangeSum(0, 3))

    # 2d
    array = [
        [1, 2, 3],
        [2, 3, 4],
        [5, 6, 7]
    ]
    cs = cumsum2D(array)
    print(cs.rangeSum(1, 3, 1, 3))  # 3+4+6+7
