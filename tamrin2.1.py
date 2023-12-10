data = [
 {'First Name': 'Raj', 'Last Name': 'Nayyar'},
 {'First Name': 'Suraj', 'Last Name': 'Sharma'},
 {'First Name': 'Karan', 'Last Name': 'Kumar'},
 {'First Name': 'Jade', 'Last Name': 'Canary'},
 {'First Name': 'Raj', 'Last Name': 'Thakur'},
 {'First Name': 'Raj', 'Last Name': 'Sharma'},
 {'First Name': 'Kiran', 'Last Name': 'Kamla'},
 {'First Name': 'Armaan', 'Last Name': 'Kumar'},
 {'First Name': 'Jaya', 'Last Name': 'Sharma'},
 {'First Name': 'Ingrid', 'Last Name': 'Galore'},
 {'First Name': 'Jaya', 'Last Name': 'Seth'},
 {'First Name': 'Armaan', 'Last Name': 'Dadra'},
 {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
 {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

def sortingnames(name): return (name['First Name'], name['Last Name'])

sorted_data = sorted(data, key=sortingnames)

for name in sorted_data: print(name)