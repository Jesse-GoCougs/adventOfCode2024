import heapq
# Read and process the data from the text file
data = []
leftHeap = []
rightHeap = []
totalDistance = 0
similarityScore = 0 
rightFrequency = {}
leftElements = []


with open("data.txt", "r") as file:
    for line in file:
        # Split each line by whitespace
        left, right =  map(int, line.split())
        leftElements.append(left)
        rightFrequency[right] = rightFrequency.get(right, 0) + 1
        heapq.heappush(leftHeap, left)
        heapq.heappush(rightHeap, right)

#part one day one challenge
while leftHeap and rightHeap:
    leftMin = heapq.heappop(leftHeap)
    rightMin = heapq.heappop(rightHeap)
    totalDistance += abs(leftMin - rightMin)

#part 2 day one challenge 
for element in leftElements:
    similarityScore += element * rightFrequency.get(element, 0)


print(totalDistance)
print(similarityScore)