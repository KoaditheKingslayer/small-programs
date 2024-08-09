class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        pass
        # display a title line of 30 chars
        # where the name of the category is
        # centered in a line of *'s.
        # display a list of items in the ledger.
        # each line shows description and
        # and the amount.
        # First 23 chars of the description
        # should be displayed, then the amount.
        # The amount should be right-aligned,
        # contain two decimal places, and 
        # show a maximum of 7 characters.
        # display a line displaying the 
        # category total. 
    
    def deposit(amount, descripton=''):
        pass
        # append an amount to the ledger list
        # as {'amount': amount, 'description': description}

    def withdraw(amount, description=''):
        pass
        # similar to deposit
        # amount passed should be stored 
        # in the ledger as a negative number
        # IF there are not enough funds, 
        # nothing should be added to the ledger.
        # must return True if the withdrawal
        # took place, and False otherwise.

    def get_balance(category):
        pass
        # returns current balance of the 
        # budget category based on deposits
        # and withdrawals that have occured.

    def transfer(amount, category):
        pass
        # add a withdrawal with the amount and
        # description 'Transfer to [Destination Budget Category]'
        # Then add a deposit to the target
        # budget category with the same amount
        # and the description
        # 'Transfer from [Source Budget Category]'
        # IF not enough funds, nothing should
        # be added to either ledger.
        # Return True if transfer took place.
        # Return False if not.

    def check_funds(amount, category):
        pass
        # returns False if the amount is 
        # greater than the balance of the 
        # budget category
        # returns True otherwise
        # should be used by both withdraw
        # and transfer 

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