import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n### OPERAÇÃO NÃO REALIZADA! SALDO INSUFICIENTE. ###")

        elif valor > 0:
            self._saldo -= valor
            print("\n### SAQUE REALIZADO COM SUCESSO! ###")
            return True

        else:
            print("\n### OPERAÇÃO NÃO REALIZADA! O VALOR INFORMADO É INVÁLIDO. ###")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n### DEPÓSITO REALIZADO COM SUCESSO! ###")
        else:
            print("\n### OPERAÇÃO NÃO REALIZADA! O VALOR INFORMADO É INVÁLIDO. ###")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n### OPERAÇÃO NÃO REALIZADA! O VALOR SOLICITADO É MAIOR QUE O LIMITE PERMITIDO. ###")

        elif excedeu_saques:
            print("\n### OPERAÇÃO NÃO REALIZADA! FOI ATINGIDO O NÚMERO MÁXIMO DE SAQUES. ###")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """\n
    -~-~-~-~-~-~-~- MENU -~-~-~-~-~-~-~-
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n### CLIENTE AINDA NÃO CADASTROU CONTA! ###")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("INFROME O CPF DO CLIENTE: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### CLIENTE NÃO ENCONTRADO! ###")
        return

    valor = float(input("INFORME O VALOR DO DEPÓSITO: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("INFORME O CPF DO CLIENTE: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### CLIENTE NÃO ENCONTRADO! ###")
        return

    valor = float(input("INFORME O VALOR DO SAQUE: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("INFORME O CPF DO CLIENTE: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### CLIENTE NÃO ENCONTRADO! ###")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n-~-~-~-~-~-~-~- EXTRATO -~-~-~-~-~-~-~-")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "NÃO FORAM REALIZADAS MOVIMENTAÇÕES."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("-~-~-~-~-~-~-~--~-~-~-~-~-~-~--~-~-~-~-")


def criar_cliente(clientes):
    cpf = input("INFORME O CPF (POR FAVOR, DIGITE APENAS NÚMEROS): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n### ESTE CPF JÁ FOI CADASTRADO! ###")
        return

    nome = input("INFORME O NOME COMPLETO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (DD-MM-AAAA): ")
    endereco = input("INFORME O ENDEREÇO COMPLETO: ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n### CLIENTE CRIADO COM SUCESSO! ###")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("INFORME O CPF DO CLIENTE: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### CLIENTE NÃO ENCONTRADO, NÃO FOI POSSÍVEL PROSSEGUIR COM ABERTURA DE CONTA! ###")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n### CONTA CRIADA COM SUCESSO! ###")


def listar_contas(contas):
    for conta in contas:
        print("-~" * 40)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q" or "Q":
            print("\n### OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS! ###")
            break
    
        else:
            print("\n### OPERAÇÃO INVÁLIDA! DIGITE NOVAMENTE A OPÇÃO DESEJADA. ###")
            return

main()