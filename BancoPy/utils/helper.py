import re
from datetime import datetime, date


def verifica_tipo(opcao: str) -> bool:
    return opcao.isdigit()


def validar_cpf(cpf: str) -> bool:
    if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return True


def validar_nome(nome: str) -> bool:
    if re.match(r'([A-Z]+)', nome):
        return True
    return False


def validar_email(email: str) -> bool:
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return True
    return False


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
