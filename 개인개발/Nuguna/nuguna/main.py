import random



number_input = Element("number_input")
results = Element("result")


def play_game(*args):
    user_guess = number_input.value
    machine_guess = random.randint(1,50)
    if int(user_guess) == machine_guess:
        results.element.innerText = "You Win!"
    else:
        results.element.innerText = f"you lost! The machine chose {machine_guess}!"
    
    number_input.clear()    