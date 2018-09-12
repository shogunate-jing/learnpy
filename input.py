
#message = input("tell me someting")
#print(message)

prompt = "Tell me someting."
prompt += "\nHow old are you?"
age = input(prompt)
if int(age) > 36:
    print("\nYou are old!")
else:
    print("\nTeenager.")
