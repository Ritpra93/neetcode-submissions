class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #last combination sum was dfs so use a stack, but why??
        #unique combinations let's use a set
        #sum to target
        #same as 1 but need to factor in set somehow so it's unique
        #whole point is not to use a set hmmm
        '''
        #brute force below so I can build intuition
        res = set()
        candidates.sort()

        def generate_subsets(i, cur, total):
            #this is the same as combinations 1 basically
            if total == target:
                res.add(tuple(cur))
                return
                #adding tuple instead of copy diff
            if total > target or i == len(candidates):
                return 
            cur.append(candidates[i])
            generate_subsets(i+1, cur, total+candidates[i])
            cur.pop()
            generate_subsets(i+1, cur, total)
        generate_subsets(0, [], 0)
        return [list(combination) for combination in res]
        '''
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()


            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
        #look at optimized solution now



       
        