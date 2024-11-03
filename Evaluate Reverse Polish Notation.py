#Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sym = ['+','*','/','-']
        res = []
        for i in tokens:
            if i in sym:
                a = res.pop()
                b = res.pop()
                if i == '+':
                    res.append(a+b)
                elif i == '-':
                    res.append(b-a)
                elif i == '/':
                    res.append(int(b/a))
                else:
                    res.append(a*b)
            else:
                res.append(int(i))
        return int(res[0])