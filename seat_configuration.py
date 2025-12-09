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

#Input your desired amount of simulation
simulation = 1000 #input your amount simulation here
valid = 0

#I want to input the result into data frame therefore we can call it again
result = []

#Simulation
while valid < simulation:       #This is to generate the desired result so it can loop back to simulation

#generate random value within the range for B
    f = random.randint(1,f_cap) 
#generate random value within the range for F
    b = random.randint(1,b_cap)

# This is the formula for Economy class
    e = math.ceil(max_cap - (1.8 * b) - (4.236 * f))  
#the desired results is >0

#if the results <0, it will not store the results
    if e > 0:
        valid += 1
        print(e, b, f)
