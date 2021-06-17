#module is basically a file containing set of functions to include in your app, you can add core python module or you can install using the pip

import datetime
import time 
from time import time


today = datetime.date.today()
timestamp = time()

print(timestamp)

import validate

from validate import validateEmail

email = 'test@test.com'
if validateEmail(email):
    print('email is valid')
else:
    print('not valid email')


