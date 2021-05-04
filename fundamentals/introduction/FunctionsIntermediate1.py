x = [ [5,2,3], [10,8,9] ] 
# x[1][0] = 15
#print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# students[0]['last_name'] = 'Bryant'
# print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in students:
        list = ''
        for (f, l) in i.items():
            list += f"'{f}, {l}'"
        print(list)
iterateDictionary(students)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        for (f, l) in i.items():
            if f == key_name:
                print(l)
iterateDictionary2('first_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for (l, p) in dojo.items():
        length = len(p)
        print(f"{length} {l}")
        for a in p:
            print(a)
printInfo(dojo)
