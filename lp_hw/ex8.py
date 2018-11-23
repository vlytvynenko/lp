formatter = "{} {} {} {}" #Defined structure of formatter variable

#Creating new string based on formatter structure with a new data
print(formatter.format(1, 2, 3, 4))
#Creating new string based on formatter structure with a new data
print(formatter.format('one', 'two', 'three', 'four'))
#Creating new string based on formatter structure with a new data
print(formatter.format(True, False, False, True))
#Creating new string based on formatter structure with a formatter variable
print(formatter.format(formatter, formatter, formatter, formatter))

#New structure for the last string
formatter2 = "{}; {}; {}; {}!"
#printed new string based on formatter2 structure
print(formatter2.format(
     "Lya, lya, lya",
     "Zhu, Zhu, zhu",
     "Ti podprignizh",
     "Ya vsazhu"
))
