def janeiro():
    valores = [
    31490.7866,
    37277.9400,
    37708.4303,
    17934.2269,
    6965.1262,
    24390.9374,
    14279.6481,
    39807.6622,
    27261.6304,
    39775.6434,
    29797.6232,
    17216.5017,
    12974.2000,
    28490.9861,
    8748.0937,
    8889.0023,
    17767.5583,
    3071.3283,
    48275.2994,
    10299.6761,
    39874.1073]

    dias = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 6', 'Dia 7', 'Dia 9', 'Dia 10', 'Dia 11','Dia 14', 'Dia 15', 'Dia 16', 'Dia 17', 
    'Dia 18', 'Dia 21', 'Dia 22', 'Dia 23', 'Dia 24', 'Dia 25', 'Dia 28', 'Dia 29', 'Dia 30']

    

    soma = sum(valores)
    media = soma / len(valores) 
    print("O Menor valor de faturamento: {}".format(min(valores)))
    print("O Maior valor de faturamento: {}".format(max(valores))) 
    print("A media é: ", media)
    
    acima = 0  
    baixo = 0 

    for valor_media in valores:  
        if valor_media > media:  
            acima += 1
            
    print(f"Total de dias em que o faturamento fora a cima da média foi: {acima}")


def fevereiro():
    valores = [
        31490.7866, 
        37277.9400, 
        37708.4303, 
        17934.2269, 
        6965.1262, 
        24390.9374, 
        14279.6481, 
        39807.6622, 
        27261.6304, 
        39775.6434, 
        29797.6232, 
        17216.5017, 
        12974.2000, 
        28490.9861, 
        8748.0937, 
        8889.0023, 
        17767.5583, 
        3071.3283, 
        48275.2994, 
        10299.6761, 
        39874.1073, 
    ]

    dias = ['dia 1', 'dia 2', 'dia 3', 'dia 6', 'dia 8', 'dia 9', 'dia 10', 'dia 13', 'dia 14', 'dia 15', 'dia 16', 
    'dia 17', 'dia 20', 'dia 21', 'dia 22', 'dia 23', 'dia 24', 'dia 27', 'dia 28', 'dia 29', 'dia 30']

    soma = sum(valores)
    media = soma / len(valores)
    print("-------------------------------------------------------------------------------------------------------------")  
    print("O Menor valor de faturamento: {}".format(min(valores)))
    print("O Maior valor de faturamento: {}".format(max(valores)))
    print("A media é: ", media)
    
    acima = 0  
    baixo = 0 

    for valor_media in valores:  
        if valor_media > media:  
            acima += 1
            
    print(f"Total de dias em que o faturamento fora a cima da média foi: {acima}")

janeiro()
fevereiro()

