from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta
from utils.helper import verifica_tipo, validar_cpf, validar_nome, validar_email


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==========================================')
    print('================= ATM ====================')
    print("=========== Wellington's Bank ============")
    print('==========================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')
    print('==========================================')

    while True:
        opcao: str = input('Digite a opção desejada: ')
        if verifica_tipo(opcao):
            if opcao == '1':
                criar_conta()
            elif opcao == '2':
                efetuar_saque()
            elif opcao == '3':
                efetuar_deposito()
            elif opcao == '4':
                efetuar_transferencia()
            elif opcao == '5':
                listar_contas()
            elif opcao == '6':
                print('\nVolte sempre!')
                sleep(2)
                exit(0)
            else:
                print('Opção inválida.')
                sleep(2)
                menu()
        else:
            print('A opção desejada deve ser um número de 1 a 6. Tente novamente.')
            sleep(1)
            continue


def criar_conta() -> None:
    print('--------------------------------')
    print('| Informe os dados do cliente  |')
    print('--------------------------------')
    print("\n(Para retornar ao menu principal, digite '0' seguido de 'Enter')\n")
    sleep(1)
    while True:
        nome: str = input('Nome do cliente: ')
        if nome == '0':
            menu()
        else:
            if validar_nome(nome):
                break
            else:
                print('Nome inválido. Por favor, digite novamente.')
                sleep(1)
                continue
    while True:
        email: str = input('E-mail do cliente: ')
        if email == '0':
            menu()
        else:
            if validar_email(email):
                break
            else:
                print('E-mail inválido. Por favor, digite novamente.')
                sleep(1)
                continue
    while True:
        cpf: str = input('CPF do cliente: ')
        if cpf == '0':
            menu()
        else:
            if validar_cpf(cpf):
                break
            else:
                print("CPF inválido. Por favor, digite no seguinte formato: '123.456.789-09'.")
                sleep(2)
                continue
    while True:
        data_nascimento: str = input('Data de nascimento do cliente: ')
        if data_nascimento == '0':
            menu()
        else:
            try:
                cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
                conta: Conta = Conta(cliente)
                contas.append(conta)
                break
            except ValueError:
                print('Por favor, digite no seguinte formato: dd/mm/aaaa')
                sleep(2)
                continue
    print('')
    print('Conta criada com sucesso!')
    print('')
    print('Dados da conta: ')
    print('-----------------')
    print(conta)
    sleep(3)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        print("\n(Para retornar ao menu principal, digite '0' seguido de 'Enter')\n")
        sleep(1)
        while True:
            try:
                numero: int = int(input('Informe o número da sua conta: '))
                break
            except ValueError:
                print('Por favor, digite somente números. Tente novamente.')
                sleep(1)
                continue
        if numero == 0:
            menu()
        else:
            conta: Conta = buscar_conta_por_numero(numero)
            if conta:
                valor: float = float(input('Informe o valor do saque: '))
                conta.sacar(valor)
            else:
                print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('\nAinda não existem contas cadastradas.\n')
    sleep(3)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        print("\n(Para retornar ao menu principal, digite '0' seguido de 'Enter')\n")
        sleep(1)
        numero: int = int(input('Informe o número da sua conta: '))
        if numero == '0':
            menu()
        else:
            conta: Conta = buscar_conta_por_numero(numero)
            if conta:
                valor: float = float(input('Informe o valor do depósito: '))
                conta.depositar(valor)
            else:
                print(f'Não foi encontrada uma conta com número {numero}')
    else:
        print('\nAinda não existem contas cadastradas.\n')
    sleep(3)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        print("\n(Para retornar ao menu principal, digite '0' seguido de 'Enter')\n")
        sleep(1)
        numero_o: int = int(input('Informe o número da sua conta: '))
        if numero_o == '0':
            menu()
        else:
            conta_o: Conta = buscar_conta_por_numero(numero_o)
            if conta_o:
                numero_d: int = int(input('Informe o número da conta destino: '))
                conta_d: Conta = buscar_conta_por_numero(numero_d)
                if conta_d:
                    valor: float = float(input('Informe o valor da transferência: '))
                    conta_o.transferir(conta_d, valor)
                else:
                    print(f'A conta destino com número {numero_d} não foi encontrada.')
            else:
                print(f'A sua conta com número {numero_o} não foi encontrada.')
    else:
        print('\nAinda não existem contas cadastradas.\n')
    sleep(3)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('')
        print('--------------------')
        print('Listagem de contas')
        print('--------------------')
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(2)
        print('')
    else:
        print('\nNão existem contas cadastradas.\n')
        sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
