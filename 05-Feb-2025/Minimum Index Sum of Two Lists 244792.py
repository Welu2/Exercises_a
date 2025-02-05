# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common=defaultdict(list)
        for i in range(len(list1)):
            if list1[i] in list2:
                common[list1[i]]=common.get(list1[i], 0) + i
        
        for j in range(len(list2)):
            if list2[j] in list1:
                common[list2[j]]+=j
        

        result=[]
        sortedValue= dict(sorted(common.items(), key=lambda item: item[1]))
        first_value = list(sortedValue.values())[0]
        
      
        for key,value in sortedValue.items():
            if value == first_value:
                result.append(key)
            else:
                break

        return result


        