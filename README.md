#  CRUD python 

CRUD universitário onde é posssível cadastrar alunos, cursos e suas respectivas disciplinas. 


## Menu

<div align="center">

**Deverá conter as funções abaixo**

</div>

 - **ALUNOS**
    - Incluir ✅
        - RA -> str
        - Nome -> str
        - CPF -> str
        - ID do curso -> str
    - Alterar ✅
        - _Busca pelo RA_.
    - Consultar pelo RA:
        - Exibir dados do aluno;
        - Exibir curso;
        - Exibir disciplinas.
    - Relátório Completo:
        - Exibir **todos** os alunos;
        - Exibir seus curso;
        - Exibir suas disciplicas.
    - Excluir:
        - _A busca para exclusão do aluno deverá ser realizda por meio do RA_.

 - **CADASTRO DE CURSOS**
    - Incluir
        - ID -> int
        - Nome -> str
        - Duração (semestres) -> int
    - Alterar:
        - _Busca pelo ID_
    - Consultar pelo ID:
        - Exibir dados do curso;
        - Exibir disciplinas.
    - Relatório: 
        - Exibir todos os cursos;
        - Exibir todas as disciplinas.
    
 - **DISCIPLINAS**
    - Incluir:
        - ID;
        - Nome;
        - ID do curso.


## Estrutura de _files_

Os arquivos em files/ possuem a tafera de armazenar os dados digitados pelo usuário.

<div align='center'>

**A estrutura dos asquivos é a seguinte**

RA   | Nome do Aluno | CPF             | Curso
-----|---------------|-----------------|--------
9999 | Fulado de tal | 000.000.000-00  | TI

</div>

Os arquivos possuem extenção _csv_, seus valores são separados por ";".

No coódico, a primera linha será utilizada como índice de linha para os dicionário, já os cabeçalhos são os índices de colunas.