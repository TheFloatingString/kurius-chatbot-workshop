import os
import requests
import random

def get_wit(user_input, auth_key):

	encoded_input = requests.utils.quote(user_input, safe='')

	headers =  {"Authorization": "Bearer "+os.getenv("AUTH_KEY")}
	wit_url = "https://api.wit.ai/message?v=20200530&n=8&q="+encoded_input

	response = requests.get(wit_url, headers=headers)

	return response
	
print("My name is superbot! Talk to me:)")
print()

emotions_dict = {"feel-happy": ["That's great!"], 
				"feel-sad": ["Hope you feel better!"], 
				"feel-surprised": ["Surprise!"],
				"not-recognized": ["I don't understand."]}

while True:
	user_input = input("User: ")
	response = get_wit(user_input, os.getenv("AUTH_KEY")).json()

	print()
	print(response)
	print()

	# define goodbye
	if response["traits"].get("wit$bye") is not None and response["traits"].get("wit$bye")[0]["confidence"] > 0.9:
		print("Goodbye!")
		break

	if response["traits"].get("wit$greetings") is not None and response["traits"].get("wit$greetings")[0]["confidence"] > 0.9:
		print("Hello there!")
			
	# define emotion response
	elif response.get("intents") is not None and response["intents"][0]["confidence"] > 0.9:
		intent = response["intents"][0]["name"]
		print(random.choice(emotions_dict[intent]))
	
	else:
		print(random.choice(emotions_dict["not-recognized"]))

	print()			
