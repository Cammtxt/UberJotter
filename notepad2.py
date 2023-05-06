import PySimpleGUI as sg

sg.theme("SystemDefaultForReal")


layout = [[sg.Button("Open"), sg.Button("Save")], [sg.Multiline(size =(50,25), key="input")]]

window = sg.Window("Notepad but BETTER!!!1111!!!!!1", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Open":
        choosen_file = sg.popup_get_file("Choose a .txt to open")
        with open(choosen_file, "r") as w:
            output = w.read()
            window["input"].update(output)
            w.close()
    if event == "Save":
        folder = sg.popup_get_folder("Choose a folder to save to")
        file_name = sg.popup_get_text("Name this file")
        with open(folder + "/" + file_name + ".txt", "w") as f:
            f.write(values["input"])
            f.close()
window.close
