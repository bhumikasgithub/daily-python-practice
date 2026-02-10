def count_decodings(dig):
    n = len(dig)
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1]

        if dig[i - 2] == '1' or (dig[i - 2] == '2' and dig[i - 1] < '7'):
            dp[i] += dp[i - 2]

    return dp[n]


dig = input("Enter Number: ")
print("Decoding count:", count_decodings(dig))
