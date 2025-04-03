# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val=Counter(nums)
        bucket=[[] for _ in range(len(nums)+1)]
    
        for i,freq in val.items():
            bucket[freq].append(i)
      
        ans=[]
        for i in range(len(nums),-1,-1):
            if bucket[i] != [] and len(ans) < k:
                ans.extend(bucket[i])
                
        return ans


      



        # freq_dic=Counter(nums)
        # heap=[(-freq,num)for num,freq in freq_dic.items()]
        # heapq.heapify(heap)
        # result=[]
        # while k>0:
        #     result.append(heapq.heappop(heap)[1])
        #     k-=1

        # return result
       

       
       