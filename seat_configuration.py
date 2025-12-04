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
E_seat = int(input("Input Maximum Economy Seat: "))
B_seat = int(input("Input Maximum Business Seat: "))
F_seat = int(input("Input Maximum First Seat: "))
Max_Seat = E_seat
print("Max Capacity: ", Max_Seat)

#Input the ticket price
print("-INPUT TICKET PRICE-")
E_Ticket = int(input("E Ticket ($): "))
B_Ticket = int(input("B Ticket ($): "))
F_Ticket = int(input("F Ticket ($): "))

#Input how many simulation needed
simulation = 1000
valid = 0

#The result will be store here
result = []

#Let's put the condition here. I want it to only generate the E>0 because it is the valid condition
while valid < simulation:

#Generate random seat capacity for Business and First class
    F = random.randint(1,F_seat)
    B = random.randint(1,B_seat)
#Generate the Economy Seat
    E = math.ceil(Max_Seat - (1.849617185 * B) - (4.497744588 * F))
#If the E < 0 it will redo again
    if E > 0:
        valid += 1
#Calculate the total revenue for each option
        revenue = (E * E_Ticket) + (B * B_Ticket) + (F * F_Ticket)

        result.append((E, B, F, revenue))
        
#Showing the top 5 option
df = pd.DataFrame(result, columns=["E", "B", "F", "Revenue"])
top5 = df.sort_values("Revenue", ascending=False).head(5)
print(top5)