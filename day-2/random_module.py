import random

# value = random.random()
# value = random.uniform(1,10)
# value = random.randint(1,6)


greetings = ['Hello', 'Hi', 'hey', 'Howdy', 'Hola'] 
value = random.choice(greetings)

# print(value)
# print(value + ', World!')

colors = ['red', 'blue', 'green']
# results = random.choices(colors, k=10)   # k times repetation
results = random.choices(colors, weights=[18,18,2], k=10)  # red has 18 out of 38 chance of beings randomly selected  similarly for other
# print(results)



deck = list(range(1,53))  # only make list 
# random.shuffle(deck)        # shuffle the number
# print(deck)

hand = random.sample(deck, k=5)   # 5 ota unique value
# print(hand)


f_name= ['Ram', 'Shyam', 'Bishow', 'Bishal','Bikash','Aakash']
l_name= ['Pandey', 'Bhatta','Kumar','Poudel','Gyawali','Basnet']
age= random.randint(18,23)
phone = f'9{random.randint(7,8)}{random.randint(10000000,99999999)}'
h_name = ['Gulmi','Palpa','Kapil','Dang','Argha']

for num in range(10):   # 10 ota print garxa randomly
    first = random.choice(f_name)
    last = random.choice(l_name)
    home = random.choice(h_name)
    
    
    # print(f'{first}\n{last}\n{age}\n{phone}\n{home}\n')




# creating random phone number

phone = f'9{random.randint(7,8)}{random.randint(10000000,99999999)}'
# print(phone)


# creating random 4 digit otp
num = random.randint(1000,9999)
# print(num)

# creating random 6 digit otp
num = random.randint(100000,999999)
# print(num)