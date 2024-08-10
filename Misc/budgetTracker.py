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
        '100|', '90|', '80|',
        '70|', '60|', '50|',
        '40|', '30|', '20|',
        '10|', '0|']

    category_amount = {}
    chart_total = 0 # Total to draw Percentage Comparison
    for category in categories:
        running_total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                running_total += entry['amount']
                #print(category.category, entry['amount'])
        category_amount[category.category] = running_total
        #print(f"{category.category}: {running_total}")
        chart_total += running_total

    # Percentage Calculation, Round Down (convert to Int)
    percentage = [] # Each item is a percentage
    for category in categories:
        percentage.append((int((category_amount[category.category] / chart_total) * 100)))
    # Each individual percentage
    for i in range(len(percentage)):
        print((percentage[i] // 10) * 10)
    #print(f'Chart Total: {chart_total}')


    return bar_chart  # return string

    # chart should show the percentage spent
    # in each category passed in the function.
    # The percentage spent should be calculated
    # only with withdrawals, not deposits.
    # Down the left side of the chart should be
    # labels 0 - 100.
    # the 'bars' in the bar chart should be 
    # made out of the 'o' character. The 
    # height of each bar should be rounded down
    # to the nearest 10. 
    # The horizontal line below the bars
    # should go two spaces past the final bar. 
    # Each category name should be written
    # vertically below the bar.
    # There should be a title at the top that 
    # Says 'Percentage spent by category.'
    # This function will be tested with up to 
    # four categories.

food = Category('Food')
ent = Category('Entertainment')
medical = Category('Medical')
ledgers = [food, ent, medical]
food.deposit(12.22, 'Deposit')
food.withdraw(10, 'Groceries')
food.deposit(13.50, 'Deposit')
food.deposit(123.10, 'Charge-Back')
food.withdraw(100.00, 'Withdraw')
ent.deposit(15.00, 'Netflix')
food.transfer(10, ent)
ent.transfer(20, food)
medical.deposit(1000, 'FSA Deposit')
medical.deposit(120, 'Medicaid')

# for ledger in ledgers:
#    print(ledger)

print(create_spend_chart(ledgers))