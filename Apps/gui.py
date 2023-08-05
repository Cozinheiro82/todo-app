import functions
import PySimpleGUI as sg

label = sg.Text("Typ hier je to-do")
input_box = sg.InputText(tooltip="Typ je todo")
add_button = sg.Button("Toevoegen")

window = sg.Window('Mijn To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
