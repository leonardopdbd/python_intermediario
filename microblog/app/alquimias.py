from datetime import datetime

def formatar_data(data):
    """
    Formata uma data no formato 'dd/mm/yyyy'.
    """
    return data.strftime('%d/%m/%Y')

def criar_slug(nome):
    """
    Cria um 'slug' para um nome de usuário, removendo espaços e convertendo para minúsculas.
    """
    return nome.replace(" ", "-").lower()

def calcular_idade(data_nascimento):
    """
    Calcula a idade de uma pessoa a partir da sua data de nascimento.
    """
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade
