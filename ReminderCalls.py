import pyperclip
from datetime import datetime

message_set = set(['l', 'lm'])
confirm_set = set({'c', 'conf', 'confirm', 'confirmed'})
cancel_set = set(['can', 'canc', 'cancel'])
no_answer_set = set(['n', 'no', 'no ans'])
hung_up_set = set(['hung', 'hung up'])
help_set = set(['h', 'help'])
text_set = set(['t', 'text', 'txt'])

commands = {"Left message": message_set, "Confirm" : confirm_set, "No answer" : no_answer_set, "Hung up" : hung_up_set, "Help" : help_set, "Cancel" : cancel_set, "Text" : text_set}

def getnote(command):

    output = datetime.now().strftime("%m/%d %I:%M %p ~ ")
    if command in message_set:
        output += "Left message, gave Chris' phone number to confirm or cancel appointment"
    elif command in confirm_set:
        output += "Appointment confirmed"
    elif command in no_answer_set:
        output += "No answer"
    elif command in hung_up_set:
        output += "Hung up mid-call"
    elif command in text_set:
        output += "Confirmation text sent"
    elif command in help_set:
        for command in commands.keys():
            print('{} : {}'.format(command, commands.get(command)))

    
    return output

if __name__ == '__main__':
    while (True):
        command = input('Enter interaction type: ').lower()
        
        output = getnote(command)
        pyperclip.copy(output)
        print('Copied: ' + output)