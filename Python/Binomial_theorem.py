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


if __name__ == "__main__":
    n = 10 ** 9
    k = 2 * 10 ** 5
    mod = 10 ** 9 + 7
    f = genCombinationFunction(k, mod)
    print(f(n, k))
    print(f(10, 3))
