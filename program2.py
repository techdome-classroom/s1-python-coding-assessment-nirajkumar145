def decode_message(s: str, p: str) -> bool:
    # Get lengths of the message and pattern
    m, n = len(s), len(p)

    # Create a DP table with (m+1) x (n+1) dimensions
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty pattern matches empty message
    dp[0][0] = True

    # Fill the first row for patterns starting with '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match 0 characters or more
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # '?' matches any single character or exact match
                dp[i][j] = dp[i - 1][j - 1]

    # The result is in the bottom-right cell
    return dp[m][n]

# Example usage
print(decode_message("aa", "a"))  # Output: False
print(decode_message("aa", "*"))  # Output: True
print(decode_message("cb", "?a"))  # Output: False
