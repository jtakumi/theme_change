import PySimpleGUI as psg

psg.theme('Blue Mono')

#ここでGUIの中のテキストやらボタンやらを配置
layout=[[psg.Text('theme browsing')],
        [psg.Text('click theme color')],
        [psg.Listbox(values=psg.theme_list(),size=(20,12),key='-LIST-',enable_events=True)],
        [psg.Button('exit')]]

#レイアウトの内容を読み込む
wnd=psg.Window('Theme Browser',layout)

#処理をループ
while True:
    #ウィンドウの内容を読み込む
    event,values = wnd.read()
    #exitボタンを押したらウィンドウを閉じる
    if event in (psg.WIN_CLOSED,'exit'):
        break
    psg.theme(values['-LIST-'][0])
    psg.popup_get_text('{} '.format(values['-LIST-'][0]))

wnd.close()