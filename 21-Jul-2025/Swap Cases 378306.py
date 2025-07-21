# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    words = ""
    for c in range(len(s)):
        if (s[c].isupper()):
            word = s[c].lower()
            words += word
        elif (s[c].islower()):
            word = s[c].upper()
            words += word
        else:
            word = s[c]
            words += word
        
            
    return words

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)