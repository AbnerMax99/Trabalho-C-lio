aluno = []
curso = [] # ARRAWS VAZIOS
disciplinas = []
duracao = []


def lin():
    print('=-' * 30)

def menu():
    print(
        'Selecione a opção desejada\n1- Cadastro de Alunos\n2- Cadastro de Cursos\n3- Cadastro de Disciplinas\n4- Sair')
    lin()
    selecione = int(input('Opção escolhida: '))
    if selecione == 1:
        menu_alunos()
    elif selecione == 2:
        menu_cursos()
    elif selecione == 3:
        menu_desci()
    elif selecione == 4:
        lin()
        print('Programa Finalizado!')
    else:
        print('OPÇÃO INVÁLIDA')
    lin()

def menu_cursos():
    lin()
    print('CADASTRO DE CURSOS')
    lin()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Relatório Completo\nd- Excluir Curso')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        incluirc()
    elif selecione == 'B':
        alterarcurso()
    elif selecione == 'C':
        relatcurso()
    elif selecione == 'D':
        excluicurso()

def menu_alunos():
    lin()
    print('CADASTRO DE ALUNOS')
    lin()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Relatório Completo\nd- Excluir Aluno')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        print('NADA AINDA')
    elif selecione == 'B':
        print('NADA AINDA')
    elif selecione == 'C':
        print('NADA AINDA')
    elif selecione == 'D':
        print('NADA AINDA')
    else:
        print('OPÇÃO INVÁLIDA')

def menu_desci():
    lin()
    print('CADASTRO DE DISCIPLINAS')
    lin()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Relatório Completo\nd- Excluir Disciplina')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        print('NADA AINDA')
    elif selecione == 'B':
        print('NADA AINDA')
    elif selecione == 'C':
       print('NADA AINDA')
    elif selecione == 'D':
       print('NADA AINDA')
    else:
        print('OPÇÃO INVÁLIDA')

def incluirc():
    lin()
    cursoins = str(input('Insira o curso a ser inserido: '))
    cursoins.upper()
    curso.append(cursoins)
    durcurso = int(input('Digite a duração (semestral) do curso inserido acima: '))
    duracao.append(durcurso)
    print('Curso inserido!')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n'))
    retorno.upper()
    if retorno == 's':
        return menu_cursos()
    elif retorno == 'n':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n'))
        retornomenu.upper()
        if retornomenu == 's':
            return menu()
        elif retornomenu == 'n':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')
    
def alterarcurso():
    lin()
    cursonew = str(input('Insira aqui o novo curso: '))
    cursonumber = int(input('Insira o código do curso: '))
    curso.insert(cursonumber, cursonew)
    print('Curso Alterado!')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n'))
    retorno.upper()
    if retorno == 's':
        return menu_cursos()
    elif retorno == 'n':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n'))
        retornomenu.upper()
        if retornomenu == 's':
            return menu()
        elif retornomenu == 'n':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')

def relatcurso():
    lin()
    for i, word in enumerate(curso):
        print ('ID:' ,i, word, f'/ A duração do curso é: {duracao[i]} semestres.')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n'))
    retorno.upper()
    if retorno == 's':
        return menu_cursos()
    elif retorno == 'n':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n'))
        retornomenu.upper()
        if retornomenu == 's':
            return menu()
        elif retornomenu == 'n':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')

def excluicurso():
    lin()
    delcurso = int(input('Insira o código do curso quer excluir?\nDigite aqui: '))
    del(curso[delcurso])
    confirm = str(input('Tem certeza?'))
    confirm.upper()
    if confirm == 's':
        print('Curso Deletado!')
    elif confirm == 'n':
        return menu_cursos()
    else:
        print('Opção Inválida')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n'))
    retorno.upper()
    if retorno == 's':
        return menu_cursos()
    elif retorno == 'n':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n'))
        retornomenu.upper()
        if retornomenu == 's':
            return menu()
        elif retornomenu == 'n':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')

menu()