# TODO
# Simplify logic, checking" b!= "." in mutiple places
# instead of manually handling squareLocation and index,use box_index = (r // 3) * 3 + (c // 3)

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        dictSets = {i: set() for i in range(len(board))}
        boxSets = {i: set() for i in range(9)}
        squareLocation = 0
        rowhits = -1
        for row in board:
            checkSet = set()
            rowhits += 1

            for index, b in enumerate(row):
                if rowhits == 3:

                    rowhits = 0
                    squareLocation += 3

                # Checks horizontal
                if b in checkSet and b != ".":
                    return False
                checkSet.add(b)
                # Checks vertical
                if b in dictSets[index] and b != ".":
                    return False

                dictSets[index].add(b)

                # Checks boxes

                if index <= 2:
                    if b in boxSets[squareLocation] and b != ".":

                        return False
                    boxSets[squareLocation].add(b)

                if index <= 5 and index > 2:
                    if b in boxSets[squareLocation + 1] and b != ".":

                        return False

                    boxSets[squareLocation + 1].add(b)

                if index <= 8 and index > 5:
                    if b in boxSets[squareLocation + 2] and b != ".":

                        return False

                    boxSets[squareLocation + 2].add(b)

        return True


obj = Solution()
print(obj.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
