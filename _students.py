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
            students[student[0]]['Nome'] = student[1]
            students[student[0]]['CPF'] = student[2]
            students[student[0]]['Curso'] = student[3]

    return students

# =============================================================================

def register_students(students:dict) -> None:
    '''
        Salva o dicionário students no arquivo de texto files\students.csv
    '''

    # Line prepara os dados para armazenalos em students.csv
    line_for_csv = ''

    with open('files\students.csv', 'a') as students_table:
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

    register_students(students=students)

# =============================================================================

input_student()
print(read_students())