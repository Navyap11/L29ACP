charecter= (input("Enter a charecter: "))

if charecter.isalpha():
    print("Alphabet")
elif charecter.isdigit():
    print("Number")
else:
    print("neither number or alphabet")