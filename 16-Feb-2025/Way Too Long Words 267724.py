# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

no = int(input())
 
 
for _ in range(no):
    string = input()
    if len(string) > 10:
        print(string[0] + str(len(string) - 2) + string[-1])
    else:
        print(string)