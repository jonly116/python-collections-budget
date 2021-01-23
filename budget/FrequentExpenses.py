from . import Expense
import collections

expense = Expense.Expenses()
expense.read_expenses('data/spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)


spending_counter = collections.Counter(spending_categories)

print(spending_counter)

top5 = spending_counter.most_common(5)