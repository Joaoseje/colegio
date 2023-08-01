
import json
import copy#não vi utilidade dessa biblioteca no meu código, mas está aí 

def ler_json(file_name):
    data = []
    try:
        with open(file_name + '.json', 'r') as f:
            data = json.load(f)
            f.close()# vou fechar só por desencargo de consciência
            return data
    except FileNotFoundError:
        try:
            escrever_json(data, file_name)
            return data
        except PermissionError:
            print("Sem permissão para escrever, mas será retornado uma lista")
            return data

def escrever_json(data, file_name):
    try:
        with open(file_name + '.json', 'w') as f:
            json.dump(data, f, indent=4)
            f.close()#acredito que não precisa fechar pq o "with" garante isso
    except PermissionError:
        print("sem permissão para escrever")

tabela_e = "estudantes"
lista_estudantes = ler_json(tabela_e)

tabela_p = "professores"
lista_professores = ler_json(tabela_p)

tabela_d = "disciplinas"
lista_disciplinas = ler_json(tabela_d)

tabela_t = "turmas"
lista_turmas = ler_json(tabela_t)

tabela_m = "matriculas"
lista_matriculas = ler_json(tabela_m)

def incluir_estudante(lista, file_name):
    novo_estudante = {}
    while True:
        matricula_estudante = input("Crie uma matrícula para um novo aluno (ou 'fim' para encerrar a adição de estudantes): ")
        if matricula_estudante == 'fim':
            break
        aluno_encontrado = False
        for aluno in lista:
            if aluno['matricula'] == matricula_estudante:
                aluno_encontrado = True
                break
        if not aluno_encontrado:
            novo_estudante['nome'] = input("Informe o nome do estudante: ")
            novo_estudante['matricula'] = matricula_estudante
            novo_estudante['curso'] = input("Informe o curso do estudante: ")
            print("Estudante adicionado com sucesso!")
            lista.append(novo_estudante)
            escrever_json(lista, file_name)
        else:
            print("Matrícula existente, tente novamente!")
    

def listar_estudante(lista):
    for estudante in lista:
        print("Nome: ", estudante['nome'])
        print("Matrícula: ", estudante['matricula'])
        print("Curso: ", estudante['curso'])
        print("-" * 30)


def atualizar_estudante(lista, matricula, file_name):
    for estudante in lista:
        if estudante['matricula'] == matricula:
            estudante['nome'] = input("Informe o novo nome do estudante: ")
            estudante['curso'] = input("Informe o novo curso do estudante: ")
            print("Estudante atualizado!")
            escrever_json(lista, file_name)
            return
    print("Estudante não encontrado.")


def excluir_estudante(lista, matricula, file_name):
    for estudante in lista:
        if estudante['matricula'] == matricula:
            lista.remove(estudante)
            escrever_json(lista, file_name)
            return
    print("Estudante não encontrado.")

def incluir_professor(lista, file_name):
    novo_professor = {}
    while True:
        codigo_professor = input("Crie um código para o novo professor (ou 'fim' para encerrar a adição de professores): ")
        if codigo_professor == 'fim':
            break
        encontrado = False
        for professor in lista:
            if professor['codigo'] == codigo_professor:
                encontrado = True
                break
        if not encontrado:
            novo_professor['nome'] = input("Informe o nome do professor: ")
            novo_professor['codigo'] = codigo_professor
            novo_professor['disciplina'] = input("Informe a disciplina do professor: ")
            print("Professor adicionado com sucesso!")
            lista.append(novo_professor)
            escrever_json(lista, file_name)
        else:
            print("Código sendo usado, tente usar um diferente!")

def listar_professor(lista):
    for professor in lista:
        print("Nome: ", professor['nome'])
        print("Código: ", professor['codigo'])
        print("Disciplina: ", professor['disciplina'])
        print("-" * 30)

def atualizar_professor(lista, codigo, file_name):
    for professor in lista:
        if professor['codigo'] == codigo:
            professor['codigo'] = input("Informe o novo código do professor: ")
            professor['nome'] = input("Informe o novo nome do professor: ")
            professor['disciplina'] = input("Informe a nova disciplina do professor: ")
            print("Professor atualizado com sucesso!")
            escrever_json(lista, file_name)
            return
    print("Professor não encontrado.")

def excluir_professor(lista, codigo, file_name):
    for professor in lista:
        if professor['codigo'] == codigo:
            lista.remove(professor)
            print("Professor excluído com sucesso!")
            escrever_json(lista, file_name)
            return
    print("professor não encontrado.")

