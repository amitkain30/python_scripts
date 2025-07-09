# Encode and decode a list of strings to a single string
# Input: ["neet", "code", "love", "you"]
# Output: ["neet", "code", "love", "you"]

class Solution:

    def encode(self, strs: list[str])->str:
        res = ""
        for s in strs:
            res+=str(len(s)) + "#" + s
        return res

    def decode(self, s:str)->list[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        
        return res

if __name__=="__main__":
    something = ["neet", "code", "love", "you"]

    res = Solution()

    temp = res.encode(something)
    print(temp)

    print(res.decode(temp))

