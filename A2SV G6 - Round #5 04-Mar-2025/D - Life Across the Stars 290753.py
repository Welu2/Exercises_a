# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

t = int(input())

dict={}
for _ in range(t):
   
    st,end = map(int,input().split())
    dict[st]=dict.get(st,0)+1
    dict[end]=dict.get(end,0)-1


sorted_dict = sorted(dict.items(), key=lambda item: item[0])

cumulative =0
result = []
for key, value in sorted_dict:
    cumulative += value
    result.append((key, cumulative))

year=0
people=0
for i in range(len(result)):
    if people < result[i][1]:
        people=result[i][1]
        year=result[i][0]

print(year,people)












    
