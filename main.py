perguntas = ["qual e o nome completo da protagonista do episódio?",
             "quem dirige a vida de joan em tempo real para uma série de televisão?",
             "qual é o nome do serviço de streaming fictício que parodia a netflix no episodio?",
             "como joan descobre a existência da série sobre sua vida?",
             "qual é a reação inicial de joan ao descobrir a série e o que ela faz em resposta?",
             "quais são os temas principais explorados neste episódio de black mirror?"]

respostas = ["Joan Tait",
             "um super computador.",
             "streaberry.",
             "por acaso,procurando uma serie para assistir no streaberry.",
             "ela fica atônita entre em um surto, ela tenta revidar criando um caos em sua vida., e depois ela tenta tirar a série do ar.",
             "uso de imagem.,contratos abusivos, aceitar temos sem ler condições ,coleta de dados, tecnologia futurísticas."]



while True:
    menu = input("""   faça sua pergunta sobre o episódio: """)

    if menu in perguntas:          
      n = perguntas.index(menu)
      print(respostas[n])       
    elif menu == "":
        print("ops.. campo vazio!")
    else:
        print("pergunta nao encontrada!!!")
        
    