#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:51:44 2018

@author: carlosponce
"""

#These are the given parameters of the problem
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
total_cost = 1000000.0
semi_annual_raise = 0.07
months = 36
cost_downpayment = total_cost*portion_down_payment

#Input the annual salary and set the base salary as the salary that was typed
annual_salary = float(input("Enter the starting salary: "))
annual_salary_base = annual_salary


current_savings = 0.0
e = 100.0
steps = 10000
counter = 1

LowerBound = 0
HigherBound = 1

savings_rate = (LowerBound+HigherBound)/2

# This is how it was intended to be solved

for i in range(steps):
    if abs(current_savings - cost_downpayment) <= e:
        break
    annual_salary = annual_salary_base
    current_savings = 0
    for i in range(1,months+1):
        current_savings *= (1+r/12)
        current_savings += (annual_salary/12)*savings_rate
        if i % 6 == 0:
            annual_salary *= (1+semi_annual_raise)
    if current_savings < cost_downpayment:
        LowerBound = savings_rate
    else:
        HigherBound = savings_rate
    savings_rate = (LowerBound+HigherBound)/2
    counter += 1

if abs(current_savings - cost_downpayment) <= e:
    print("Best savings rate:", savings_rate)
    print("Steps in bisection search:", counter)
    print(current_savings)
else:
    print("It is not possible to save for the down payment in 36 months.")


#
#while abs(portion_down_payment*total_cost - current_savings) > e:
#    current_savings = 0.0
#    annual_salary = annual_salary_base
#    for i in range(1,months+1):
#        current_savings *= (1+r/12)
#        current_savings += (annual_salary/12)*savings_rate
##        print("current_savings =",current_savings,"annual_salary =",annual_salary)
#        if i % 6 == 0:
#            annual_salary *= (1+semi_annual_raise)
#    counter += 1
#    if current_savings < portion_down_payment*total_cost:
#        LowerBound = savings_rate
#    else:
#        HigherBound = savings_rate
##    print("This is iteration", counter,"current_savings =",current_savings, "savings_rate =",savings_rate)
#    savings_rate = (LowerBound+HigherBound)/2
#
#if savings_rate > 1:
#    print("It is not possible to save for a downpayment given this salary")
#else:
#    print("The best savings rate is:",savings_rate)
#    print("The difference between the current savings and the total cost of the home is:",portion_down_payment*total_cost - current_savings)
#    print("\nThe number of iterations on the savings rate to get the answer was:",counter+1)