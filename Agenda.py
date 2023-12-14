#Amanda, Alvacy, Heitor
from tkinter import *


#adad
current_height = 35 #altura
current = []
root = Tk()
tentative_users = 0
root.geometry("750x750")
root.title("Sistema de Agenda de Contatos")
root.resizable(False, False)

def generic_label(generic_text):
    global current_height
    text_generic_label = Label(text = generic_text )
    text_generic_label.place(x = 35, y = current_height)
    current_height += 35
    
def cria_caixa_de_texto():
    global current_height
    text_box = Entry(root)
    current.append(text_box)
    text_box.place(x=35, y=current_height)
    text_box.config(width=80)
    current_height += 35
    
def generic_radio_button_two_options(option_1, option_2):
    global current_height
    radio_button_two_options = IntVar()
    radio_button_two_options.set(1)
    
    radio_button_two_options_option_1 = Radiobutton(text = option_1, variable=radio_button_two_options, value=1)
    radio_button_two_options_option_2 = Radiobutton(text = option_2, variable=radio_button_two_options, value=2)

    radio_button_two_options_option_1.place(x = 35, y = current_height)
    radio_button_two_options_option_2.place(x = 90, y = current_height)
    current_height += 35

def generic_label_status_send_information(text_from_user, exactly_height):
    global current_height, tentative_users
    if tentative_users == 0:
        label_status_user = Label(text = text_from_user, bg="red")
        label_status_user.place(x = 35, y = exactly_height)
    else:
        label_status_user.config(text = text_from_user)
    tentative_users += 1

def send_informations_button():
    global current_height
    button_information = Button(text="Enviar informações", command=save_content)
    button_information.place(x=35, y=current_height)
    current_height += 35
    
def save_content():
    
    while True:
        global current_height
        listaFormatada = [entrada.get() for entrada in current]
        print(listaFormatada)
        try:
            listaFormatada[1] = int(listaFormatada[1])
        except:
            generic_label_status_send_information("Você não inseriu um ano válido. Tente novamente", current_height + 35)
            break
        if "@" not in listaFormatada[2] and ".com" not in listaFormatada[2]:
            generic_label_status_send_information("Você não inseriu um email válido. Inclua @ e ponto")
            break
        with open ('contatos.txt', 'a', encoding='utf-8') as arquivo:
            for x in listaFormatada:
                # item = arquivo.readlines()
                print(x)
        
       
        


        
        
        
generic_label("Nome:")
cria_caixa_de_texto()
generic_label("N° de telefone:")
cria_caixa_de_texto()
generic_label("E-mail")
cria_caixa_de_texto()
generic_radio_button_two_options("Sim", "Não")
send_informations_button()
root.mainloop()
    

