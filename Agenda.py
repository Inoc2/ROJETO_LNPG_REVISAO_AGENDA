#Amanda, Alvacy, Heitor
from tkinter import *

def abrir_txt():
    with open ('contatos.txt', 'a', encoding='utf-8') as arquivo:
        
        item = arquivo.readlines()
        
        for i in item:
            interface.insert(END, i)

current_height = 35 #altura
curretnt = list 
root = Tk()
root.title("Sistema de Agenda de Contatos")
root.resizable(False, False)

def generic_label(generic_text):
    global current_height
    text_generic_label = Label(text = generic_text )
    text_generic_label.place(x = 35, y = current_height)
    current_height += 35

def cria_caixa_de_texto():

def generic_radio_button_two_options(option_1, option_2):
    radio_button_two_options = IntVar
    radio_button_two_options.set(1)
    
    radio_button_two_options_option_1 = Radiobutton(value=)
    
    Radiobutton
generic_label("Nome:")
generic_label("N° de telefone:")
generic_label("E-mail")

root.mainloop()
    

