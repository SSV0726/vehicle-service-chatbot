from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)


from twilio.rest import Client
account_sid = "AC6e37dc249eaf22ba5fd81743dd150d6e"
auth_token = "0efed2e4e2b99e0bb6912f0eb9fa51d1"



@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/share")
def share():
    reply = " Location Captured successfully !!"
    resp = MessagingResponse()
    # Create reply
    resp.message(reply)

    return "Location Shared Successfully , You can go back now "

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    print(phone_no , " => " , msg.lower()  )
    client = Client(account_sid, auth_token)
    
   
    if msg.lower() == "hi cubestop" :
       
        media_url = ('https://he-s3.s3.amazonaws.com/media/uploads/0ca15d3.png')
                
        msgBody = " Hi Sagar , Welcome to cubestop 1-stop Destination for all your need \n \n Visit : https://www.cubestop.com  "
        resp = MessagingResponse()
        mymsg =   resp.message(msgBody)
        mymsg.media(media_url)

        return str(resp)
    elif msg.lower() == "find nearest restaurant":
              
        print( "String Case matched !!")     
        
        msgBody = " Plz Click on the link to share your Location 📍 with Cube Stop .  \n \n Visit : http://751648d76e73.ngrok.io/share \n \n OR \n \n Share your thorugh whatsapp itself !! 😊 "
        resp = MessagingResponse()
        mymsg =   resp.message(msgBody)

        return str(resp)

    elif msg.lower() == "done":
              
        print( "String Case matched  = Done!!")     
        
        media_url = ('https://i.pinimg.com/736x/6a/fc/63/6afc63bf06c99262ad7efa4683f956b1.jpg')
                
        msgBody = " Hi Sagar , \n \n  We found the nearest cubestop to you  . \n  \n Click below link to Navigate : https://goo.gl/maps/vVwTX6p95fkpJFNp6  "
        resp = MessagingResponse()
        mymsg =   resp.message(msgBody)
        mymsg.media(media_url)

        return str(resp)

    elif msg.lower() == "great service":
              
        print( "String Case matched  = great service !!")     
        
        happy_url = ('https://www.futurenetzero.com/wp-content/uploads/2014/06/Smiley-face-emoticon-575.jpg')
                
        msgBody = " Thanks for the FeedBack . \n \n  We are happy to Help you . \n \n If you would like to recommed someone to visit cubestop just tell us their number and you will get a Free Service next Time !!   "
        resp = MessagingResponse()
        mymsg =   resp.message(msgBody)
        mymsg.media(happy_url)

        return str(resp)


    else:
        reply = fetch_reply(msg, phone_no)
        resp = MessagingResponse()
        # Create reply
        resp.message(reply)
        return str(resp)

    

if __name__ == "__main__":
    app.run(debug=True)