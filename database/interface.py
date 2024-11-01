from database.cliente import CLIENTES
class ContaBancaria:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo_atual = 0
        
        novo_usuario = {
            "id": len(CLIENTES) + 1,
            "nome": self.nome,
            "cpf": self.cpf,
            "saldo_atual": 0
        }
        CLIENTES.append(novo_usuario)

    def sacar(id, valor):
        for i in CLIENTES:
            if i['id'] == id:
                if(i['saldo_atual'] >= float(valor)):
                    i['saldo_atual'] -= float(valor)


    def depositar(id, valor):
        for i in CLIENTES:
            if i['id'] == id:
                i['saldo_atual'] += float(valor)

    def verCliente(id):
        for i in CLIENTES:
            if i['id'] == id:
                return i
    
    def consultarCPF(cpf):
        for i in CLIENTES:
            if i['cpf'] == cpf:
                return i
