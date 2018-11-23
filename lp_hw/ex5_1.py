name = 'Viktor'
age = 25 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches = 2.54 #cm
pound = 0.453592 #kg

heinght_sm = height * inches
weight_kg = weight * pound

print("Let's talk about {}.".format(name))
print("He's {} inches tall.".format(height))
print("Thats equal {} cm".format(heinght_sm))
print("He's {} pound havy.".format(weight))
print("Thats equal {} kg".format(weight_kg))
print("Actually that's not so have.")
print("He's got {} eyes and {} hair.".format(eyes, hair))
print("He's teeth are usually {} dependings on the cofee.".format(teeth))

#This line are tricki try to get this exactly right

total = age + height + weight
print("If I add {}, {}, and {} I get {}.".format(age, height, weight, total))
