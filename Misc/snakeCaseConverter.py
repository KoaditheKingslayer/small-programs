# Completed on 7/18/2024 as part of: Scientific Computing with Python (beta) - FreeCodeCamp 
# Learn Python List Comprehension by Building a Case Converter Program

def convert_to_snake_case(pascal_or_camel_cased_string):
    # List comprehension below: Evaluation -> Condition -> Iterate
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('WhatInTheWorldAreYouDoing'))

main()