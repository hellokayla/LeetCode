class Solution(object):
    def permute(self, nums):
        
        def permute_helper(nums, s_i, e_i):
            # when finished
            if s_i == e_i:
                # must append copy rather than referance
                res.append(nums[:]) 
            else: 
                for i in xrange(s_i, e_i):
                    ## swap
                    nums[s_i], nums[i] = nums[i], nums[s_i]

                    ## permute
                    permute_helper(nums, s_i+1, e_i)


                    ## swap back 
                    nums[s_i], nums[i] = nums[i], nums[s_i]
        res = []
        permute_helper(nums,0, len(nums))
        return res   