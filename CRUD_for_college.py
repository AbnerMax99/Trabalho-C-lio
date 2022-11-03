from random import randrange

from _students import input_student, change_student, consult_students, full_report, del_studentes


# Variáveis para CRUD de cursos 
course_id = list()
curso = list()
duracao = list()

# Variáveis para CRUD de disciplinas 
subjects = dict()


def skip_line() -> str:
    '''Função para pular linha'''

    print('=-' * 30)


def invalid_option() -> None:
    '''Retorna ao menu quando o usuário escolher uma opção inválida'''

    return menu()


# ============== Seção de menus ============== 

def menu() -> None:
    '''Chama o manu principal, no qual o usuário poderá escolher entre o controle de cadastro de alunos, usuário ou disciplinas'''

    print(
        'Selecione a opção desejada\n1- Controle de Alunos\n2- Controle de Cursos\n3- Controle de Disciplinas\n4- Sair')
    skip_line()
    selecione = int(input('Opção escolhida: '))
    if selecione == 1:
        menu_alunos()
    elif selecione == 2:
        menu_cursos()
    elif selecione == 3:
        menu_disciplinas()
    elif selecione == 4:
        skip_line()
        print('Programa Finalizado!')
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()


def menu_alunos() -> None:
    '''Menu para criação, consulta, atualização e destruição de dados de ALUNOS.'''

    skip_line()
    print('CADASTRO DE ALUNOS')
    skip_line()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Consultar pelo RA\nd- Relatório Completo\ne- Excluir Aluno')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        input_student()
        menu()
    elif selecione == 'B':
        change_student()
    elif selecione == 'C':
        consult_students()
        menu()
    elif selecione == 'D':
        full_report()
        menu()
    elif selecione == 'E':
        del_studentes()
        menu()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()


def menu_cursos() -> None:
    '''Menu para criação, consulta, atualização e destruição de dados de CURSOS.'''

    skip_line()
    print('CADASTRO DE CURSOS')
    skip_line()
    print(
        'Selecione uma opção\na- Incluir\nb- Alterar\nc- Relatório Completo\nd- Relatório Específico\ne- Excluir Curso')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        incluir_curso()
    elif selecione == 'B':
        alterarcurso()
    elif selecione == 'C':
        return_all_courses()
    elif selecione == 'D':
        return_course()
    elif selecione == 'E':
        excluir_curso()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()


def menu_disciplinas() -> None:
    '''Menu para criação, consulta, atualização e destruição de dados de DISCIPLINAS.'''

    skip_line()
    print('CADASTRO DE DISCIPLINAS')
    skip_line()
    print('Selecione uma opção\na- Incluir\nb- Alterar\nc- Relatório Completo\nd- Excluir Disciplina')
    selecione = str(input('Opção escolhida: ')).upper()
    if selecione == 'A':
        incluir_disciplina()
    elif selecione == 'B':
        alterar_disciplina()
    elif selecione == 'C':
        all_subjects()
    elif selecione == 'D':
        excluir_disciplina()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()

# ============== Seção de CURSOS ============== 

def generate_course_id() -> int:
    '''
        Gera um número ramdômico pseudoaleatório que servirá como identificador do curso.
    '''

    # Resultado do função
    result_id = 0

    # Verificador da validade do ID do curso
    valid_id = False

    while (valid_id == False):
        result_id = int(randrange(10000, 99999))
        for i in course_id:
            if i == result_id:
                break

        valid_id = True
    return result_id


def incluir_curso() -> None:
    '''Cadastra um novo curso'''

    skip_line()
    course_id.append(generate_course_id())
    curso_nome = str(input('Insira o curso: ')).upper()
    curso_duracao = int(input('Digite a duração (semestral) do curso: '))
    curso.append(curso_nome)
    duracao.append(curso_duracao)
    print('Curso inserido!')

    skip_line()

    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        return menu_cursos()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            skip_line()
            invalid_option()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()


