a  = ''
b = 'lljk'
c = '12345'
d = ''
list1 = (a,b,c,d)


list2 = {'Name_Client':a,'Dob':b,'Gender':c,'City':d}
l = [(i,j) for i,j in list2.items() if filter(len, j)]
# for i in l:
#     print(i)
#     list2.pop(i)
# print(list2)
for j in l:
    print(j)
    # list2.pop(j)
print(list2)