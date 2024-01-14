# Here, I am making a time based two-factor authentication tool.
# first to import what I need -- the onetimepass package and whatever 2fa authenticator you prefer.
# Inspiration from Jothin Kumar

from onetimepass import valid_totp
from secrets import choice

# First, I am making a function to give a random string with a length of 16.
def generate_secret():
    secret = ''
    while len(secret) < 16:
        secret += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
    return secret

# Next, I create steps for the authenticator app. I am using Google's personally.

secret = generate_secret()
print('Enter the following secret in your authenticator app:', secret)
print("""Instructions for saving this secret it Google Authenticator:
1. Open Google Authenticator. 
2. Click plus icon at the right bottom.
3. Click Enter a setup key.
4. Enter an Account name of your choice and enter the secret provided above.
5. Click Add.""")
while True:
    otp = int(input('Please enter the otp generated by your authenticator app:'))
    authenticated = valid_totp(otp, secret)
    if authenticated:
        print('Correct otp, Authenticated!')
    elif not authenticated:
        print('Wrong otp, please try again.')