def alterarcurso() -> None:
    '''Altera os dados de um curso cadastrado'''

    skip_line()

    try:  
    # Tenta localizar o curso pelo ID, que foi gerado pela função 'generate_course_id e armazenada pela função 'incluir_curso'

        # Localiza o indicador do curso na lista por meio do ID fornecido pelo usuário.
        select_curso = course_id.index(int(input('Insira o ID do curso que deseja alterar: ')))  

        print(f'O Curso selecionado foi {curso[select_curso]}')

        option_change_course = str(input('O que deseja alterar? (CURSO) (DURAÇÃO)\nPara alterar CURSO, digite C\nPara alterar DURAÇÃO, digite D\n')).upper()
        if option_change_course == 'C':
            new_curso = str(input('Insira o novo curso: ')).upper()
            confirm_change = str(input('Confirmar Alteração? (S) (N)\n')).upper()
            if confirm_change == 'S':
                curso[select_curso] = f'{new_curso}'
                print('Curso Alterado!')
            elif confirm_change == 'N':
                return menu_cursos()
            else:
                print('OPÇÃO INVÁLIDA')
                skip_line()
                invalid_option()
        elif option_change_course == 'D':
            new_duracao = int(input('Insira a nova duração do curso: '))
            confirm_duracao = str(input('Confirmar Alteração? (S) (N)\n')).upper()
            if confirm_duracao == 'S':
                duracao[select_curso] = f'{new_duracao}'
                print('Curso Alterado!')
            elif confirm_duracao == 'N':
                return menu_cursos()
            else:
                print('OPÇÃO INVÁLIDA')
                skip_line()
                invalid_option()
    except:
        print("Desculpe, mas não localizei este curso!")

    # Opções de menu
    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        return menu_cursos()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            skip_line()
            invalid_option()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()


def return_course() -> str:
    '''Exibe os dados de um curso'''

    global subjects
    skip_line()

    try:
    # Tenta localizar o curso pelo ID, que foi gerado pela função 'generate_course_id e armazenada pela função 'incluir_curso'

        # Localiza o indicador do curso na lista por meio do ID fornecido pelo usuário.
        select_curso = course_id.index(int(input('Insira o ID do curso: ')))

        print(f'O curso selecionado foi: {curso[select_curso]}')
        print(f'Este curso possui: {duracao[select_curso]} semestre(s)')
        print(f'Este curso possui a(s) seguinte(s) disciplina(s): ')
        print(', '.join(subjects[select_curso]))   #mostra as diciplinas do curso
        skip_line()

    except:
        print("Desculpe, mas não consegui localizar o curso")

    # Opções de menu
    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        return menu_cursos()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            skip_line()
            invalid_option()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()


def return_all_courses() -> str:
    '''Exibe os dados de todos os cursos'''

    skip_line()

    for i, value in enumerate(curso):
        print('ID:', course_id[i], '/ Curso:', value, f'/ A duração do curso é: {duracao[i]} semestres.')

    skip_line()

    # Opções de menu
    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        return menu_cursos()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')


def excluir_curso():
    ''' curso cadastrado'''

    skip_line()

    try:
    # Tenta localizar o curso pelo ID, que foi gerado pela função 'generate_course_id e armazenada pela função 'incluir_curso'

        # Localiza o indicador do curso na lista por meio do ID fornecido pelo usuário.
        curso_id = course_id.index(int(input('Insira o ID do curso quer excluir?\n')))

        print(f'O curso selecionado foi {curso[curso_id]}')

        # Confirma de o usuáiro realmente deseja deletar o curso
        confirm_excluir_course = str(input('Tem certeza que deseja excluir o curso? (S) (N)\n')).upper()
        if confirm_excluir_course == 'S':
            curso.pop(curso_id)
            course_id.pop(curso_id)
            print('Curso Deletado!')
        elif confirm_excluir_course == 'N':
            return menu_cursos()
        else:
            print('Opção Inválida')

    except:
        print("Desculpe, mas não consegui localizar o curso.")

    skip_line()

    # Opções de menu
    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        return menu_cursos()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')

# ============== Seção de DISCIPLINAS ============== 

def incluir_disciplina() -> None:
    '''Cadastra uma nova disciplina'''

    global subjects

    skip_line()

    try:
    # Tenta localizar o curso pelo ID, que foi gerado pela função 'generate_course_id e armazenada pela função 'incluir_curso'

        # Localiza o indicador do curso na lista por meio do ID fornecido pelo usuário
        select_curso = course_id.index(int(input('Insira o ID do curso: '))) 

        print(f'O curso selecionado foi: {curso[select_curso]}')

        subjectc_name = str(input('Qual disciplina deseje inserir?\n: ')) #Inserção da disciplina no curso selecionado

        try:
            subjects[str(select_curso)][str(generate_course_id())] = subjectc_name
        except:
            subjects[str(select_curso)] = dict()
            subjects[str(select_curso)][str(generate_course_id())] = subjectc_name

        print('Disciplina Inserido!')

    except:
        print("Desculpe, mas não consegui localizar este curso!")

    skip_line()

    # Opções de menu
    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        menu_disciplinas()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('OPÇÃO INVÁLIDA')
            skip_line()
            invalid_option()
    else:
        print('OPÇÃO INVÁLIDA')
        skip_line()
        invalid_option()

