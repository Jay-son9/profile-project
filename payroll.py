import pandas as pd

emp_list = []
num_emp = 0
fed_tax = .10
state_tax = .06
fica = .03

while len(emp_list) < 1:
    employee_name = input("Enter employee name")
    pay_rate = float(input("pay rate"))
    hours_worked = int(input("hours"))  #43
    regular_pay = 0
    overtime_pay = 0
    gross_pay = 0
    fed_tax_ded = 0
    state_tax_ded = 0
    fica_ded = 0
    net_pay = 0
    
    if hours_worked > 40:
        extra_hours = hours_worked - 40
        overtime = pay_rate * 1.5
        overtime_pay = overtime * extra_hours
        regular_pay = 40 * pay_rate
        gross_pay = regular_pay + overtime_pay
    elif hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay
    
    fed_tax_ded = gross_pay * fed_tax
    state_tax_ded = gross_pay * state_tax
    fica_ded = gross_pay * fica
    net_pay = gross_pay - (fed_tax_ded + state_tax_ded + fica_ded)
     #Employee Name    Hours Worked    Pay Rate      Regular Pay    OT Pay    Gross Pay   Fed Tax   State Tax FICA  Net Pay

    result = {"Employee Name":employee_name, "Hours Worked": hours_worked, "Pay Rate": pay_rate, "Regular Pay": regular_pay, "OT Pay": overtime_pay, "Gross Pay": gross_pay, "Fed Tax":fed_tax_ded, "State Tax": state_tax_ded, "FICA": fica_ded, "Net Pay": net_pay}
    emp_list.append(result)
    num_emp += 1
    

print(pd.DataFrame(emp_list).reindex(columns=['Employee Name','Hours Worked','Pay Rate', 'Regular Pay', 'OT Pay', 'Gross Pay', 'Fed Tax', 'State Tax', 'FICA', 'Net Pay']))

