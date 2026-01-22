class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        l = 0
        r = n-1
        if n%2!=0:
            while l<r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            if l==r:
                return True
        if n%2==0:
            while l<r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            if l>r:
                return True
            
