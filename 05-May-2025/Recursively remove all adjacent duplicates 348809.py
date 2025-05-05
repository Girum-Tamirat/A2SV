# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#User function Template for python3

class Solution:
    def removeUtil(self, S):
        # Convert string to list
        res = ""
        i = 0
        while i < len(S):
            rept = False
            while i + 1 < len(S) and S[i] == S[i+1]:
                rept = True
                i += 1
            if not rept:
                res += S[i]
            i += 1
        return res if len(S)==len(res) else self.removeUtil(res)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        s = ob.removeUtil(S)
        if len(s) == 0:
            print("\"\"")
        else:
            print(s)

        print("~")

# } Driver Code Ends