balance = 3000

def buy_things(item, price):
    dream_phone = 'xphone'
    global balance
    print(f'previous balance value ', balance)
    #balance = 500
    balance = balance - price
    print(f'blance after buying {item}', balance)
# print(dream_phone)
buy_things('sunglass', 1000)    
print('global balance after buy', balance)
