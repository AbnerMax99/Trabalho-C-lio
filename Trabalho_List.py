#  ========== Opening commit by Leo ========== 
from random import randrange

from _students import input_student, change_student, consult_students, full_report, del_studentes

course_id = list()
#  ========== End commit ========== 
id_curso = []
disciplinas = []
duracao = []
curso = []


def lin():
    print('=-' * 30)

def invalida():
    return menu()

def menu():

    # Busca a varial global que controla o funcionamento do programa 
    global go

    print(
        'Selecione a opção desejada\n1- Conntrole de Alunos\n2- Conntrole de Cursos\n3- Conntrole de Disciplinas\n4- Sair')
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


#  ========== Opening commit by Leo ========== 

def menu_alunos():
    lin()
    print('CADASTRO DE ALUNOS')
    lin()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Consultar pelo RA\nd- Relatório Completo\ne- Excluir Aluno')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        input_student()
    elif selecione == 'B':
        change_student()
    elif selecione == 'C':
        consult_students()
    elif selecione == 'D':
        full_report()
    elif selecione == 'E':
        del_studentes()
    else:
        print('OPÇÃO INVÁLIDA')
        lin()
        invalida()
        print('OPÇÃO INVÁLIDA')
        lin()
        invalida()

#  ========== End commit ========== 

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

#  ========== Opening commit by Leo ========== 

def generate_course_id() -> int:
    '''
        Gera um número ramdômico pseudoaleatório que servirá como identificador do curso.
    '''

    # Resultado do função 
    result_id = 0

    # Verificador da validade do ID do curso 
    valid_id = False

    while(valid_id == False):
        result_id = int(randrange(10000, 99999))
        for i in course_id:
            if i == result_id:
                break

        valid_id = True
    return result_id
        
#  ========== End commit ========== 

def incluirc():
    lin()
#  ========== Opening commit by Leo ========== 
    course_id.append(generate_course_id())
#  ========== End commit ========== 
    cursoins = str(input('Insira o curso: ')).upper()
    cursodur = int(input('Digite a duração (semestral) do curso: '))
    curso.append(cursoins)
    duracao.append(cursodur)
    print('Curso inserido!')
    for i in range (0, len(curso)):
        print(f'O ID deste curso é: {i}')

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
    try: # Tratamento de erro
        select_curso = course_id.index(int(input('Insira o ID do curso que deseja alterar: '))) # Seleção do curso pelo ID
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
    except:
        print("Desculpe, mas não localizei este curso!")

def relatcursoesp():
    lin()
    try: # Tratamento de erro
        select_curso = course_id.index(int(input('Insira o ID do curso: '))) # Seleção do curso pelo ID
        print(f'O curso selecionado foi: {curso[select_curso]}')
        print(f'Este curso possui: {duracao[select_curso]} semestre(s)\nA disciplica ainda não consta.')
        lin()
    except:
        print("Desculpe, mas não consegui localizar o curso")

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
        print('ID:', course_id[i], '/ Curso:' , word, f'/ A duração do curso é: {duracao[i]} semestres.')
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
    try: # Tratamento de erro
        curso_id = course_id.index(int(input('Insira o ID do curso quer excluir?\n'))) # Seleção do curso pelo ID
        print(f'O curso selecionado foi {curso[curso_id]}')
        confirm = str(input('Tem certeza? (S) (N)\n')).upper()
        if confirm == 'S':
            curso.pop(curso_id)
            course_id.pop(curso_id)
            print('Curso Deletado!')
        elif confirm == 'N':
            return menu_cursos()
        else:
            print('Opção Inválida')
    except:
        print("Desculpe, mas não consegui localizar o curso.")

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


# =======> GO 
menu()