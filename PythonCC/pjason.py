#json is commonly used with data apis, parse json into a python dict

import json

userjson = '{"firstname":"nitish","lastname":"joshi","age":35}'

#parsing
user = json.loads(userjson)

print(user)
print(user['firstname'])

car = {'make':'honda','model':'civic','year':2007}
carjson=json.dumps(car)
print(carjson)