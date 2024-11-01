from flask import Blueprint, render_template, request, redirect
from database.cliente import CLIENTES
from database.interface import ContaBancaria

cliente_route = Blueprint("cliente", __name__)

@cliente_route.route("/")
def lista_cliente():
    return render_template("lista_clientes.html", clientes=CLIENTES)

@cliente_route.route("/", methods=["POST"])
def consultar_cliente():
    cliente_consulta = ContaBancaria.consultarCPF(request.form.get("cpf"))
    if(cliente_consulta != None):
        return render_template("ver_cliente.html", cliente=cliente_consulta)
    else:
        cliente_consulta = {"nome": f'Cliente com o CPF: {request.form.get("cpf")} não existe.'}
        return render_template("cliente_inexistente.html", cliente=cliente_consulta)

@cliente_route.route("/criar", methods=["POST"])
def criar_cliente():
    ContaBancaria(request.form.get("nome"), request.form.get("cpf"))
    return redirect("/cliente", code=302)


@cliente_route.route("/criar")
def criar_form_cliente():
    return render_template("criar_form_cliente.html")

@cliente_route.route("/<int:cliente_id>")
def ver_cliente(cliente_id):
    cliente_consulta = None
    
    cliente_consulta = ContaBancaria.verCliente(cliente_id)
    if(cliente_consulta != None):
        return render_template("ver_cliente.html", cliente=cliente_consulta)
    else:
        cliente_consulta = {"nome": f"Cliente com o ID: {cliente_id} não existe."}
        return render_template("cliente_inexistente.html", cliente=cliente_consulta)

@cliente_route.route("/<int:cliente_id>/depositar", methods=["POST"])
def depositar_valor(cliente_id):
    for i in CLIENTES:
        if i['id'] == cliente_id:
            print(request.form.get("valor"))  
            ContaBancaria.depositar(cliente_id, request.form.get("valor"))
            return redirect(f"/cliente/{cliente_id}")

@cliente_route.route("/<int:cliente_id>/sacar", methods=["POST"])
def sacar_valor(cliente_id):
    for i in CLIENTES:
        if i['id'] == cliente_id:
            if(float(request.form.get("valor")) <= float(i['saldo_atual'])):
                ContaBancaria.sacar(cliente_id, request.form.get("valor"))
                return redirect(f"/cliente/{cliente_id}")
            else:
                return redirect(f"/cliente/{cliente_id}?saldo=false")
               
            