import json         # javascript object notation

data1 = '{"Name": "Lorem Ipsum", "Address": "A-15, Dolor Sit Amet, Adipscing, Voluptatem, Gonzara"}'        # creating a json string

data_python = json.loads(data1)                          # parsing over the data to convert json string to python object (dictionary)
print(type(data_python))
print(data_python)
print('Name :', data_python['Name'])                    # printing name
print('Address :', data_python['Address'])              # printing address

print()

data2 = {'Name': 'Lorem Ipsum', 'Address': 'A-15, Dolor Sit Amet, Adipscing, Voluptatem, Gonzara'}  # creating a python object(dictionary)

data_json = json.dumps(data2)
print(data_json)
# data_json['Name']                                     # it will throw error here in python, but will work in js console