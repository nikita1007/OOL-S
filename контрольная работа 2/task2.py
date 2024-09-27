def longest_monotone_subsequence(arr):
    def longest_non_decreasing_subsequence(arr):
        n = len(arr)
        dp = * n

        for i in range(1, n):
            for j in range(i):
                if arr[i] >= arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def longest_non_increasing_subsequence(arr):
        n = len(arr)
        dp = * n

        for i in range(1, n):
            for j in range(i):
                if arr[i] <= arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    return max(longest_non_decreasing_subsequence(arr), longest_non_increasing_subsequence(arr))
