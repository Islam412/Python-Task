'''
12. Build an email slicer : create a function that takes an email as input and retrieve the
username and domain of the email
'''
import itertools
import re
 
# Function to extract the domain names
def extract_domain(email):
    pattern = r"@([A-Za-z0-9.-]+)\."
    match = ''.join(list(itertools.dropwhile(lambda x: x != '@', email)))
    domain = re.findall(pattern, match)[0] + ".com"
    return domain
 
 
# Example Usage:
email = input('Enter e-mail: ')
 
# Print the original string
print("The original string is : " + str(email))
 
print("The extracted domain name : " + extract_domain(email))
 
