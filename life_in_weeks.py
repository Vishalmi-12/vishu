#this code will help you to know how may days,weeks,months you have have left if your live 100 years
age = int(input('What is your age: '))
Days = ((100-age) * 365)
weeks = (100-age) * 52
month = (100-age) * 12
print(f'You have {Days} Days, {weeks} weeks , {month} months left')
