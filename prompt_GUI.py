#Libraries
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import PySimpleGUI as sg
import datetime as time

#key
openai.api_key="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"
key="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"

# Choose a Theme for the Layout
sg.theme('DarkPurple4')
# Define the window's contents
layout = [[sg.Text("Enter Prompt:",font='Calibri')],
          [sg.Multiline(key='-INPUT-',size=(50,2),autoscroll=True,font='Calibri')],
          [sg.Text("Output:",font='Calibri')],
          [sg.Multiline(size=(50,10), key='-OUTPUT-',autoscroll=True,font='Calibri')],
          [sg.Button('Send',font='Calibri'), sg.Button('Quit',font='Calibri'),sg.Button('Save Response',font='Calibri')]]

# Create the window
window = sg.Window('Ada-001', layout,resizable=True)

#Instantiate ada:
llm = OpenAI(model_name="text-ada-001",openai_api_key=key)
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    now=time.datetime.now()
    now=str(now)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if  event == 'Save Response':
        with open('C:/GitHub_repos/Numbskulls/Ada_outputs.txt', 'a') as f:
            f.writelines('\n\n'+ now + '\n\n'+'Q:\n'+ prev_input + '\n\nA:\n' + response)
    else:
        window.find_element('-OUTPUT-').Update('')
        response=llm(values['-INPUT-'])
        # Output a message to the window
        window['-OUTPUT-'].update( '\n'+ now+'\n\n' + values['-INPUT-'] + response)
        prev_input=values['-INPUT-']
        window.find_element('-INPUT-').Update('')
# Finish up by removing from the screen
window.close()
