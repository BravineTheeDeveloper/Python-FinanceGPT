# Import necessary libraries
import matplotlib.pyplot as plt

# Input income, expenses, and savings
income = 5000
expenses = [1000, 200, 300, 400]  # Example list of expenses
savings = 0

# Calculate total expenses and savings
total_expenses = sum(expenses)
savings = income - total_expenses

# Display income, expenses, and savings in a pie chart
labels = ['Income', 'Expenses', 'Savings']
values = [income, total_expenses, savings]
colors = ['green', 'red', 'blue']
plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Budget Tracker')
plt.show()

# Provide functionalities such as data input/output, basic financial calculations,
# and visualization as needed
# ... (implement additional functionalities as needed)
