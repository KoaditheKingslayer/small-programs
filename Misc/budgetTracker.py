class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        # Calculate needed asterisks on each side
        asterisk_count = int((30 - len(self.category)) / 2)
        asterisks = '*' * asterisk_count
        # Create the Title Line, with category surrounded by asterisks.
        title_line = asterisks + self.category + asterisks
        # If there's one missing from rounding, add a last asterisk.
        if len(title_line) < 30:
            title_line += '*'
        full_output = ''
        full_output += title_line + '\n' # Add Title Line to Output
        count = 0
        for entry in self.ledger:
            desc = entry['description'][:23] # limit to 23 chars
            count += entry['amount']
            amount = f"{entry['amount']:>7.2f}" # max 7 chars, 2 dec places
            full_output += f"{desc:<23}{amount}\n"  # 30 char wide format
        # Output Category Total
        total_line = f"Total: {count:.2f}"
        full_output += f"{total_line}\n"  
        
        return full_output
 
    
    def deposit(self, amount, description=''):
        # Add the deposit to the ledger of the current (self) category.
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self, amount, description=''):
        # Verify funds, then add the amount as a negative number.
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})

    def get_balance(self, category=None):
        category = category if category else self
        balance = 0
        for entry in category.ledger:
            balance += entry['amount'] 
        return round(balance, 2)       

    def transfer(self, amount, category):
        category = category if category else self
        if category.check_funds(amount): # Transfer
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
    
        return amount <= balance 

def create_spend_chart(categories):
    pass
    # pass a list of categories
    # return a string that is a bar chart
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
food.deposit(12.22, 'Deposit')
food.withdraw(10, 'Groceries')
food.deposit(13.50, 'Deposit')
food.deposit(123.10, 'Charge-Back')
food.withdraw(100.00, 'Withdraw')
ent = Category('Entertainment')
ent.deposit(15.00, 'Netflix')
food.transfer(10, ent)

print(food)
print(ent)
print(food.get_balance())

