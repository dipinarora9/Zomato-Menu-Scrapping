from bs4 import BeautifulSoup
import csv

f = ''' '''

data = BeautifulSoup(f, 'html.parser')

headings = data.find('div', attrs={'class': 'ui secondary pointing menu o2_nav_bar'}).text

subcategories = data.find('div', attrs={'class': 'menu-container'}).text
head = data.find_all('div', attrs={'class': 'category_heading'})

b = []
for i in subcategories.split('Add'):
    b.extend(i.split('customizations available'))
m = []
for i in b:
    m.extend(i.split('₹'))
f = []
e = []
a = 0
for i in m:
    if a == 3:
        e.append(f)
        f = list()
        f.append(i)
        a = 1
    else:
        f.append(i)
        a += 1

# for i in e:
#     # writer.writerow(i)
#     print(i)

w = data.find_all('div', attrs={'class': 'ui divided items mbot0 category'})

da = []
for i in w:
    da.extend(i.text.split('₹'))
pa = []
for i in da:
    pa.extend(i.split('Add'))
ma = []
for i in pa:
    ma.extend(i.split('customizations available'))

extra = []
a = 0
e = []
f = []
num = 0
for i in ma:
    if i == '':
        continue
    elif a == 3:
        e.append(f)
        f = list()
        f.append(i)
        a = 1
    # elif (a==1 and i.isdigit()):
    #     extra.append(f'{num} {i}')

    else:
        f.append(i)
        a += 1
    num += 1
csv_file = open('data.csv', 'w', newline='')

writer = csv.writer(csv_file, )
# writer.writerow(['name','price','des'])
writer.writerow(['Main Category', 'Sub Category', 'Name', 'Description', 'Variant Group Name', 'Price', 'Veg_egg_non',
                 'Packing Charges', 'Spicy', 'Photos available', 'Typing  Error'])
final = ['Main Category', 'Sub Category', 'Name', 'Description', 'Variant Group Name', 'Price', 'Veg_egg_non', '', 0,
         'No', 'No']
nonveg = ['nonveg', 'chicken', 'non-veg', 'non - veg', 'non veg']
for i in e:
    spicy = 0
    cat = 'Veg'
    # if (i[0].lower().find('spicy')!=-1 or i[1].lower().find('spicy')!=-1 or i[2].lower().find('spicy')!=-1):
    #     spicy=1
    # if ():
    #     cat=
    # writer.writerow(i)

# def check
