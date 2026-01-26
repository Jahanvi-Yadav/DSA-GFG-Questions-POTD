#Generate Permutations of an array. 
#GFG POTD using Python.
class Solution:
    def permuteDist(self, arr):
        n = len(arr)
        used = [False] * n
        
        def dfs(acc: list[int]=[], output: list[int]=[]) -> list[int]:
            if len(acc) == n:
                output.append(acc.copy())
                return output
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                acc.append(arr[i])
                dfs()
                acc.pop()
                used[i] = False
            return output
        
        return dfs()
