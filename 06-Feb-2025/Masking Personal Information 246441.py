# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        answer=[]
        def isnums(n):
            num=[]
            for i in n:
                if i != '+' and i !=  '-' and i != '(' and i != ')' and i!= ' ':
                    num.append(i)
            return num

        if "@" in s:
            domain,com=s.split("@")   
            domain=domain.lower()
            answer.append(domain[0]+"*****"+domain[-1]+'@'+com.lower())
            return "".join(answer)
        num=isnums(s)
        last=num[-4:]
        if len(num)==10:
            answer.append("***-***-")
            
        elif len(num)==11:
            answer.append("+*-***-***-")
            
        elif len(num)==12:
            answer.append("+**-***-***-")
            
        else:
            answer.append("+***-***-***-")
        answer.append("".join(last))
        return "".join(answer)
           
             
