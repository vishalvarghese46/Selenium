'''For lambda functions

+> Lambda function is a small anonymous function
+> A lambda function can take any number of arguments, but can only have one expression
lambda arguments : expression

You type the keyword lambda followed by zero or more inputs
Then you put ':' then, a single expression. This expression returns a value

'''
names = ["Vishal VArghese", "Ben Philip Thomas", "Bibin Varghese", "Lans Christopher", "Bibin Benny"]

names.sort(key=lambda names : names.split()[-1].lower())
print(names)


f = lambda firstName, lastName: firstName.strip().title()+" "+ lastName.strip().title()
print(f(" vaki", " mownusee"))


