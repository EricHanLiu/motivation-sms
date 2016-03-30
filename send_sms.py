import sys
import requests
import conf
from twilio.rest import TwilioRestClient 

client = TwilioRestClient(conf.ACCOUNT_SID, conf.AUTH_TOKEN) 

default_message = "Eroc you are so cool!"
message = sys.argv[1] if len(sys.argv) > 1 else default_message

client.messages.create(
    to=conf.TO, 
    from_=conf.FROM, 
    body=message,  
)
