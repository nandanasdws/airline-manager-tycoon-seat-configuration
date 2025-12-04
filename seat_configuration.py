import pandas as pd
import numpy as np
import random
import math

#Header
print ("===AIRPLANE SEAT CONFIGURATION===")
print("--MAXIMUM SEAT INPUT--")

#Input the airplane Information
airplane_name = input("Input Airplane Name: ")
route = input("Input Your Route: ")

#Input the maximum capacity for the airplane
e_seat = int(input("Input Maximum Economy Seat: "))
b_seat = int(input("Input Maximum Business Seat: "))
f_seat = int(input("Input Maximum First Seat: "))
max_seat = e_seat
print("Max Capacity: ", max_seat)

#Input the ticket price
print("-INPUT TICKET PRICE-")
e_Ticket = int(input("E Ticket ($): "))
b_Ticket = int(input("B Ticket ($): "))
f_Ticket = int(input("F Ticket ($): "))

#Input how many simulation needed
simulation = 1000
valid = 0

#The result will be store here
result = []

#Let's put the condition here. I want it to only generate the E>0 because it is the valid condition
while valid < simulation:

#Generate random seat capacity for Business and First class
#I prioritize B and F seat first than try to calculate the E seat because it has the most space of all
    f = random.randint(1,f_seat)
    b = random.randint(1,b_seat)

#Generate the Economy Seat
#The formula is based on the average seat gap between each airplane
    e = math.ceil(max_seat - (1.849617185 * b) - (4.497744588 * f))

#If the E < 0 it will redo again
    if e > 0:
        valid += 1
#Calculate the total revenue for each option

        revenue = (e * e_Ticket) + (b * b_Ticket) + (f * f_Ticket)

        result.append((e, b, f, revenue))
        
#Showing the top 5 option
df = pd.DataFrame(result, columns=["E", "B", "F", "Revenue"])
top5 = df.sort_values("Revenue", ascending=False).head(5)
print(top5)
