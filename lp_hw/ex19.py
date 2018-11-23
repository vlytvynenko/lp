#Defind function name which take 2 arguments and print them out
def chees_and_crackers(chees_count, boxes_of_crackers):
    print("You have %d cheeses!" %(chees_count))
    print("You have %d boxes of crackers!" %(boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#Adding arguments in parenthesins directly
print("We can just give the function numbers directly.")
chees_and_crackers(20, 30)

#Call function and pass value via variables
print("OR, we can use variable from out script.")
amount_of_chees = 10
amount_of_creckers = 50
chees_and_crackers(amount_of_chees, amount_of_creckers)

#made math in parenhesis of function
print("We can even do math inside to!")
chees_and_crackers(10 + 20, 5 + 6)

# take variablse and made math in parenthesin
print("And we can combinate variables and math!")
chees_and_crackers(amount_of_chees + 100, amount_of_creckers + 1000)
