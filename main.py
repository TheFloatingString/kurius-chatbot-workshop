import os
import requests
import random

def get_wit(user_input, auth_key):

	encoded_input = requests.utils.quote(user_input, safe='')

	headers =  {"Authorization": "Bearer "+os.getenv("AUTH_KEY")}
	wit_url = "https://api.wit.ai/message?v=20200528&n=8&q="+encoded_input

	response = requests.get(wit_url, headers=headers)

	return response
	
print("My name is superbot! Talk to me:)")
print()

emotions_dict = {"feel-happy": "That's great!", 
				"feel-sad": "Hope you feel better!", 
				"feel-surprised": "Surprise!"}

while True:
	user_input = input("User: ")
	response = get_wit(user_input, os.getenv("AUTH_KEY")).json()

	# define goodbye
	if response["entities"].get("bye") is not None and response["entities"]["bye"][0]["confidence"] > 0.9:
		print("Goodbye!")
		break

	elif response["entities"].get("greetings") is not None and response["entities"]["greetings"][0]["confidence"] > 0.9:
		print("Hello there!")
			
	# define emotion response
	elif response["entities"].get("intent") is not None and response["entities"]["intent"][0]["confidence"] > 0.9:
		intent = response["entities"]["intent"][0]["value"]
		print(random.choice(emotions_dict[intent]))
	
	else:
		print(random.choice(emotions_dict["not_recognized"]))

	print()			
