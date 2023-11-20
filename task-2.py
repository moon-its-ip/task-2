import base64
import my_api

message = base64.b64encode((text[::-2] + text[-2::-2]).encode('ascii')).decode('ascii')
my_api.send_message(message)
