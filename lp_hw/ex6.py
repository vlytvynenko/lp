#Let's calculate l_cp
#l_cp p/d
daily = 250
print("l_cp p/d", daily)
#l_cp p/m (working)
weeks = 4
days_per_week = 5
days = weeks * days_per_week
print("We have about", days, "working days per month")
#So per month should be around
month = daily * days
print("l_cp p/m", month)

#vac feb
f = 3
# days jan
j = 5
# remove jan and feb days
working = days - j - f
print("total in office", working, "days")
#Let's rechek how much they should give me
mw = working * daily
print("So", mw, "not bad")
#Let's compare
print("should be", 3000 >= mw )