def alterar_disciplina() -> None:

    skip_line()

    try:
    # Tenta localizar o curso pelo ID, que foi gerado pela função 'generate_course_id e armazenada pela função 'incluir_curso'

        # Localiza o indicador do curso na lista por meio do ID fornecido pelo usuário
        select_curso = course_id.index(int(input('Insira o ID do curso: ')))  #Seleção do curso pelo ID
        print(f'O Curso selecionado foi {curso[select_curso]}')
        print(subjects[select_curso])
        
        select_subject = (input('Selecione a disciplina que deseja alterar: ')).upper() 
        index_subject = subjects[select_curso].index(select_subject)
        try:
            print(f'A disciplina selecionada foi {subjects[select_curso][index_subject]}')
            new_subject = str(input('Insira a nova disciplina: ')).upper()    #Aqui é para inserir a nova disciplina na atual ERRO
            confirm = str(input('Cofirmar alteração? (S) (N)\n: ')).upper()
            if confirm == 'S':
                subjects[select_curso][index_subject] = f'{new_subject}'
                print('Disciplina alterada')
            elif confirm == 'N':
                return menu_disciplinas()
            else:
                print('OPÇÃO INVÁLIDA')
                skip_line()
                invalid_option()
        except:
            print("Desculpe, mas não localizei esta disciplina")
            menu()
    
    except:
        print("Desculpe, mas não consegui localizar o curso!")

    skip_line()

    # Opções de menu
    retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
    if retorno_menu_secundario == 'S':
        return menu_cursos()
    elif retorno_menu_secundario == 'N':
        retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
        if retorno_menu_principal == 'S':
            return menu()
        elif retorno_menu_principal == 'N':
            print('Programa Finalizado!')
        else:
            print('Opção Inválida!')
    else:
        print('Opção Inválida!')

def all_subjects() -> str: #Relatório das disciplinas a qual deve mostrar : Disciplina 'x' - Curso 'y' e etc..
    '''Exibe todas as disciplinas de todos os cursos'''

    global subjects, course_id, curso

    for id_course in subjects.keys():
        for id_subjects in subjects[id_course].keys():
            print(subjects[id_course][id_subjects])

            # Opções de menu
        retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
        if retorno_menu_secundario == 'S':
            return menu_cursos()
        elif retorno_menu_secundario == 'N':
            retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
            if retorno_menu_principal == 'S':
                return menu()
            elif retorno_menu_principal == 'N':
                print('Programa Finalizado!')
            else:
                print('Opção Inválida!')
        else:
            print('Opção Inválida!')

def excluir_disciplina() -> None:
    '''Apaga uma disciplina'''

    global subjects

    skip_line()

    try:
    # Tenta localizar o curso pelo ID, que foi gerado pela função 'generate_course_id e armazenada pela função 'incluir_curso'

        # Localiza o indicador do curso na lista por meio do ID fornecido pelo usuário
        select_curso = course_id.index(int(input('Insira o ID do curso: ')))  #Seleção do curso pelo ID
        print(f'O Curso selecionado foi {curso[select_curso]}')
        print(subjects[select_curso])
        
        select_subject = (input('Selecione a disciplina que deseja alterar: ')).upper()
        index_subject = subjects[select_curso].index(select_subject)
        try:
            print(f'Disciplina selecionada foi: {subjects[select_curso][index_subject]}')
            confirm = str(input('Confirmar Exclusão? (S) (N)'))
            if confirm == 'S':
                subjects[select_curso].pop(index_subject)
                print('Disciplina Excluída com Sucesso!')
            elif confirm == 'N':
                return menu_disciplinas()
            else:
                print('OPÇÃO INVÁLIDA')
                skip_line()
                invalid_option()
        except:
            print("Não localizei o curso")
    except:
        print("Não localizei a disciplina")


        # Opções de menu
        retorno_menu_secundario = str(input('Deseja voltar ao menu anterior? (S) (N)\n')).upper()
        if retorno_menu_secundario == 'S':
            return menu_cursos()
        elif retorno_menu_secundario == 'N':
            retorno_menu_principal = str(input('Deseja voltar ao menu principal? (S) (N)\n')).upper()
            if retorno_menu_principal == 'S':
                return menu()
            elif retorno_menu_principal == 'N':
                print('Programa Finalizado!')
            else:
                print('Opção Inválida!')
        else:
            print('Opção Inválida!')

# =======> GO
menu()