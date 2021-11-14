import wikipedia, time
import PySimpleGUI as sg
# 
#      ____        _  ___                _ _       
#     |  _ \ _   _| |/ (_)_ __   ___  __| (_) __ _ 
#     | |_) | | | | ' /| | '_ \ / _ \/ _` | |/ _` |
#     |  __/| |_| | . \| | |_) |  __/ (_| | | (_| |
#     |_|    \__, |_|\_\_| .__/ \___|\__,_|_|\__,_|
#            |___/       |_|                       
# 
#     Este software foi escrito inteiramente em Python e utiliza a API wikipedia para fazer as buscas
#     Software criado por Elizeu Barbosa Abreu
#     Veja meus projetos no GitHub https://github.com/elizeubarbosaabreu
                                         
wikipedia.set_lang("pt")
x = wikipedia.summary("Wikipedia")

sg.theme('Reddit')

layout=[ [sg.Stretch(),
          sg.Input(key='-pesquisa-', size=(60,1), font=('Arial', 12)),
          sg.Button('Pesquisar', size=(12, 1), font=('Arial', 12)),
          sg.Stretch()],
         [sg.Stretch(),
          sg.Multiline(x, key='-conteudo-', size=(75, 25), font=('Arial', 12)),
          sg.Stretch()],
         [sg.Stretch(), sg.Text('PyKipedia - A Wikipedia Feita com Python')]
         ]
window = sg.Window('PyKipedia - A Wikipedia Feita com Python', layout, resizable=True)

while True:   
    
    event, values = window.read()    
        
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Pesquisar':
        try:
            window['-conteudo-'].update(wikipedia.summary(values['-pesquisa-']))
            time.sleep(5)
            window['-pesquisa-'].update('')
        except wikipedia.exceptions.WikipediaException as e:
            texto = f'''Ocorreu o seguinte erro durante a pesquisa: [{e}].
Tente usar outras palavras na pesquisa ou verifique sua conexão com a internet...
'''
            window['-conteudo-'].update(texto)
            time.sleep(5)
            window['-pesquisa-'].update('')

window.close()