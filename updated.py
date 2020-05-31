import requests
import os
import json
import random

responses_dict = {
    "feel-happy": 
        ["That is great!", "Keep it up!", "You're a star"],
    "feel-sad":
        ["I hope you feel better soon", "I'm here to help"],
    "not-recognized":
        ["Hmmm I don't get it.", "Say it again?"],
    "bye":
        ["See ya!", "See you next time!"]
}

# loop until condition is met
while True:

    # receive user input
    user_input = input("User: ")

    if user_input == '':
        user_input = "."

    # send response to wit.ai 
    encoded_input = requests.utils.quote(user_input, safe='')

    headers = {"Authorization": "Bearer "+os.getenv("AUTH_KEY")}

    wit_url = "https://api.wit.ai/message?v=20200530&n=8&q="+encoded_input

    # print(encoded_input)
    # print(wit_url)

    response = requests.get(wit_url, headers=headers)

    processed_response = response.json()

    # print(response)
    # print(response.json())
    # print()
    # print(json.dumps(response.json(), indent=4))


    # select a relevant response

    # print(processed_response["intents"])
    # print(processed_response["intents"][0])
    # print(processed_response["intents"][0]["name"])
    # print(processed_response["intents"][0]["confidence"])

    emotion_name = processed_response["intents"][0]["name"]
    confidence_level = processed_response["intents"][0]["confidence"]

    # print(emotion_name)
    # print(confidence_level)

    # display chatbot output

    if processed_response["traits"]["wit$bye"] is not None and processed_response["traits"]["wit$bye"][0]["confidence"] > 0.9:
        list_of_responses = responses_dict["bye"]
        print(random.choice(list_of_responses))
        break

    if emotion_name == "feel-happy" and confidence_level > 0.8:
        list_of_responses = responses_dict[emotion_name]
        print(random.choice(list_of_responses))

    elif emotion_name == "feel-sad" and confidence_level > 0.8:
        list_of_responses = responses_dict[emotion_name]
        print(random.choice(list_of_responses))

    else:
        list_of_responses = responses_dict["not-recognized"]
        print(random.choice(list_of_responses)) 
