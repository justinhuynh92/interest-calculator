#collect the necessary inputs: principal, apr, years
#calculate the monthly payment
#show the user

def main():
    print('This is a monthly payment loan calculator')
    print('')

    #convert to floating piont numbers
    principal = float(input('Input the loan amount: '))
    apr = float(input('Input the annual interest rate: '))
    years = int(input('Input amount of years: '))

    #get interest rate by dividing 1200
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    #calculate monthly payments
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
