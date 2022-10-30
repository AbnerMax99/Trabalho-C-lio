from random import uniform

students = dict()

def register_students() -> None:
    '''
        Salva a variável students no arquivo de texto files\students.csv
    '''

    # Line prepara os dados para armazenalos em students.csv
    line = ''

    with open('files\students.csv', 'a') as students_txt:
        for row in students.keys():
            line = row

            for column in students[row].keys():
                line += ';' + str(students[row][column])

            students_txt.write(str(line +'\n'))


def input_student () -> None:
    '''
        Cadastrar alunos
    '''

    # Variável radomica
    id = str(int(uniform(1000, 9999)))

    # Input de variáveis
    name = str(input("Infome o nome do aluno: "))
    cpf = str(input("Informe o CPF do aluno: "))
    id_course = str(input("Informe o ID do curso: "))

    #cadastro das variáveis
    students[id] = dict()
    students[id]['name'] = name
    students[id]['cpf'] = cpf
    students[id]['id_course'] = id_course

    register_students()

input_student()