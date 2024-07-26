Date_of_Purchase = int(input('How many days ago have you purchased the item? '))
item_status = input('Have you used the item at all [y/n]? ' )
condition_of_item = input('Has the item broken down on its own [y/n]? ')

if ((Date_of_Purchase <=10 and item_status == 'n') or condition_of_item == 'y'):
    print('You can get a refund')
else:
    print('You cannot get a refund')