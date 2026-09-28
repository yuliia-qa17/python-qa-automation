#Converting characters to uppercase
message = "hello, world!"
upper_message = message.upper()
print(upper_message)

#Converting a string to title case
titled_message = message.title()
print(titled_message)

#Checking for numeric values in a string
num = "12345"
print(num.isdigit())
num_2 = "123asd"
print(num_2.isdigit())

#Check for prefix content
text = "Hello, everybody"
result = text.startswith("Hel")
print(result)
result = text.startswith("Hia")
print(result)
result = text.endswith("ody")
print(result)
result = text.endswith("ody!")
print(result)

#Checking for the presence of a substring in a string
var = "Hi, Guy"
var_index = var.find("Guy")
print(var_index)
var_index = var.find("guy")
print(var_index)

#Substring extraction
text = "Привет, мир!"
substring = text[0:6]
print(substring)

#Extraction from the end of the string
text = "Привет, мир!"
last_word = text[-4:]
print(last_word)

#Using the step
text = "Привет, мир!"
every_second_char = text[::2]
print(every_second_char)

#Modifying a string using slices
text = "Привет, мир!"
modified_text = text[:8] + "все!"
print(modified_text)

#Reverse string
text = "Привет, мир!"
reversed_text = text[::-1]
print(reversed_text)
