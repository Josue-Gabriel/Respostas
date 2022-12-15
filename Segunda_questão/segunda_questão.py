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
        gatilho = False
        exame = False
        while retorno > conta:
            conta = segundo + primeiro
            primeiro = segundo
            segundo = conta
            if retorno == conta:
                janela["Texto"].update("Faz parte da lista de Fibonacci")
                gatilho = True
                exame = True
        if exame == False:
            janela["Texto"].update("Não faz parte da lista de Fibonacci")
        print(conta)
