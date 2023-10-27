loan_amount = int(input("insert loan ammount: "))
loan_term = int(input("insert loan term in months: "))
interest_rate = ( loan_amount / 100 ) * 5
total_payment = loan_amount + interest_rate
print ("you will have to pay" , total_payment / loan_term , "per month")