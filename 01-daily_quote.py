#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    '"​​We will fail when we fail to try.” — Rosa Parks', 
    '"Youve got to get up every morning with determination if you’re going to go to bed with satisfaction.” — George Lorimer',
    '“The plan is to fan this spark into a flame.” — Lin-Manuel Miranda',
    '“Light tomorrow with today.” — Elizabeth Barrett Browning', 
    '“And now that you don’t have to be perfect, you can be good.” — John Steinbeck', 
    '“Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.” — Earl Nightingale', 
    '“A year from now you may wish you had started today.” — Karen Lamb', 
    '“You may not control all the events that happen to you, but you can decide not to be reduced by them.” — Maya Angelou'
    # Create a list of quotes here 
]

def get_quote_of_the_day(quotes):
    todays_quote = None
   
    # Your code here
    todays_quote = random.choice(quotes)

    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt