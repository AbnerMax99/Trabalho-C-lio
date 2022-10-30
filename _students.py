from random import uniform

students = dict()

def read_students() -> dict:
    '''
        Lê o arquivo de texto na variável students
    '''

    number = 0

    with open('files\students.csv') as students_txt:
        for line in students_txt:
            students = line

def save_students() -> dict:
    '''
        Salva a variável students no arquivo de texto files\students.csv
    '''

    with open('files\students.csv', 'w') as students_txt:
        for key in students.keys():
            students_txt.write(str(students[key]))


def register_student () -> None:
    '''
        Cadastrar alunos
    '''

    read_students()

    # Variável radomica
    id = ''
    while (id in students.keys()) == True:
        id = int(uniform(1000, 9999))

    # Input de variáveis
    name = str(input("Infome o nome do aluno: "))
    cpf = str(input("Informe o CPF do aluno: "))
    id_course = str(input("Informe o ID do curso: "))

    #cadastro das variáveis
    students[id] = dict()
    students[id]['name'] = name
    students[id]['cpf'] = cpf
    students[id]['id_course'] = id_course

    save_students()

register_student()