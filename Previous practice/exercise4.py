name , charater = input('enter your name and any character of your name(comma separated): ').split(',')
print(len(name))
pk = name.lower()
pkk = charater.lower()
print(pk.count(pkk))        #or print(name.lower().count(charater.lower()))
        
'''
If there is spaces in the text,then
'   Text   '----> 'Text'----> 'text'
'     T    '---->   'T'---->  't'
'''
print(name.strip().lower().count(charater.strip().lower))


