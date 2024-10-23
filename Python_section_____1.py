#Question 5: Find All Dates in a Text

import re

def find_all_dates(text):
    # Define the regex pattern for matching dates in the specified formats
    date_pattern = r'\b(\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2})\b'
    
    # Find all matching dates in the text
    matches = re.findall(date_pattern, text)
    
    return matches

# Example usage
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
output = find_all_dates(text)
print(output)  # Output: ['23-08-1994', '08/23/1994', '1994.08.23']
