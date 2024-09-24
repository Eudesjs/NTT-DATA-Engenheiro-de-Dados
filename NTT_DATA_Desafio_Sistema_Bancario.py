# Função Menu()

import textwrap

def menu():
    menu = """\n
    ++++++++++BEM VINDO AO MENU+++++++++++++++++++++++
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [Nc]\tNova Conta
    [Lc]\tListar Conta
    [Nu]\tNovo Usuário
    [Sa]\tSair

    """
    return input(textwrap.dedent(menu))

# Função Depositar()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n@@@ Deposito Realizado com Sucesso! ===")
    else:
        print("\n@@@ Operação Falhou! O valor informado é invalido. @@@")

    return saldo, extrato

# Função Sacar()

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação Falhou! Você nao tem Saldo Suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação Falhou! O Valor de Saque Excede o Limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação Falhou! Numero Máximo de Saque Excedido @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n@@@ Saque realizado com Sucesso @@@")
    else:
        print("\n Operação Falhou! O Valor Informado é Inválido. ")

    return saldo, extrato

