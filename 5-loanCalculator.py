# Input loan amount, interest rate, and loan term
loan_amount = 100000
interest_rate = 0.05
loan_term = 10

# Calculate monthly payment using the formula for calculating EMI (Equated Monthly Installment)
r = interest_rate / 12  # Monthly interest rate
n = loan_term * 12  # Total number of monthly payments
emi = (loan_amount * r * (1 + r)**n) / (((1 + r)**n) - 1)

# Display monthly payment
print(f'Your monthly payment for a loan amount of ${loan_amount:.2f} with an interest rate of {interest_rate * 100}% for {loan_term} years is: ${emi:.2f}')

# Provide functionalities such as working with user inputs, basic financial calculations,
# and display of loan amortization schedule
# ... (implement additional functionalities as needed)