def incluir_disciplina(lista, file_name):
    nova_disciplina = {}
    while True:
        codigo = input("Crie um código para a nova disciplina (ou 'fim' para encerrar a adição de disciplinas): ")
        if codigo == 'fim':
            break
        encontrado = False
        for disciplina in lista:
            if disciplina['codigo'] == codigo:
                encontrado = True
                break
        if not encontrado:
            nova_disciplina['nome'] = input("Informe o nome da disciplina: ")
            nova_disciplina['codigo'] = codigo
            nova_disciplina['carga_horaria'] = int(input("Informe a carga horária da disciplina: "))
            print("disciplina adicionada com sucesso!")
            lista.append(nova_disciplina)
            escrever_json(lista, file_name)
        else:
            print("Código sendo usado, tente novamente!")


def listar_disciplina(lista):
    for disciplina in lista:
        print("Código: ", disciplina['codigo'])
        print("Nome: ", disciplina['nome'])
        print("Carga Horária: ", disciplina['carga_horaria'])
        print("-" * 30)

def atualizar_disciplina(lista, codigo, file_name):
    for disciplina in lista:
        if disciplina['codigo'] == codigo:
            disciplina['codigo'] = input("Informe o novo código da disciplina: ")
            disciplina['nome'] = input("Informe o novo nome da disciplina: ")
            disciplina['carga_horaria'] = int(input("Informe a nova carga horária da disciplina: "))
            print("Disciplina atualizada com sucesso!")
            escrever_json(lista, file_name)
            return
    print("Disciplina não encontrada.")

def excluir_disciplina(lista, codigo, file_name):
    for disciplina in lista:
        if disciplina['codigo'] == codigo:
            lista.remove(disciplina)
            print("Disciplina excluída com sucesso!")
            escrever_json(lista, file_name)
            return
    print("Disciplina não encontrada.")

def incluir_turma(lista, lista_disciplinas, lista_professores, lista_estudantes, file_name):
    nova_turma = {}
    nova_turma['codigo'] = input("Informe o código da turma: ")
    
    while True:
        codigo_disciplina = input("Informe o código da disciplina: ")
        disciplina_encontrada = False
        for disciplina in lista_disciplinas:
            if disciplina['codigo'] == codigo_disciplina:
                disciplina_encontrada = True
                nova_turma['disciplina'] = disciplina
                break
        if disciplina_encontrada:
            break
        else:
            print("Disciplina não encontrada.")
    
    while True:
        codigo_professor = input("Informe o código do professor da turma: ")
        professor_encontrado = False
        for professor in lista_professores:
            if professor['codigo'] == codigo_professor:
                professor_encontrado = True
                nova_turma['professor'] = professor
                break
        if professor_encontrado:
            break
        else:
            print("Professor não encontrado.")
    
    nova_turma['estudantes'] = []
    while True:
        matricula_estudante = input("Informe a matrícula do aluno a ser adicionado à turma (ou 'fim' para encerrar a seleção de alunos): ")
        if matricula_estudante == 'fim':
            break
        aluno_encontrado = False
        for aluno in lista_estudantes:
            if aluno['matricula'] == matricula_estudante:
                aluno_encontrado = True
                novo_aluno = {'matricula': aluno['matricula'], 'nome': aluno['nome']}
                nova_turma['estudantes'].append(novo_aluno)
                break
        if not aluno_encontrado:
            print("Aluno não encontrado.")
    
    lista.append(nova_turma)
    escrever_json(lista, file_name)


def listar_turma(lista):
    for turma in lista:
        print("Código: ", turma['codigo'])
        print("Disciplina: ", turma['disciplina'])
        print("Professor: ", turma['professor'])
        print("Estudantes: ", turma['estudantes'])
        print("-" * 30)

def atualizar_turma(lista, codigo, file_name):
    for turma in lista:
        if turma['codigo'] == codigo:
            turma['professor'] = input("Informe o novo código do professor da turma: ")
            print("Turma atualizada com sucesso!")
            escrever_json(lista, file_name)
            return
    print("Turma não encontrada.")

def excluir_turma(lista, codigo, file_name):
    for turma in lista:
        if turma['codigo'] == codigo:
            lista.remove(turma)
            print("Turma excluída com sucesso!")
            escrever_json(lista, file_name)
            return
    print("Turma não encontrada.")

def atualizar_matricula(matricula, lista, file_name):
    for estudante in lista:
        if estudante['matricula'] == matricula:
            estudante['matricula'] = input("Informe a nova matrícula do estudante: ")
            print("Matrícula atualizada com sucesso!")
            escrever_json(lista, file_name)
            return
    print("Estudante não encontrado.")
    

def limpar_tela():
    print('\n' * 100)
def crud():
    print("\n(1) Incluir."'\n')
    print("(2) Listar."'\n')
    print("(3) Atualizar."'\n')
    print("(4) Excluir"'\n')
    print("(5) Voltar ao menu principal.""\n")
    
