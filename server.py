# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def stus(mon):
#     for i in mon:
#         print i['first_name'], i['last_name']
# stus(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# def monkey(tuse):
#     for key in tuse:
#         # print tuse["Students"][3]['first_name']
#         for guess in range(len(tuse[key])):
#             a = tuse[key][guess]['first_name']
#             b = tuse[key][guess]['last_name']
#             print guess+1, '-', a, b, '-', len(a)+len(b)
# monkey(users)

def monkey2(wens):
    for key,value in wens.iteritems():
        # print key
        # print value[1]['first_name']
        for count in range(len(wens[key])):
            a = value[count]['first_name']
            b = value[count]['last_name']
            print count+1, '-', a, b, '-', len(a)+len(b)
monkey2(users)
# unpacks it for you.