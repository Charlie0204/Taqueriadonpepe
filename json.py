import json

strings = []
data =  '{ "datetime": "2017-01-01 23:23:23", "request_id": "123-123-123", "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] }, { "part_id": "123-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  } ], "answer" : { "start_time": "", "end_date": "" [ { "step": 1, "state": "running", "action": "working on orden", "part_id": "123-123", "startTime": "", "endTime": "" }, { "step": 2, "state": "suspend", "action": "waiting for cheese", "part_id": "123-222", "start_time": "", "end_date": ""  }, { "step": 3, "state": "running", "action": "working on orden", "part_id": "123-222", "start_time": "", "end_date": ""  } ]}}'

with open("ordenes.json", 'w') as f:
    for i in range(5):
        f.write(data + "\n")
    f.close()
with open("ordenes.json", "r") as f:
    while True:
        line = f.readline()
        if line != '':
            strings.append(line[:-1])
            jsonorden = json.loads(data)
        else:
            break
    f.close()

 #para leer en diccionario el json
