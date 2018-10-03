income = {}
years = {'Rick':1970,'Carl':2000,'Susan':1968}

years2 = years.copy()

print("""Susan's birth year is""", years['Susan'])

years['Henry'] = 2004

del years2 ['Susan']


addressBook = [ betsyInfo, tomInfo,
                
                {'Name': 'Susan Fox', 
                 'Phone': 'x6553', 
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'},
                
                 {'Name': 'Jimmy Dean', 
                 'Phone': 'x6663', 
                 'Street': '1605 Grand Avenue',
                 'City': 'Minneanapolis',
                 'State': 'MN',
                 'Email': 'jdean@macalester.edu'},   
                 
                 {'Name': 'James Dean', 
                  'Phone': 'x773', 
                  'Street': '1605 Grand Avenue',
                  'City': 'Denver',
                  'State': 'CO',
                  'Email': 'jdean3@macalester.edu'}                 
                 
                 ]

def filterByCity (city, addressBook):
    for entry in adressBook:
        if 