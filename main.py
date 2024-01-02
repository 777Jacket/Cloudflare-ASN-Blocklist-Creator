# Reads the AS Numbers from the text file
with open('as_numbers.txt', 'r') as file:
    as_numbers = file.read().splitlines()

# Creates the Cloudflare WAF expression
expression = ' or '.join([f'(ip.geoip.asnum eq {asn})' for asn in as_numbers])

# Saves the expression to a text file
with open('expression.txt', 'w') as file:
    file.write(expression)

print(expression)
