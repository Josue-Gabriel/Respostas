import PySimpleGUI as sg

sg.theme("DarkPurple")


layout = [
    [sg.Text("Digite um valor", key="Texto")],
    [sg.Input(size=(3,3), border_width=(3), key="input"), sg.Button("Botão")]
]

janela = sg.Window('Fibonacci', layout)

while True:
    acao, valor = janela.read()
    if acao == sg.WINDOW_CLOSED:
        break
    if acao == "Botão":
        conta = 0
        primeiro = 0
        segundo = 1
        retorno = int(valor["input"])
        quantidade_de_calculos = 0
        gatilho = False
        exame = False
        while quantidade_de_calculos < 50 and gatilho == False:
            quantidade_de_calculos = quantidade_de_calculos + 1
            conta = segundo + primeiro
            primeiro = segundo
            segundo = conta
            if quantidade_de_calculos <= 49 and retorno == conta:
                janela["Texto"].update("Faz parte da lista de Fibonacci")
                gatilho = True
                exame = True
            if quantidade_de_calculos == 49:
                gatilho = True
        if exame == False:
            janela["Texto"].update("Não faz parte da lista de Fibonacci")
                        
                