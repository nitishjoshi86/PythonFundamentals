#custom module to be imported

import re

def validateEmail(email):
    if len(email) > 7:
        return bool(re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email))

