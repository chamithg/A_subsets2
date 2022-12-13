class Solution:
    def subsetsWithDup(self, nums):
        
        output = []
        output.append([])
        output.append(nums)
        
        def backtrack(nums,length,start,temp):
            if len(temp)== length:
                subset = sorted(temp[:])
                if subset not in output:
                    output.append(subset)
                return

            for i in range(start,len(nums)):
                temp.append(nums[i])
                backtrack(nums,length,i+1,temp)
                temp.pop()
                
                
        for j in range(1,len(nums)+1): 
            backtrack(nums,j,0,[])        
         
        return output
    
nums = [1,2,2]


obj = Solution()

print(obj.subsetsWithDup(nums))