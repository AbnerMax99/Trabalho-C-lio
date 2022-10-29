aluno = []
id_curso = []
disciplinas = []
duracao = []
curso = []


def lin():
    print('=-' * 30)

def invalida():
    return menu()

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
        invalida()


def menu_cursos():
    lin()
    print('CADASTRO DE CURSOS')
    lin()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Relatório Completo\nd- Relatório Específico\ne- Excluir Curso')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        incluirc()
    elif selecione == 'B':
        alterarcurso()
    elif selecione == 'C':
        relatcurso()
    elif selecione == 'D':
        relatcursoesp()
    elif selecione == 'E':
        excluicurso()
    else:
        print('OPÇÃO INVÁLIDA')
        lin()
        invalida()


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
        lin()
        invalida()


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
        lin()
        invalida()

def incluirc():
    lin()
    cursoid = int(input('Insira o ID do curso: '))
    cursoins = str(input('Insira o curso: ')).upper()
    cursodur = int(input('Digite a duração (semestral) do curso: '))
    curso.append(cursoins)
    duracao.append(cursodur)
    id_curso.append(cursoid)

    print('Curso inserido!')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno == 'S':
        return menu_cursos()
    elif retorno == 'N':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retornomenu == 'S':
            return menu()
        elif retornomenu == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            lin()
            invalida()
    else:
        print('OPÇÃO INVÁLIDA')
        lin()
        invalida()


def alterarcurso():
    lin()
    select_curso= int(input('Insira o ID do curso que deseja alterar: '))
    print(f'O Curso selecionado foi {curso[select_curso]}')
    alt_option= str(input('O que deseja alterar? (CURSO) (DURAÇÃO)\nPara alterar CURSO, digite C\nPara alterar DURAÇÃO, digite D\n')).upper()
    if alt_option == 'C':
        new_curso= str(input('Insira o novo curso: ')).upper()
        confirm_altc= str(input('Confirmar Alteração? (S) (N)\n')).upper()
        if confirm_altc == 'S':
            curso[select_curso] = f'{new_curso}'
            print('Curso Alterado!')
        elif confirm_altc == 'N':
            return menu_cursos()
        else:
            print('OPÇÃO INVÁLIDA')
            lin()
            invalida()
    elif alt_option == 'D':
        new_duracao= int(input('Insira a nova duração do curso: '))
        confirm_durc= str(input('Confirmar Alteração? (S) (N)\n')).upper()
        if confirm_durc == 'S':
            duracao[select_curso] = f'{new_duracao}'
            print('Curso Alterado!')
        elif confirm_durc == 'N':
            return menu_cursos()
        else:
            print('OPÇÃO INVÁLIDA')
            lin()
            invalida()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno == 'S':
        return menu_cursos()
    elif retorno == 'N':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retornomenu == 'S':
            return menu()
        elif retornomenu == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            lin()
            invalida()
    else:
        print('OPÇÃO INVÁLIDA')
        lin()
        invalida()

def relatcursoesp():
    lin()
    select_curso= int(input('Insira o ID do curso digitado: '))
    print(f'O curso selecionado foi: {curso[select_curso]}')
    print(f'Este curso possui: {duracao[select_curso]} semestre(s)\nA disciplica ainda não consta.')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno == 'S':
        return menu_cursos()
    elif retorno == 'N':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retornomenu == 'S':
            return menu()
        elif retornomenu == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            lin()
            invalida()
    else:
        print('OPÇÃO INVÁLIDA')
        lin()
        invalida()

def relatcurso():
    lin()
    for i, word in enumerate(curso):
        print('ID:', i, '/ Curso:' , word, f'/ A duração do curso é: {duracao[i]} semestres.')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno == 'S':
        return menu_cursos()
    elif retorno == 'N':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retornomenu == 'S':
            return menu()
        elif retornomenu == 'N':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')


def excluicurso():
    lin()
    curso_id = int(input('Insira o ID do curso quer excluir?\n'))
    print(f'O curso selecionado foi {curso[curso_id]}')
    confirm = str(input('Tem certeza? (S) (N)\n')).upper()
    if confirm == 'S':
        curso.pop(curso_id)
        print('Curso Deletado!')
    elif confirm == 'N':
        return menu_cursos()
    else:
        print('Opção Inválida')
    lin()
    retorno = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno == 'S':
        return menu_cursos()
    elif retorno == 'N':
        retornomenu = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retornomenu == 'S':
            return menu()
        elif retornomenu == 'N':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')

menu()