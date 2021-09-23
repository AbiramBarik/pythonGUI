import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg
sg.theme('DarkAmber')
layout=[[sg.Text('Enter the URL ',font=('Lucida',13)),sg.In(size=(50,1)),sg.Submit()],[sg.Output(size=(80,20),key='-out-',font=('Lucida',15))],[sg.Button(button_text='Get data of a particular tag',key='-open-')]]
window = sg.Window("Web scarpper", layout,element_justification='c').finalize()
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event=='Submit':
        url=values[0]
        response=requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        window['-out-'].TKOut.output.config(wrap='word')
        print(soup.prettify)
    while event=='-open-':
        new=[[sg.Text('Enter tag to get its content ',font=('Lucida',15)),sg.In(size=(20,1)),sg.Button('GET',key='b1')],[sg.Output(size=(80,15),key='-out1-',font=('Lucida',15))]]
        win=sg.Window("content",new,element_justification='c').finalize()
        while True:
            ev,val=win.read()
            if ev=="Exit" or ev==sg.WINDOW_CLOSED:
                break
            elif ev=='b1':
                my_list=[tag.text for tag in soup.findAll(val[0])]
                win['-out1-'].update(my_list)
            