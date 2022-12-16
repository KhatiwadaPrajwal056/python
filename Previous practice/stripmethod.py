# Strip method is used for removing sapaces in the text
name = '      Prajwal       '
dots = '......'
print(name + dots)
print(name.strip())   #Also lstrip & rstrip removes left and right spaces

#If there is spaces between the text as example below
text = '    praj   wal'   # we cannt remove spaces of middle so we use REPLACE
print(text.replace(' ',''))

# This strip is used in exercise 4
