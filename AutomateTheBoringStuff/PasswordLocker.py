#! python3
# Pasword locker - An insecure password locker program

paswords = {'email' : 'jrfkjjsdfjQasadasd',
            'fb' : 'fdpkgpokdfpgpfedg',
            'snap' : 'dsfsdfqwewqde'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python PasswordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in paswords:
    pyperclip.copy(paswords[account])
    print('Password for {} copied to clipboard'.format(account))
else:
    print('There is no account named '+  account)