def analisar_alunos(alunos):

    melhor_media = 0 
    top_student = []
    recuperacao = []

    for nome, notas in alunos:

        print (nome, notas)
        if not notas:
            print(f"Estudante {nome} não posusi notas validas")
            continue 

        media = sum(notas) / len(notas)

        print(f"a media do(a) estudante {nome} é de {media: .2f}")
        if media < 7:
            recuperacao.append(nome)

        if media > melhor_media:
            melhor_media = media 
            top_student = [nome]

        elif media == melhor_media:
            top_student.append(nome)
         

    print("\nAlunos em recuperação:", recuperacao)
    print(f"Top Student: {top_student} com média de {media: .2f}") 



