 # Importa o módulo local de consulta do CEP.
from utilidades import checar_codigo_postal

# Solicita o CEP.
cep = input("Digite o CEP para consulta: ").strip()

# chama a função importada para buscar os dados postais.
resultado = checar_codigo_postal.buscar_dados(cep)

# Verifica se foi retornado algum erro.
if "erro" in resultado:

    # Exibe a mensagem de erro.
    print(f"Erro: {resultado['erro']}")


# Se não houver erro, exibe os dados postais.
else:

    #Exibe o endereço postal completo.
    print(f"CEP: {resultado.get('cep', 'N/A')}")
    print(f"Logradouro: {resultado.get('logradouro', 'N/A')}")
    print(f"Bairro: {resultado.get('bairro', 'N/A')}")
    print(f"Cidade: {resultado.get('localidade', 'N/A')}")
    print(f"Estado: {resultado.get('uf', 'N/A')}")
