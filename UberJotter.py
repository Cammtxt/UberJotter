import PySimpleGUI as sg

main_menu = True
notepad = False

main_menu_options = ["Notepad", "More soon!"]

sg.theme("SystemDefaultForReal")

main_layout = [[sg.Text("Please select a software you would like to use:")], 
               [sg.DD(main_menu_options, default_value="Notepad", key="main_DD", size=(25,25)), sg.OK(key="main_OK")]]

pad_layout = [[sg.Button("Open"), sg.Button("Save")], 
            [sg.Multiline(size =(100,50), key="note_input")]]

main_window = sg.Window("UbberJotter", main_layout)
pad_window = sg.Window("UberJotter - Notepad", pad_layout)

while main_menu == True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        main_menu = False
        main_window.close
    if event == "main_OK":
        if values["main_DD"] == "Notepad":
            notepad = True
            main_menu = False
            main_window.close
        else:
            sg.popup_error()
    
while notepad == True:
    event, values = pad_window.read()
    if event == sg.WIN_CLOSED:
        notepad = False
        pad_window.close
    if event == "Open":
        choosen_file = sg.popup_get_file("Choose a .txt to open")
        with open(choosen_file, "r") as w:
            output = w.read()
            pad_window["note_input"].update(output)
            w.close()
    if event == "Save":
        folder = sg.popup_get_folder("Choose a folder to save to")
        file_name = sg.popup_get_text("Name this file")
        with open(folder + "/" + file_name + ".txt", "w") as f:
            f.write(values["note_input"])
            f.close()