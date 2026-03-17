def analisar_alunos(alunos):

    melhor_media = 0 
    top_student = []
    recuperacao = []
    relatorio = [] 
    for nome, notas in alunos:

        print (nome, notas)
        if not notas:
            linha = f"Estudante {nome} não possui notas validas"
            print(linha)
            relatorio.append(linha)
            continue

        media = sum(notas) / len(notas)
        linha = f"Estudante {nome} média de: {media:.2f}"
        print(linha)
        relatorio.append(linha)

        if media < 7:
            recuperacao.append(nome)

        if media > melhor_media:
            melhor_media = media 
            top_student = [nome]

        elif media == melhor_media:
            top_student.append(nome)
         
    relatorio.append ("\nEstudantes em recuperação: " + ", ".join(recuperacao))

    relatorio.append(
        f"Top Students: {', '.join(top_student)} com melhor média de: {melhor_media:.2f}"    
    )

    with open("ResultadoNotas.txt", "w", encoding="utf-8") as arquivo:
        for linha in relatorio:
            arquivo.write(linha + "\n")








