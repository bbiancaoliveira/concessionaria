def pularLinha():
    print('')

def mostraLinha():
    print('-' * 40)

def titulo(msg):
    mostraLinha()
    print(msg.center(40))
    mostraLinha()

def exibirMenu():
    pularLinha()
    print('1. Cadastrar cliente\n2. Alterar cliente\n3. Listar clientes\n4. Apagar clientes\n5. Cadastrar moto\n6. Alterar moto\n7. Listar motos\n8. Apagar moto\n9. Iniciar vendas\nO. Sair ')
    pularLinha()

def cadastrarClientes(clientes):

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('CADASTRO DE CLIENTES:')
    identif = int(input('Informe o CPF: '))
    nome = input('Nome completo: ')
    email = input('Email: ')

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO Clientes (CPF, nome, email)
    VALUES (?,?,?)
    """, (identif, nome, email))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()


def listarClientes(clientes):
    pularLinha()
    titulo('LISTA DE CLIENTES CADASTRADOS:')

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
    SELECT * FROM Clientes;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    pularLinha()

def alterarClientes(clientes):
    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('ALTERAR CLIENTE')
    cpf = int(input('Informe o CPF do cliente: '))
    nome_alt = input('Informe o novo nome: ')
    email_alt = input('Informe o novo email: ')

    # alterando os dados da tabela
    cursor.execute("""
    UPDATE Clientes
    SET Nome = ?, Email = ?
    WHERE CPF = ?
    """, (nome_alt, email_alt, cpf))

    conn.commit()

    print('Dados atualizados com sucesso.')

    conn.close()


    pularLinha()


def apagarClientes(clientes):
    pularLinha()

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    titulo('APAGAR CLIENTE')
    cpf = int(input('Informe o CPF do cliente: '))

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM Clientes
    WHERE cpf = ?
    """, (cpf,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

'''MOTOS'''

def cadastrarMotos(motos):
    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('CADASTRO DE MOTOS:')
    #identif = int(input('Informe o CPF: '))
    fabricante = input('Fabricante: ')
    modelo = input('Modelo: ')
    valor = float(input('Valor da moto: '))
    # clientes.append((identif, nome, idade))
    # print('Cadastrado realizado com sucesso!')
    # pularLinha()

    # inserindo dados na tabela
    cursor.execute("""
        INSERT INTO Motos (Fabricante, Modelo, Valor)
        VALUES (?,?,?)
        """, (fabricante, modelo, valor))

    conn.commit()

    print('Moto cadastrada com sucesso.')

    conn.close()


def listarMotos(motos):
    pularLinha()
    titulo('LISTA DE MOTOS CADASTRADAS:')

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
        SELECT * FROM Motos;
        """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    pularLinha()

def alterarMotos(motos):
    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('ALTERAR MOTO')
    id = int(input('Informe o ID da moto: '))
    fabricante_alt = input('Informe o novo fabricante: ')
    modelo_alt = input('Informe o novo modelo: ')
    valor_alt = float(input('Informe o novo valor: '))


    # alterando os dados da tabela
    cursor.execute("""
        UPDATE Motos
        SET Fabricante = ?, Modelo = ?, Valor = ?
        WHERE ID = ?
        """, (fabricante_alt, modelo_alt, valor_alt, id))

    conn.commit()

    print('Dados atualizados com sucesso.')

    conn.close()

    pularLinha()

def apagarMotos(motos):
    pularLinha()

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    titulo('APAGAR MOTO')
    id = int(input('Informe o ID da moto: '))

    # excluindo um registro da tabela
    cursor.execute("""
        DELETE FROM Motos
        WHERE id = ?
        """, (id,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

def iniciarVendas():

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('VENDAS DE MOTOS:')

    cpf = int(input('CPF do comprador: '))
    nome = cursor.execute('SELECT Nome from Clientes WHERE CPF = cpf')
    nome_cliente = cursor.fetchall()

    print(nome_cliente)

    modelo = input('Que moto deseja comprar? ')
    cursor.execute('SELECT Modelo from Motos WHERE Modelo = modelo')
    valor = cursor.execute('SELECT Valor from Motos WHERE modelo = Modelo')

    valor_moto = cursor.fetchall()
    print(valor_moto)

    # inserindo dados na tabela
    cursor.execute("""
            INSERT INTO Vendas (CPF_Comprador, Cliente, Moto, Valor_Gasto)
            VALUES (?,?,?,?)
            """, (cpf, modelo, nome_cliente, valor_moto))

    conn.commit()

    print('Venda cadastrada com sucesso.')

    conn.close()

def iniciarPrograma():
    clientes = []
    motos = []
    while True:
        exibirMenu()
        opcao = int(input('Escolha a opçao: '))
        if opcao == 1:
            cadastrarClientes(clientes)
        elif opcao == 2:
            alterarClientes(clientes)
        elif opcao == 3:
            listarClientes(clientes)
        elif opcao == 4:
            apagarClientes(clientes)
        elif opcao == 5:
            cadastrarMotos(motos)
        elif opcao == 6:
            alterarMotos(motos)
        elif opcao == 7:
            listarMotos(motos)
        elif opcao == 8:
            apagarMotos(motos)
        elif opcao == 9:
            iniciarVendas()
        elif opcao == 0:
            print('Programa finalizado!')
            break
        else:
            print('Opção inválida. Tente novamente.')


# Fazer sistema de vendas
# Fazer uma validaçao da entrada de 'opçao'
# Fazer um 'voltar para menu' ou 'finalizar programa' para nao ficar retornando sempre o menu de opçoes completo.


#INÍCIO DO PROGRAMA

titulo('SISTEMA CONCESSIONÁRIA')
iniciarPrograma()





