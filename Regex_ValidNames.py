import re

def validate_name(name):

    reg_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)

    res = reg_name.search(name)

    if res: print("valid")
    else: print("Invalid")

validate_name('Mrs. Tan')
validate_name('Su')
validate_name('Ms.Tan')
validate_name('Mr. Sirius black')