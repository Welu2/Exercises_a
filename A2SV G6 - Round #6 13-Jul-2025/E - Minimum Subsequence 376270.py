# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E


def solve():
    
    # Read input: length of binary string
    n = int(input().strip())
    
    # Convert input string into a list of integers (0s and 1s)
    nums = [int(i) for i in input().strip()]

    zero = []   # Tracks subsequences ending in 0
    one = []    # Tracks subsequences ending in 1
    ans = []    # Stores the assigned subsequence number for each character
    maxi = 0    # Keeps track of the total number of subsequences used

    # Process each character in the binary string
    for val in nums:
        if val == 1:  # If the current character is '1'
            if zero:
                # If there exists a subsequence ending in '0', use it
                temp = zero.pop()
            else:
                # Otherwise, create a new subsequence
                maxi += 1
                temp = maxi 
              
            # Mark that this subsequence now ends in '1'
            one.append(temp)
            ans.append(temp)

        else:  # If the current character is '0'
            if one:
                # If there exists a subsequence ending in '1', use it
                temp = one.pop()
            else:
                # Otherwise, create a new subsequence
                maxi += 1
                temp = maxi 

            # Mark that this subsequence now ends in '0'
            zero.append(temp)
            ans.append(temp)

    # Print the total number of subsequences used
    print(max(ans))
    
    # Print the assigned subsequence number for each character
    print(*ans)

q = int(input().strip())

for _ in range(q):
    solve()