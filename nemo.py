import aiml 
import time
import os
# Print Logo 
logo = """                      	
 | \ | |                       / ____| |         | | | |         | |  
 |  \| | ___ _ __ ___   ___   | |    | |__   __ _| |_| |__   ___ | |_ 
 | . ` |/ _ \ '_ ` _ \ / _ \  | |    | '_ \ / _` | __| '_ \ / _ \| __|
 | |\  |  __/ | | | | | (_) | | |____| | | | (_| | |_| |_) | (_) | |_ 
 |_| \_|\___|_| |_| |_|\___/   \_____|_| |_|\__,_|\__|_.__/ \___/ \__|"""

print(logo) 
                                                                     
nemo = aiml.Kernel()
for file in os.listdir("Nemo's_brain"):
	if file.endswith('.aiml'):
		nemo.learn("Nemo's_brain/"+file)
# nemo.learn('intro.aiml')
# nemo.learn('ai.aiml')
# nemo.learn('fun.aiml')
# nemo.learn('Business.aiml')
# neo.respond("load aiml b")

while True:
	query = raw_input("YOU :> ")
	if query.lower() == "stop":
		time.sleep(0.2)
		print('Ok Bye')
		time.sleep(1)
		print('Nice to chat You :) ')
		break
	else:	
		time.sleep(0.2)
		responce = nemo.respond(query)
		print("Neo:> {}".format(responce))		
