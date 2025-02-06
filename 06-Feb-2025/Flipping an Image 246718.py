# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
        n=len(image)
        for i in range(n):
            for j in range(n):
                if image[i][j] ==0:
                    image[i][j]=1
                else:
                    image[i][j]= 0
        return image