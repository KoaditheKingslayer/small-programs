class Category: 
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        # Title line: centered category name surrounded by asterisks, total length 30 characters
        asterisk_count = int((30 - len(self.category)) / 2) 
        asterisks = '*' * asterisk_count
        title_line = asterisks + self.category + asterisks
        if len(title_line) < 30:
            title_line += '*'
        
        # Ledger entries: description (23 chars), amount (7 chars, right-aligned)
        full_output = title_line + '\n'
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amount = f"{entry['amount']:>7.2f}"
            full_output += f"{desc}{amount}\n"
        
        # Total line: right after ledger entries
        total = self.get_balance()
        total_line = f"Total: {total:.2f}"
        full_output += total_line
        
        return full_output 
    
    def deposit(self, amount, description=''):
        # Add the deposit to the ledger of the current (self) category.
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self, amount, description=''):
        # Verify funds, then add the amount as a negative number.
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self, category=None):
        category = category if category else self
        balance = 0
        for entry in category.ledger:
            balance += entry['amount'] 
        return round(balance, 2)       

    def transfer(self, amount, category):
        category = category if category else self
        if self.check_funds(amount): # Transfer
            self.withdraw(amount, description=f'Transfer to {category.category}')
            category.deposit(amount, description=f'Transfer from {self.category}')
            return True
        else: # No Transfer
            print("Transfer unsuccessful")
            return False

    def check_funds(self, amount, category=None):
        # Use the specified category or default to self
        category = category if category else self
    
        balance = 0
        for entry in category.ledger:
            balance += entry['amount']
        if amount <= balance:
            return True 
        else: 
            return False

def create_spend_chart(categories):
    title = 'Percentage spent by category'
    bar_chart = title + '\n'
    labels = [
        '100', ' 90', ' 80',
        ' 70', ' 60', ' 50',
        ' 40', ' 30', ' 20',
        ' 10', '  0']

    category_amount = {}
    chart_total = 0
    for category in categories:
        running_total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                running_total += -entry['amount']
        category_amount[category.category] = running_total
        chart_total += running_total

    percentage = [int((category_amount[cat.category] / chart_total) * 100) for cat in categories]
    f_percentages = [(p // 10) * 10 for p in percentage]

    # Initialize the bar chart rows
    label_string = ['' for _ in range(len(labels))]
    dashes = '    ' + '-' * (len(categories) * 3 + 1)

    for i, label in enumerate(labels):
        label_string[i] = f"{label:>3}|"
        for p in f_percentages:
            if p >= int(label):
                label_string[i] += ' o '
            else:
                label_string[i] += '   '
        label_string[i] += ' \n'  # Adding space and newline

    bar_chart += ''.join(label_string) + dashes + '\n'

    # Prepare to add category names below the chart
    max_name_length = max(len(category.category) for category in categories)
    category_names = [category.category.ljust(max_name_length) for category in categories]

    # Add Category Names
    for i in range(max_name_length):
        name_line = '    '
        for name in category_names:
            if i < len(name):
                name_line += f" {name[i]} "
            else:
                name_line += '   '
        # Ensure there is a newline character and avoid extra spaces
        bar_chart += name_line.rstrip() + '\n'

    return bar_chart

# Test Output 
food = Category('Food')
ent = Category('Entertainment')
other = Category('Other')
medical = Category('Medical')
toy = Category('Toys')
toy.deposit(40, 'Deposit for Fun')
other.deposit(1000, 'Deposit')
other.transfer(80, ent)
food.deposit(12.22, 'Deposit')
food.withdraw(10, 'Groceries')
food.deposit(13.50, 'Deposit')
food.deposit(123.10, 'Charge-Back')
food.withdraw(100.00, 'Withdraw')
ent.deposit(15.00, 'Netflix Refund')
ent.withdraw(25, 'Movie Night')
food.transfer(10, ent)
ent.transfer(20, food)
medical.deposit(1000, 'FSA Deposit')
medical.deposit(120, 'Medicaid')
ledgers = [food, ent, medical, other, toy]

for ledger in ledgers:
    print(ledger)
print(create_spend_chart(ledgers))