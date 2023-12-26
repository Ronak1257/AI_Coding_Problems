# solve for travel salesman problem of 5 cities consider the datapoint of the cities as random value. (range < 20).

import random

city=5
city_pos=[random.randint(1, 20) for _ in range(city)]
print("random selcted city is : ",city_pos)

dist = [[0 for j in range(city)] for i in range(city)]
for i in range(0,city):
    for j in range(0,city):
        dist[i][j]=abs(city_pos[j]-city_pos[i])

visite_all=(1<<city)-1

def travel_sales(mask,pos):
    if mask==visite_all:
        return dist[pos][0];
    ans=1000000
    for i in range(0,city):
        if (mask&(1<<i))==0:
            ans=min(ans,travel_sales(mask|(1<<i),i)+dist[i][pos])
    return ans;

print("Minimum Distance Travel To Complete Full Trip : ",travel_sales(1,0))