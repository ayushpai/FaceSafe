from py_imessage import imessage
import time

phone = "7274596857"



guid = imessage.send(phone, "Hello World!")

# Let the recipient read the message
time.sleep(5)
resp = imessage.status(guid)

print(f'Message was read at {resp.get("date_read")}')