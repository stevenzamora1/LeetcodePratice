def evalRPN(tokens: list[str]) -> int:
    tokenStack = []
    for n in tokens:

        if n == "+":
            tempSoultion = tokenStack.pop() + tokenStack.pop()
            tokenStack.append(tempSoultion)

        elif n == "-":

            num1 = tokenStack.pop()
            num2 = tokenStack.pop()

            tempSoultion = num2 - num1
            tokenStack.append(tempSoultion)

        elif n == "*":
            tempSoultion = tokenStack.pop() * tokenStack.pop()
            tokenStack.append(tempSoultion)

        elif n == "/":

            num1 = tokenStack.pop()
            num2 = tokenStack.pop()

            tempSoultion = int(num2 / num1)
            tokenStack.append(tempSoultion)

        else:
            tokenStack.append(int(n))
    return tokenStack.pop()


print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
