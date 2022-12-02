import json
from time import sleep

def running_test(obj):
    i = 0
    while(i < 50):
        if i % 3 == 0:
            obj.send(text_data=json.dumps({
                'message' : str(i)
                }))
        i += 1
        print(i)
        sleep(1)
