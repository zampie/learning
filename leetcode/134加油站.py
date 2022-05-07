'''
# n2
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)


        for i in range(length):
            tank = 0
            for j in range(length):
                index = (i+j)%length
                tank += gas[index]
                tank -=cost[index]
                if tank < 0:
                    break
            if tank >=0:
                return i

        return -1

# n1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        length = len(gas)
        totalTank = 0
        currTank = 0
        startIndex = 0

        for i in range(length):
            currTank += gas[i] - cost[i]
            totalTank += gas[i] - cost[i]
            if currTank < 0:
                startIndex = i+1
                currTank = 0

        return startIndex if totalTank >=0 else -1
'''