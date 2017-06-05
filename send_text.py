from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa6c6047d0fa3cf931c03c1f96eed3e5f"
# Your Auth Token from twilio.com/console
auth_token  = "6ea964d775c95faf322305dcdb294fad"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17376005308", # your phone number
    from_="+18175221474", # your Twilio number
    body="Hello from Trang :D I can send spam messages from my program now lol! Don't reply for now. I'm still playing.")

print(message.sid)
