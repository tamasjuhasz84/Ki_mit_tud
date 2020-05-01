import PySimpleGUI as sg 
sg.theme("LightGrey3")

layout = [
    [sg.Text(                                 size=(32,1))],
    [sg.Text("Versenyző neve",                size=(32,1)),       sg.Input(key="-NÉV-")],
    [sg.Text("Versenyző pontszáma",size=(32,1)),sg.Input(key = "-PONT-", enable_events = True), sg.Text(key = "-DB-", size=(10,1))],
    
    [sg.Text("Kieső legmagasabb pontszám",    size=(32,1))],
    [sg.Text("Kieső legalacsonyabb pontszám", size=(32,1))],
    [sg.Text("Összesített pontszám",          size=(32,1))],
    [sg.Text(size=(32,1)),                                        sg.Button("Versenyző hozzáadása")]
    ]
window = sg.Window("Versenyző GUI",layout)
while True:
    event, values = window.read()
#    print(event, values)
    
    if event in (None, "Exit"):
        break
    if event == "-PONT-":
        p = values["-PONT-"]
        db= len(p.split())
        window["-DB-"].update(db)
        
window.close()
text_input = values["-NÉV-"]
sg.Popup("Eredmény", text_input)


