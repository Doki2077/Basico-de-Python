from tkinter import *

# cores
cor1 = "#0a0a0a"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul
cor7 = "#ffcbdb" # rosa
cor8 = "#ffd4e1" #rosinha
 
# Configurando a janela
janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor7)
janela.resizable(width=False, height=False)

# Definindo variáveis globais
tempo = "00:00:00"
contador = -2

# Função para iniciar o cronômetro
def iniciar():
    global tempo, contador

    # Atualizando o contador
    contador += 1

    if contador >= 0:
        h = contador // 3600
        m = (contador % 3600) // 60
        s = contador % 60
        tempo = f"{h:02d}:{m:02d}:{s:02d}"
        label_tempo.config(text=tempo)
    
    # Chamando a função novamente após 1 segundo
    janela.after(1000, iniciar)

# Função para iniciar o cronômetro
def start():
    iniciar()

# Criando labels
label_app = Label(janela, text='Cronômetro', font='Arial 16 bold', bg=cor7, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor7, fg=cor2)
label_tempo.place(x=20, y=30)

# Criando botões
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor8, fg=cor2, font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, text='Pausar', width=10, height=2, bg=cor8, fg=cor2, font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2, bg=cor8, fg=cor2, font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)

janela.mainloop()
