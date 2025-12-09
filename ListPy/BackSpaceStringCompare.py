# def BackSpace(string):

#     stack = []

#     for ch in string:
#         if ch == "#":
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(ch)
    
#     return "".join(stack)


            
            

# def backspaceCompare(str1, str2):
#     return BackSpace(str1) == BackSpace(str2)
class Solution(object):
   def BackSpace(self, string):

        stack = []

        for ch in string:
            if ch == "#":
                if self.stack:
                    self.stack.pop()
            else:
                self.stack.append(ch)
        
        return "".join(self.stack)            

def backspaceCompare(self, str1, str2):
    return self.BackSpace(str1) == self.BackSpace(str2)    
   

s = "ab##"
t = "c#d#"
print(backspaceCompare(s, t))