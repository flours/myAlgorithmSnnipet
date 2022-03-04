def genCombinationFunction(max_k, mod):
    modinv_table = [-1] * (max_k + 1)
    modinv_table[1] = 1
    for i in range(2, max_k + 1):
        modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

    def binomial_coefficients(n, k):
        ans = 1
        for i in range(k):
            ans *= n - i
            ans *= modinv_table[i + 1]
            ans %= mod
        return ans

    return binomial_coefficients
# 前処理O(N)でO(1)nCr

def genO1CombinationFunction(N,mod):
    table=[1]
    inv_table=[1]

    for i in range(1,N):
      table+=table[-1]*i%mod,
      inv_table+=pow(table[-1],mod-2,mod),

    def nCr(n,r):
      return table[n]*inv_table[r]*inv_table[n-r]%mod

    return nCr


if __name__ == "__main__":
    n = 10 ** 9
    k = 2 * 10 ** 5
    mod = 10 ** 9 + 7
    f = genCombinationFunction(k, mod)
    print(f(n, k))
    print(f(10, 3))
    f=genO1CombinationFunction(10**6, 998244353)
    print(f(10,3))
