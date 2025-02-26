class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # Hash Table to Map closing brackets to opening brackets
        closeToOpen = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        # Iterate through each character in the input string
        for n in s:
            if n in closeToOpen:
                # If the character is a closing bracket, check if the stack is not empty
                # and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == closeToOpen[n]:
                    # Remove the matching opening bracket from the stack
                    stack.pop()
                else:
                    # If there's no match or the stack is empty, return False
                    return False
            else:
                # If the character is an opening bracket, add it to the stack
                stack.append(n)

        # After processing all characters, return True if the stack is empty (all brackets matched)
        # Otherwise, return False (unmatched opening brackets remain in the stack)
        return True if not stack else False
