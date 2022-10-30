from random import uniform

# =============================================================================

def read_students() -> dict:
    '''
    Le o arquivo files\students.py e retorna em um dicionário
    '''

    students = dict()

    # Estrutura de leitura do arquivo students.csv
    # 0 - RA | 1 - Nome | 2 - CPF | 3 - Curso

    with open('files\students.csv', 'r') as students_table:
        for text_line in students_table:
            text_line = text_line.replace('\n', '')
            student = text_line.split(';')
            
            students[student[0]] = dict()
            students[student[0]]['name'] = student[1]
            students[student[0]]['CPF'] = student[2]
            students[student[0]]['id_course'] = student[3]

    return students

# =============================================================================

def register_students(students=dict, mode=str) -> None:
    '''
        Salva o dicionário students no arquivo de texto files\students.csv
    '''

    # Line prepara os dados para armazenalos em students.csv
    line_for_csv = ''

    with open('files\students.csv', mode) as students_table:
        for row in students.keys():
            line_for_csv = row

            for column in students[row].keys():
                line_for_csv += ';' + str(students[row][column])

            students_table.write(str(line_for_csv +'\n'))

# =============================================================================

def generate_id() -> int:
    '''
    Gera um RA do tipo inteiro para o estudante
    '''

    # Recebe os estudantes que já foram cadastrados
    students = read_students()

    # Verifica se o id é valido, ou seja, nao é repetido
    valid_id = False

    id = 0

    while( valid_id == False ):
        id = int(uniform(1000, 9999))
        for key in students.keys():
            if key == id:
                break

        valid_id = True
    return id

# =============================================================================

def input_student () -> None:
    '''
        Recebe e organiza dos dados dos alunos informados pelo usuário antes de armazena-los
    '''
    
    students = dict()
    go_repet = True

    while( go_repet == True ):
        
        # Variável radomica
        id = str( generate_id() )

        # Input de variáveis
        name = str(input("Infome o nome do aluno: "))
        cpf = str(input("Informe o CPF do aluno: "))
        id_course = str(input("Informe o ID do curso: "))

        #cadastro das variáveis
        students[id] = dict()
        students[id]['name'] = name
        students[id]['cpf'] = cpf
        students[id]['id_course'] = id_course

        repet = input("Deseja cadastrar um novo aluno? [y/n] ").upper()
        if (repet != 'Y'):
            go_repet = False

    register_students(students=students, mode='a')

# =============================================================================

def change_student() -> None:
    '''
    Altera o cadastro de um estudante.
    '''

    # Verifica se o aluno foi encontrado
    student_located = False

    # Le a tabela com os dados dos estudantes
    students = read_students()

    # Recebe o ID/RA do aluno que deverá alterar
    ra = str(input("Informe o RA do aluno para alterar o cadastro: "))

    for key in students.keys():
        if ra == key:
            print('Consegui localizar o aluno ^_^')
            print(students[key]['name'], '- CPF ' , students[key]['CPF'], '- ID do curso ', students[key]['id_course'])
            option = str(input("Qual dado deseja alterar?\nA - Nome\nB - CPF\nC - Curso\nPara desistir aperte outra tecla\n")).upper()
            match option:
                case 'A':
                    students[key]['name'] = str(input("Ok, entao me informe o nome correto do aluno, por favor: "))
                case 'B':
                    students[key]['CPF'] = str(input("E qual é o CPF correto deste aluno? "))
                case 'C':
                    students[key]['id_course'] = str(input("Me inform o ID do curso em que devo matricula-lo, por favor: "))
                case _:
                    print("Poxa, ainda nao consigo antender isso. Por que nao tenta depois? ")

            print(students)
            confirm = str(input("Tem certeza que deseja realizar a alteraçao? [y/n] ")).upper()
            if confirm == 'Y':
                register_students(students=students, mode='w')

            student_located = True
            break
        
    if student_located == False:
        print("Perdao, nao consegui localizar este aluno :/")

change_student()