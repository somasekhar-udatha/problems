'''Longest Palindromic Substring Length (Difficulty - medium)
Description :
    Given a string S, find the length of the longest palindromic substring of S.
code : '''

t = int(input())
for m in range(t):
    S = input()
    s = S.lower()
    n = len(s)
    max_len = 1 
    l = 0
    r = 0
    # for odd length palindrome 
    for i in range(n-1):
        l = i 
        r = i 
        while ( l >=0 and r < n):
            if s[l] == s[r] :
                l = l - 1 
                r = r + 1 
            else :
                break 
        plen = r-l-1
        if plen > max_len :
            max_len = plen
    for j in range(n-1):
        l = j 
        r = j + 1 
        while (l >= 0 and r < n):
            if s[l] == s[r]:
                l = l - 1 
                r = r + 1 
            else:
                break 
        plen = r- l - 1
        if plen > max_len :
            max_len = plen
    print(max_len)
