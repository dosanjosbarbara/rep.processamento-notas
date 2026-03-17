# rep.processamento-notas
Sistema em Python para processamento e análise de desempenho acadêmico a partir de estruturas de dados (listas e tuplas), com cálculo de médias, identificação de alunos em recuperação e geração de relatório automatizado.

Descrição do Projeto
Este projeto foi desenvolvido para auxiliar a coordenação acadêmica no acompanhamento do desempenho dos alunos.
O sistema processa uma estrutura de dados composta por uma lista de tuplas, onde cada tupla contém o nome do aluno e uma lista de notas. A partir dessas informações, o programa calcula a média de cada estudante, identifica alunos em situação de recuperação e determina o aluno com melhor desempenho da turma.
O sistema também valida os dados recebidos, verificando se as listas de notas estão vazias ou inválidas antes de realizar os cálculos.
Por fim, o programa gera um arquivo de relatório chamado resultado.txt, contendo os resultados da análise.

Estrutura dos Dados
Os dados dos alunos são representados utilizando lista de tuplas, conforme o formato abaixo:
[("Nome do aluno", [lista_de_notas])]
Exemplo:
[
    ("Ana", [8, 7, 9]),
    ("Carlos", [5, 6, 4]),
    ("Maria", [10, 9, 8]),
    ("João", [])
]
Cada elemento da lista contém:
Nome do aluno
Lista com suas notas
O número de notas pode variar para cada aluno.

Funcionalidades do Sistema
O sistema realiza as seguintes operações:
Percorre todos os alunos cadastrados
Valida se a lista de notas não está vazia
Calcula a média de cada aluno
Identifica alunos em recuperação (média menor que 7.0)
Identifica o aluno com maior média da turma (Top Student)
Exibe os resultados no terminal
Gera um relatório final no arquivo resultado.txt

Estrutura do Projeto
O projeto foi organizado de forma modular, separando a execução principal do processamento dos dados.
projeto/
│
├── main.py
├── processamento.py
├── resultado.txt
└── README.md
Descrição dos arquivos:
main.py
Responsável pela execução principal do programa e definição da estrutura de dados dos alunos.
processamento.py
Responsável pelo processamento das informações, incluindo:
validação das notas
cálculo das médias
identificação de alunos em recuperação
identificação do aluno com melhor desempenho
resultado.txt
Arquivo gerado automaticamente contendo o relatório final do processamento das notas.

Metodologia Utilizada
O desenvolvimento do projeto foi baseado em conceitos de Design Thinking e Gestão Ágil, conforme solicitado na atividade.
Foi utilizado um quadro Kanban individual para organizar as tarefas do projeto.
Kanban do Projeto
To Do
Levantamento de requisitos
Estruturação do projeto
Implementação da validação de dados
Doing
Implementação do cálculo de média
Identificação de alunos em recuperação
Done
Identificação do Top Student
Geração do relatório resultado.txt

Controle de Versão
O projeto utiliza Git para versionamento de código, simulando um ambiente colaborativo através do uso de branches.
Estrutura utilizada:
main → versão principal do projeto
feat/calculo-media → implementação do cálculo das médias
feat/recuperacao → identificação de alunos em recuperação
feat/relatorio → geração do relatório final
Após o desenvolvimento e testes de cada funcionalidade, as alterações foram integradas à branch principal através de merge.

Tecnologias Utilizadas
Python
Git
GitHub

Autora

**Bárbara dos Anjos**

Projeto desenvolvido como atividade do curso de **Ciência de Dados – SENAI**.
