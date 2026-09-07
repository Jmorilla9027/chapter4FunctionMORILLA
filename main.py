def seatwork_03_get_employee_name():
    return input("Enter Employee Name: ")

def seatwork_03_get_employee_initials():
    return input("Enter Employee Initials: ")

def seatwork_03_get_hours_worked():
    return float(input("Enter Hours Worked: "))

def seatwork_03_get_hourly_rate_php():
    return float(input("Enter Hourly Rate (PHP): "))

def seatwork_03_compute_gross_pay_php(seatwork_03_hours_worked, seatwork_03_hourly_rate_php):
    if seatwork_03_hours_worked <= 40:
        return seatwork_03_hours_worked * seatwork_03_hourly_rate_php

    seatwork_03_overtime_time = seatwork_03_hours_worked - 40

    return (
        (40 * seatwork_03_hourly_rate_php)
        + (
            seatwork_03_overtime_time
            * seatwork_03_hourly_rate_php
            * 1.50
        )
    )

if seatwork_03_hours_worked <= 40:
        seatwork_03_gross_pay=  seatwork_03_hours_worked * seatwork_03_hourly_rate_php
else:
    seatwork_02_overtime_time=seatwork_03_hours_worked - 40
    seatwork_03_gross_pay =(40 * seatwork_03_hourly_rate_php) + (seatwork_02_overtime_time * seatwork_03_hourly_rate_php * 1.5)

if seatwork_03_gross_pay <=500:
    seatwork_03_tax_deduction = 0
elif seatwork_03_gross_pay <=1000:
    seatwork_03_tax_deduction = (seatwork_03_gross_pay - 500) * 0.10
else:
    seatwork_03_tax_deduction = 50 + (seatwork_03_gross_pay - 1000) * 0.20

seatwork_03_net_pay = seatwork_03_gross_pay - seatwork_03_tax_deduction



