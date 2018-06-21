import pyperclip
from datetime import datetime

message_set = set(['l', 'lm'])
confirm_set = set({'c', 'conf', 'confirm', 'confirmed'})
no_answer_set = set(['n', 'no', 'no ans'])
hung_up_set = set(['hung', 'hung up'])
help_set = set(['h', 'help'])

commands = {"Left message": message_set, "Confirm" : confirm_set, "No answer" : no_answer_set, "Hung up" : hung_up_set, "Help" : help_set}

while (True):
    output = datetime.now().strftime("%m/%d %H:%M")
    command = input('Enter interaction type: ').lower()
    if command in message_set:
        output += " Left message, gave Chris' phone number to confirm or cancel appointment"
    elif command in confirm_set:
        output += " Appointment confirmed"
    elif command in no_answer_set:
        output += " No answer"
    elif command in hung_up_set:
        output += " Hung up mid-call"
    elif command in help_set:
        for command in commands.keys():
            print('{} : {}'.format(command, commands.get(command)))

    
    pyperclip.copy(output)
    print('Copied: ' + output)