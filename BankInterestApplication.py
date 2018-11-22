# Account holder money input
account_holder_money = float(input("Enter account holder money: "))

# Account holder interest input
account_holder_interest = float(input("Enter interest rate: "))

# First year bank statement

first_year_interest = account_holder_money * account_holder_interest
first_year_total_money = first_year_interest + account_holder_money
print("Dear,\nhonourable client you will get " + str(first_year_interest) + " Taka in first year. ")
print("and you will get " + str(first_year_total_money) + " Taka in first year.\n ")

# Second year bank statement

second_year_interest = first_year_total_money * account_holder_interest
second_year_total_money = second_year_interest + first_year_total_money
print("your second year interest will be " + str(second_year_interest) + " Taka in second year. ")
print("and you will get " + str(second_year_total_money) + " Taka in second year.\n ")


# third year bank statement

third_year_interest = second_year_total_money * account_holder_interest
third_year_total_money = third_year_interest + second_year_total_money
print("your third year interest will be " + str(third_year_interest) + " Taka in third year. ")
print("and you will get " + str(third_year_total_money) + " Taka in third year.\n ")

# forth year bank statement

forth_year_interest = third_year_total_money * account_holder_interest
forth_year_total_money = forth_year_interest + third_year_total_money
print("your forth year interest will be " + str(forth_year_interest) + " Taka in forth year. ")
print("and you will get " + str(forth_year_total_money) + " Taka in forth year.\n ")

# fifth year bank statement

fifth_year_interest = forth_year_total_money * account_holder_interest
fifth_year_total_money = fifth_year_interest + forth_year_total_money
print("your fifth year interest will be " + str(fifth_year_interest) + " Taka in fifth year. ")
print("and you will get " + str(fifth_year_total_money) + " Taka in fifth year.\n ")
