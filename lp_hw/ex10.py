#Checking some escape symbols
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
#ESCAPE sequences the rest symbols
Single_quote = "Test \'single quote"
double_quotes = "Test \"double quotes"
ASCII_BELL = "ascii \abell"
ASCII_backspace = "ascii \bbackspace"
ASCII_formatter = "ascii \fformating"
ASCII_linefeed = "ascii \nlinefeed"
ASCII_UC_only = "Character named name in the Unicode /N{name} databes"
ASCII_CR = "ascii \rcarriage return"
ASCII_VT = "vertical \ttab"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fisies
\t* Catpin\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(Single_quote)
print(double_quotes)
print(ASCII_BELL)
print(ASCII_backspace)
print(ASCII_formatter)
print(ASCII_linefeed)
print(ASCII_UC_only)
print(ASCII_CR)
print(ASCII_VT

#Here’s a tiny piece of fun code to try out

while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i,)
