word = "hello"
print(word)
print(dir(word))
print(word.upper())

#String concatenation
name = "Maksim"
a = "Good day, {}"
result = a.format(name)
print(result)

first_name = "Yuliia"
last_name = "Zakirzhanova"
a = '{} {}'
result = a.format(first_name, last_name)
print("My names is : " + result)

result = f'{first_name} {last_name}'
print(result)

