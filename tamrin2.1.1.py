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

def sort_data(data):
    n = len(data)

    for i in range(n):
        
        for j in range(0, n-i-1):

            if compare(data[j], data[j+1]) > 0:
                data[j], data[j+1] = data[j+1], data[j]

def compare(item1, item2):
    first_name_compare = (item1['First Name'].lower() > item2['First Name'].lower()) - (item1['First Name'].lower() < item2['First Name'].lower())
    if first_name_compare == 0:
        return (item1['Last Name'].lower() > item2['Last Name'].lower()) - (item1['Last Name'].lower() < item2['Last Name'].lower())
    return first_name_compare

sort_data(data)

print(data)