class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parlist={")":"(","}":"{","]":"["}
        for c in s:
           if c in parlist:
            if stack and stack[-1]==parlist[c]:
                stack.pop()
            else:
                return False
           else:
            stack.append(c)
        return True if not stack else False
