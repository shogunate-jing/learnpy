prompt = "\nTell me someting."
prompt += "\nEnter 'quit' to end the program."

'''
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print("\nThe program stoped")
'''

Active = True
while Active:
    message = input(prompt)
    if message == 'quit':
        Active = False
    else:
        print(message)

