from twilio.rest import Client

# User information is hidden in private-information.txt (gitignored file)
# Your Account SID from twilio.com/console
# Your Auth Token from twilio.com/console

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+31613925045", #My Number
    from_="+3197014201108", #My Twilio Number +3197014201108

    body="Groetjes van de SMS bot van Arie!")

print(message.sid)

# It worked!
