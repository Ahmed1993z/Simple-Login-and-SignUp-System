print('create your account ')
username = input('enter user username ')
password = input('enter user password ')
print('user'+username+' created successfully')
username1 = input('input username ')
if username1 == username:
    password1 = input('input password ')
    if password1 == password:
        print('User logged in successfully')
    else:
        print('password is incorrect')
else:
    print('username is incorrect')
