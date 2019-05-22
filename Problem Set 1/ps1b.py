#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:41:36 2018

@author: carlosponce
"""

portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary = float(input("Enter the annual salary: "))
portion_saved = float(input("Enter the portion of the salary to be saved as a decimal percentage: "))
total_cost = float(input("Enter the total cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual salary rise as a decimal percentage: "))

months = 0

while (current_savings < portion_down_payment*total_cost):
    current_savings *= (1+r/12)
    current_savings += (annual_salary/12)*portion_saved
    months += 1
    if months % 6 == 0:
        annual_salary *= (1+semi_annual_raise)

print("The total months needed to save for your downpayment is:",months)
print("Your current savings are: ",int(current_savings))

