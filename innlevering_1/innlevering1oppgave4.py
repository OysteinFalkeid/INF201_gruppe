with open("norway_municipalities_2017.csv", "r", encoding="utf-8") as file:
    headders = file.readline().replace("\n","").split(",")
    data = [line.strip().split(",") for line in file.readlines()]   
    
districts = []
for i in range(len(data)):
    if data[i][1] not in districts:
        districts.append(data[i][1])
     
population = [0 for _ in range(len(districts))]
    
for i in range(len(data)):
    population[districts.index(data[i][1])] += int(data[i][2])

for i in range(len(districts)):
    while len(districts[i]) < 25:
        districts[i] += " "
        
table = sorted(zip(population, districts), reverse = True)

print(headders[1] + "                 " +headders[2])            
for i in range(len(population)):
    print(table[i][1], end = "")
    print(table[i][0])