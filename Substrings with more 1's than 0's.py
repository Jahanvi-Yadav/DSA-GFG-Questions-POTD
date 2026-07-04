#Given a binary string s consists only of 0s and 1s. Calculate the number of substrings that have more 1s than 0s.
class Solution():
    def countSubstring(self, S):
        lenS = len(S)
        timesOfValue = [0]*(2*lenS + 1)
        i0 = lenS
        substrs = 0 
        currValue = 0
        ended = 0
        timesOfValue[i0] = 1
        for i in range(lenS):
            if(S[i]=='1'):
                ended += timesOfValue[i0+currValue]
                currValue += 1
            else:
                ended -= timesOfValue[i0+currValue-1]
                currValue -= 1            
            substrs += ended    
            timesOfValue[i0+currValue] +=1    
        return substrs
