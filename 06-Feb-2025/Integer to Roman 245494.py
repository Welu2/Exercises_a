# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        symbol=['I' ,'V','X','L' ,'C','D' ,'M']
        value=[1,5,10,50,100,500,1000]
        d=dict(zip(value,symbol))
        numbers=[int(j) for j in str(num)]
        index=len(numbers)-1
        roman=[]
        for i in numbers:
            if i in d:
                roman.append(d[i*(10**index)])
            elif i == 4 or i ==9:

                if index==1:
                    if i ==4:
                        roman.append("XL")
                    else:
                        roman.append("XC")
                elif index==2:
                    if i ==4:
                        roman.append("CD")
                    else:
                        roman.append("CM")
                elif  index==0:
                    if i ==4:
                        roman.append("IV")
                    else:
                        roman.append("IX")
            else:
                if 0< i <4:
                    roman.append(d[(10**index)]*i)
                elif 9 >i > 5:
                    roman.append(d[(5*(10**index))]+(i-5)*d[(10**index)])
            index-=1
        return "".join(roman)
            






            

              

           