from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 500.00
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} ' \
               f'\nSaldo: R$ {self.saldo}' \
               f' \nLimite disponível: R$ {self.limite}'

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            if self.saldo < 0:
                while self.limite >= 0:
                    if valor + self.limite > 500:
                        self.limite -= self.saldo
                        self.saldo += valor
                    else:
                        self.saldo += valor
                        self.limite += valor
                    print('\nDepósito efetuado com sucesso!\n')
                    break
            else:
                self.saldo += valor
                print('\nDepósito efetuado com sucesso!\n')
        else:
            print('\nDepósito não realizado! Informe um valor válido.\n')

    def sacar(self: object, valor: float) -> None:
        if valor > 0:
            if self.saldo < 0:
                if self.limite > 0:
                    if valor <= self.limite:
                        self.saldo -= valor
                        self.limite -= valor
                        print('\nSaque efetuado com sucesso!')
                        print('ATENÇÃO: Você está na linha de crédito do cheque especial.\n')
                    else:
                        print('\nSaque não realizado! O valor informado excede seu limite disponível.\n')
                else:
                    print('\nSaque não realizado! O valor informado excede seu limite disponível.\n')
            else:
                if valor > (self.saldo + self.limite):
                    print('\nSaque não realizado! O valor informado excede seu limite disponível.\n')
                else:
                    if valor > self.saldo:
                        restante: float = self.saldo - valor
                        self.limite = self.limite + restante
                        self.saldo -= valor
                        print('\nSaque efetuado com sucesso!')
                        print('ATENÇÃO: Você está na linha de crédito do cheque especial.\n')
                    else:
                        self.saldo -= valor
                        print('\nSaque efetuado com sucesso!\n')
        else:
            print('\nSaque não realizado! Informe um valor válido.\n')

    def transferir(self: object, conta_destino: object, valor: float) -> None:
        if valor > 0:
            if self.saldo < 0:
                while self.limite >= 0:
                    if valor <= self.limite:
                        self.saldo -= valor
                        self.limite -= valor
                        conta_destino.saldo += valor
                        print('\nTransferência realizada com sucesso!')
                        print('ATENÇÃO: Você está na linha de crédito do cheque especial.\n')
                        break
                    else:
                        print('\nTransferência não realizada! O valor informado excede seu limite disponível.\n')
                        break
            else:
                if valor > (self.saldo + self.limite):
                    print('\nTransferência não realizada! O valor informado excede seu limite disponível.\n')
                else:
                    if valor > self.saldo:
                        restante: float = self.saldo - valor
                        self.limite = self.limite + restante
                        self.saldo -= valor
                        while conta_destino.limite >= 0:
                            if valor + conta_destino.limite > 500:
                                conta_destino.limite -= conta_destino.saldo
                                conta_destino.saldo += valor
                                print('\nTransferência realizada com sucesso!')
                            else:
                                conta_destino.limite += valor
                                conta_destino.saldo += valor
                            print('\nTransferência realizada com sucesso!')
                            print('ATENÇÃO: Você está na linha de crédito do cheque especial.\n')
                            break
                    else:
                        self.saldo -= valor
                        while conta_destino.limite >= 0:
                            if valor + conta_destino.limite > 500:
                                conta_destino.limite -= conta_destino.saldo
                                conta_destino.saldo += valor
                                print('\nTransferência realizada com sucesso!')
                            else:
                                conta_destino.limite += valor
                                conta_destino.saldo += valor
                                print('\nTransferência realizada com sucesso!')
                            break
        else:
            print('\nTransferência não realizada! Informe um valor válido.\n')
