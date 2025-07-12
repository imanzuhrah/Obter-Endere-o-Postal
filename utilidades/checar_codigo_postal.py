# Importação do pacote de requisições de HTTP
import requests

# Função que retorna informações postais pelo CEP
def buscar_dados (cep) -> dict:

    # Constrói a URL da interface de programação do VIA CEP
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # Faz a requisição para a URL montada.
    resposta = requests.get(url)
    resposta.raise_for_status()

    # Tranforma o JSON retornado em um dicionário do Python
    dados = resposta.json()

    # Verifica se a resposta retornou um erro interno.
    if 'erro' in dados:

        # Feedback de erro ao usuário.
        return {"erro": f"O CEP {cep} não foi encontrado..."}
    
    # Retorna os dados do endereço em caso de sucesso.
    return dados