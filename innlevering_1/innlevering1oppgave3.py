
NumberOfCalculations = 11
DistanceBetweenValues = 7
TableMatrix = [[0 for col in range(NumberOfCalculations)] for row in range(3)]

ListOfFirstOrder = []
for i in range(NumberOfCalculations):
    ListOfFirstOrder.append(str(i**1))
#print(ListOfFirstOrder)

ListOfSecondOrder = []
for i in range(NumberOfCalculations):
    ListOfSecondOrder.append(str(i**2))
#print(ListOfSecondOrder)

ListOfThirdOrder = []
for i in range(NumberOfCalculations):
    ListOfThirdOrder.append(str(i**3))
#print(ListOfThirdOrder)


for i in range(NumberOfCalculations):
    while len(ListOfFirstOrder[i]) < DistanceBetweenValues:
        ListOfFirstOrder[i] = " " + ListOfFirstOrder[i]
    while len(ListOfSecondOrder[i]) < DistanceBetweenValues:
        ListOfSecondOrder[i] = " " + ListOfSecondOrder[i]
    while len(ListOfThirdOrder[i]) < DistanceBetweenValues:
        ListOfThirdOrder[i] = " " + ListOfThirdOrder[i]

TableMatrix[0] = ListOfFirstOrder
TableMatrix[1] = ListOfSecondOrder
TableMatrix[2] = ListOfThirdOrder

for i in range(DistanceBetweenValues*3):
    print("-", end="")
print()
print("      x    x^2    x^3")
for i in range(DistanceBetweenValues*3):
    print("-", end="")
print()

for i in range(NumberOfCalculations):
    print(TableMatrix[0][i] + TableMatrix[1][i] + TableMatrix[2][i])
    
for i in range(DistanceBetweenValues*3):
    print("-", end="")
print()