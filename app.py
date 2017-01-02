import os
import sys
import json

import requests
from flask import Flask, request
from Vision import detect_face

#Flask is a web framework to develop python web apps
app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when we register a webhook, we need to verify the authenticity of the fb server
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == unicode(os.environ["VERIFY_TOKEN"]):
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

# endpoint for processing incoming messaging events
@app.route('/', methods=['POST'])
def webhook():
    imageCount=0
    facesCount=0
    videoCount=0
    audioCount=0
    fileCount=0
    message_text="NONE"
    
    
    data = request.get_json()
    log(data)  # logging incoming messages

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message
                    message=messaging_event.get("message")
                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person who sent the message
                    if message.get("text"):
                        message_text=message.get("text")
                    if message.get("attachments"):
                        for attachment in message.get("attachments"):
                            if attachment["type"]=="image":
                                imageCount=imageCount+1
                                faces= detect_face(attachment["payload"]["url"])
                                if faces is not None:
                                    for face in faces:
                                        facesCount=facesCount+1
                            if attachment["type"]=="audio":
                                audioCount=audioCount+1
                            if attachment["type"]=="video":
                                videoCount=videoCount+1
                            if attachment["type"]=="file":
                                fileCount=fileCount+1
        message_text="text:"+message_text+"\n"+"images:"+str(imageCount)+"\n"+"audio:"+str(audioCount)+"\n"+"video:"+str(videoCount)+"\n"+"file:"+str(fileCount)+"\n"+"faces:"+str(facesCount)
        send_message(sender_id, message_text)        

    return "ok", 200


def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
