# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain=defaultdict()
        for i in cpdomains:
            no,part=i.split()
            part=part.split(".")
            
            for j in range(len(part)):
                joined=".".join(part[j:])
                domain[joined]=domain.get(joined, 0) + int(no)
        
        result=[]
        for j in domain:
            result.append(f"{domain[j]}" + " " +f"{j}")
        return result