class mo:
    # data 左端を右に動かす(leftadd)、左端を左に動かす(leftsub)、右端を右に動かす(rightadd)、右端を左に動かす(righsub)メソッドを持つクラス
    # 初期化時は左端(left)、右端(right)ともに0
    # q (l,r)のクエリ
    # N (l,r)の右端(左端は0)
    def __init__(self, data, q, N):
        self.data = data
        self.q = q

    def solve(self):
        num_block = int(len(self.q) ** 0.5)
        self.blockedQ = [[] for i in range(num_block)]
        for l, r in self.q:
            self.blockedQ[l * num_block // N] += ((l, r),)
        for i in range(len(self.blockedQ)):
            self.blockedQ[i].sort(key=lambda x: x[1])

        ans = {}
        for block in self.blockedQ:
            for l, r in block:
                while self.data.left > l:
                    self.data.leftsub()
                while self.data.right < r:
                    self.data.rightadd()
                while self.data.left < l:
                    self.data.leftadd()
                while self.data.right > r:
                    self.data.rightsub()
                ans[(l, r)] = self.data.ans
        ret = []
        for l, r in self.q:
            ret += (ans[(l, r)],)
        return ret


# ABC242G
def ABC242G():
    class paringQuery:
        def __init__(self, N, A):
            self.left = 0
            self.right = 0
            self.array = [0] * (N + 1)
            self.A = A
            self.ans = 0
            self.array[A[0]] += 1

        def leftadd(self):
            self.array[A[self.left]] -= 1
            if self.array[A[self.left]] % 2 != 0:
                self.ans -= 1
            self.left += 1

        def leftsub(self):
            self.left -= 1
            self.array[A[self.left]] += 1
            if self.array[A[self.left]] % 2 == 0:
                self.ans += 1

        def rightadd(self):
            self.right += 1
            self.array[A[self.right]] += 1
            if self.array[A[self.right]] % 2 == 0:
                self.ans += 1

        def rightsub(self):
            self.array[A[self.right]] -= 1
            if self.array[A[self.right]] % 2 != 0:
                self.ans -= 1
            self.right -= 1

    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    lr = []
    for i in range(Q):
        l, r = map(int, input().split())
        lr += ((l - 1, r - 1),)
    dataset = paringQuery(N, A)
    solver = mo(dataset, lr, N)
    ans = solver.solve()
    for i in ans:
        print(i)
