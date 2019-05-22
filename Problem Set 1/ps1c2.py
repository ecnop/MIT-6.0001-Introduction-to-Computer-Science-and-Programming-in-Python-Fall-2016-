#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:51:44 2018

@author: carlosponce
"""

#These are the given parameters of the problem
portion_down_payment = 0.25
current_savings = 0
r = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
months = 36

annual_salary = float(input("Enter the annual salary: "))
annual_salary_base = annual_salary
savings_rate = 0.0
#savings_rate = 0.2     #Testing line


current_savings = 0.0
e = 100.0
#step = 0.00001
counter = 1

while (current_savings - portion_down_payment*total_cost) < 0:
    current_savings = 0
    annual_salary = annual_salary_base
    savings_rate = counter/10000
    for i in range(1,months+1):
        current_savings *= (1+r/12)
        current_savings += (annual_salary/12)*savings_rate
    #        print("current_savings =",current_savings,"annual_salary =",annual_salary)
        if i % 6 == 0:
            annual_salary *= (1+semi_annual_raise)
    if savings_rate > 1:
        break
    counter += 1
#    print("This is iteration", counter,"current_savings =",current_savings, "savings_rate =",savings_rate)
#    savings_rate += step

if savings_rate > 1:
    print("It is not possible to save for a downpayment given this salary")
else:
    print("The best savings rate is:",savings_rate)
    print("The difference between the current savings and the total cost of the home is:",portion_down_payment*total_cost - current_savings)
    print("The current savings are:",current_savings)
#print("The number of iterations is:",counter-1)  #testing line
#print("Your current savings are:",current_savings)   #testing line