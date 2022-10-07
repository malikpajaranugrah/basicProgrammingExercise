name = input("Your name: ")
Class = input("Your class: ")
major = input("Your major: ")
quote = input("Your quote: ")
age = int(input("Your age: "))
ilikespicefood = bool(input("i like spice food: "))

if ilikespicefood == "y":
      ilikespicefood = bool(True)
elif ilikespicefood == "n":
      ilikespicefood = bool(False)
else:
      print("wrong input")
hobbies = input("Hobbies: ").split(',')
print("="*30)
print(f"My name is: {name}\nClass: {Class}\nMajor: {major}\nQuote: {quote}\nAge: {age}\n"
      f"I Like Spice Food: {ilikespicefood}\nHobbies: {hobbies}")

print("="*30)
print("name: ",type(name))
print("class: ",type(Class))
print("major: ",type(major))
print("quote: ",type(quote))
print("age ",type(age))
print("i like spice food ",type(ilikespicefood))
print("hobbies ",type(hobbies))


