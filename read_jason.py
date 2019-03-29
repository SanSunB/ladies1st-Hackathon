import json

with open('data1.txt') as json_file:
    data = json.load(json_file)
    print("wanted job " + str(data['wanted_job']['job']))
    """
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
    """
