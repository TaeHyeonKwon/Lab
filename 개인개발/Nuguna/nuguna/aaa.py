import email
import random



instaemail = Element("instaID")
instapw = Element("instaPW")
results = Element("result")

def play_game(*args):
    email = instaemail.value
    pw = instapw.value
    
    results.element.innerText = "{}".format(email)
    
    instaemail.clear()  
    instapw.clear()