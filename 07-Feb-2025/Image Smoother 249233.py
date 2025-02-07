# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer=[]
        def calculate(img,a,b):
            d=[[a-1,b-1], [a-1,b], [a-1,b+1], [a,b-1], [a,b],[a,b+1],[a+1,b-1],[a+1,b+1],[a+1,b]]
            c=0
            total=0
            for i in d:
                if 0<= i[0] <len(img) and 0<=i[1]<len(img[0]):
        
                    total += img[i[0]][i[1]]
                    c+=1
            if c ==0:
                return total
            return total // c 
        
        for i in range(len(img)):
            answer.append([0]*len(img[0]))
        
        for i in range(len(img)):
            for j in range(len(img[i])):
                answer[i][j]=calculate(img,i,j)
                
                
                    
        return answer