def menup():
    print("---- MENU PRINCIPAL ---" "\n")
    print("(1) Gerenciar estudantes."'\n')
    print("(2) Gerenciar professores."'\n')
    print("(3) Gerenciar disciplinas."'\n')
    print("(4) Gerenciar turmas."'\n')
    print("(5) Gerenciar matrícula."'\n')
    print("(6) Sair." "\n")
    
continuar = True
while continuar :
    while True:
        limpar_tela()
        menup()
        try:
            menu = int(input("Informe a opção desejada:"))
            if menu <= 0 or menu > 6:
                print("Opção deve ser entre 1 e 6")
            else:
                break
        except ValueError:
            print("Opção inválida")
    while True:
        if menu == 1 :
            limpar_tela()
            print(" [ESTUDANTES] MENU DE OPERAÇÕES")
            crud()
            try:
                est = int(input("Informe a opção desejada: "))
                if est <= 0 or est > 5:
                    print("Opção deve ser entre 1 e 5")
                    continue
                if est == 1:
                    incluir_estudante(lista_estudantes, tabela_e)
                if est == 2:
                    listar_estudante(lista_estudantes)
                if est == 3:
                    atualizar_estudante(lista_estudantes, input("Informe a matrícula do estudante a ser atualizado: "), tabela_e)
                if est == 4:
                    excluir_estudante(lista_estudantes, input("Informe a matrícula do estudante a ser excluído: "), tabela_e)
                if est == 5:
                    break
            except ValueError:
                print("Opção inválida ")
        if menu == 2 :
            limpar_tela()
            print("  [PROFESSORES] MENU DE OPERAÇÕES")
            crud()
            try:
                prof = int(input("Informe a opção desejada: "))
                if prof <= 0 or prof > 5:
                    print("Opção deve ser entre 1 e 5")
                    continue
                if prof == 1:
                    incluir_professor(lista_professores, tabela_p)
                if prof == 2:
                    listar_professor(lista_professores)
                if prof == 3:
                    atualizar_professor(lista_professores, input("Informe o código do professor a ser atualizado: "), tabela_p)
                if prof == 4:
                    excluir_professor(lista_professores, input("Informe o código do professor a ser excluído: "), tabela_p)
                if prof == 5:
                    break
            except ValueError:
                print("Opção inválida ")
        if menu == 3 :
            limpar_tela()
            print("  [DISCIPLINAS] MENU DE OPERAÇÕES")
            crud()
            try:
                disc = int(input("Informe a opção desejada: "))
                if disc <= 0 or disc > 5:
                    print("Opção deve ser entre 1 e 5")
                if disc == 1:
                    incluir_disciplina(lista_disciplinas, tabela_d)
                if disc == 2:
                    listar_disciplina(lista_disciplinas)
                if disc == 3:
                    atualizar_disciplina(lista_disciplinas, input("Informe o código da disciplina a ser atualizada: "), tabela_d)
                if disc == 4:
                    excluir_disciplina(lista_disciplinas, input("Informe o código da disciplina a ser excluída: "), tabela_d)
                if disc == 5:
                    break
            except ValueError:
                print("Opção inválida ")
        if menu == 4 :
            limpar_tela()
            print("  [TURMAS] MENU DE OPERAÇÕES")
            crud()
            try:
                turm = int(input("Informe a opção desejada: "))
                if turm <= 0 or turm > 5:
                    print("Opção deve ser entre 1 e 5")
                    continue
                if turm == 1:
                    incluir_turma(lista_turmas, lista_disciplinas, lista_professores, lista_estudantes, tabela_t)
                if turm == 2:
                    listar_turma(lista_turmas)
                if turm == 3:
                    atualizar_turma(lista_turmas, input("Informe o código da turma a ser atualizada: "), tabela_t)
                if turm == 4:
                    excluir_turma(lista_turmas, input("Informe o código da turma a ser excluída: "), tabela_t)
                if turm == 5:
                    break
            except ValueError:
                print("Opção inválida ")
        if menu == 5 :
            limpar_tela
            print("  [MATRÍCULA] MENU DE OPERAÇÕES")
            crud()
            try:
                matr = int(input("Informe a opção desejada: "))
                if matr <= 0 or matr > 5:
                    print("Opção deve ser entre 1 e 5")
                    continue
                if matr == 1:
                    incluir_estudante(lista_estudantes, tabela_e)
                if matr == 2:
                    listar_estudante(lista_estudantes)
                if matr == 3:
                    atualizar_matricula(input("Informe a matrícula a ser atualizada: "), lista_estudantes, tabela_e)

                if matr == 4:
                    excluir_estudante(lista_estudantes, input("Informe o código da matrícula a ser excluída: "), tabela_e)
                if matr == 5:
                    break
            except ValueError:
                print("Opção inválida ")
        if menu == 6:
            limpar_tela()
            print("Finalizando o programa ")
            continuar = False
            break
        