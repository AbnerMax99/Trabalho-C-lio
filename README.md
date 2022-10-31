# <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" width="40px"> CRUD for college.

CRUD universitário onde é possível cadastrar alunos, cursos e suas respectivas disciplinas. 


## Menu

<div align="center">

**CONTÉM AS FUNÇÕES ABAIXO**

</div>

 - **ALUNOS**
    - ✅ Incluir 
        - RA -> str
        - Nome -> str
        - CPF -> str
        - ID do curso -> str
    - ✅ Alterar 
        - _Busca pelo RA_.
    - ✅ Consultar pelo RA:
        - Exibir dados do aluno;
        - Exibir curso;
        - Exibir disciplinas.
    - ✅ Relatório Completo:
        - Exibir **todos** os alunos;
        - Exibir seus curso;
        - Exibir suas disciplinas.
    - ✅ Excluir:
        - _A busca para exclusão do aluno deverá ser realizada por meio do RA_.

 - **CADASTRO DE CURSOS**
    - Incluir
        - ID -> int
        - Nome -> str✅
        - Duração (semestres) -> int✅
    - Alterar:
        - _Busca pelo ID_
    - Consultar pelo ID:
        - Exibir dados do curso;✅
        - Exibir disciplinas.
    - Relatório: 
        - Exibir todos os cursos;✅
        - Exibir todas as disciplinas.
    
 - **DISCIPLINAS**
    - Incluir:
        - ID;
        - Nome;
        - ID do curso.


## Estrutura de _files_

Os arquivos em files/ possuem a tarefa de armazenar os dados digitados pelo usuário.

**A estrutura dos asquivos é a seguinte**

<div align='center'>

RA   | Nome do Aluno | CPF             | Curso
-----|---------------|-----------------|--------
9999 | Fulano de tal | 000.000.000-00  | TI

</div>

Os arquivos possuem extensão _csv_, seus valores são separados por ";".

No código, a primeira linha será utilizada como índice de linha para os dicionários, já os cabeçalhos são os índices de colunas.

___

Authors: [Leonardo Espindola](https://github.com/HiLeomoreira) | [Abner Max](https://github.com/AbnerMax99)
