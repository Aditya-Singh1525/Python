items = []
ask_user = input("How many items do you wanna store in the list:")
if ask_user.isdigit():
    ask_user = int(ask_user)
else:
    print(ValueError('Invalid Input! The value should be a number. Default value is 5.'))
    ask_user = 5
for i in range(0,ask_user):
    ask_user_values = input('Enter the items to store:')
    items.append(ask_user_values)
if items:
    print(f"\nThere are {len(items)} items in the list:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")
else:
    print("\nThe list is empty.")
