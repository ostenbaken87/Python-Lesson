x = 'some long and awesome TEXT'
print(len(x))
print(x[len(x)-1])
print(x.count('o'))
print(x.find('T'))

print(x.capitalize())
print(x.upper())

print(x.lower())

upper_cased = x.upper()
lower_cased = x.lower()

print(upper_cased)

print(upper_cased.isupper())
print(lower_cased.islower())

print(x.isupper())

x = str('hello')
print(x.startswith('he'))
print(x.endswith('lo'))

solit = x.split('l')
print(type(solit))
print(solit)

some_data = '4;8;15;16;23;42'
separeted_data = some_data.split(';')
print(separeted_data)
print(separeted_data[4])



