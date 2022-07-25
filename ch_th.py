import PySimpleGUI as sg

"""
to learn the system
original↓
https://stackoverflow.com/questions/66171339/is-there-a-way-to-update-every-window-when-a-new-theme-has-been-selected-in-pysi"""

#normal window
def make_window(theme=None):
    if theme:
        sg.theme(theme)

    layout=[[sg.Text('this is your theme.')],
            [sg.Button('ok'),sg.Button('change theme'),sg.Button('exit')]]
    return sg.Window('pattern for changing theme',layout)

def main():
    window=make_window()

    while True:
        event,values=window.read()
        if event in( sg.WIN_CLOSED,'exit'):
            break
        #theme change window
        if event == 'change theme':
            event,values=sg.Window('choose theme',
                        [[sg.Combo(sg.theme_list(),readonly=True,key='change'),sg.OK(),sg.Cancel()]]).read(close=True)
            #when click OK button on theme change window
            if event=='OK':
                #restart window
                window.close()
                window=make_window(values['change'])
        #when click ok button on normal window
        if event == 'ok':
            sg.popup('thank you!')
            break
    window.close()

if __name__ == '__main__':
    main()