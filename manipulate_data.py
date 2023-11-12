import os 

import os 
import json

# Type hints
from typing import List, Dict, Union, Any

def load_json_file(folder_name: str, file_name: str) -> Union[List[Dict[str, str]], None]:
    '''
    Carrega as informações da lista armazenada em um arquivo JSON. 

    Parameters:
    -----------
    folder_name: str
        Nome da pasta onde o arquivo JSON está armazenado.
    file_name: str
        Nome do arquivo JSON.

    Returns:
    --------
    result: list
        Lista com as informações do arquivo JSON.
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, folder_name, file_name + '.json')
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        data = json.load(f)
        result = [[v for _,v in restaurant.items()] for restaurant in data]
    return result

def save_json_file(folder_name: str, file_name: str, data: List[List[Any]], column_name: List[str]) -> None:
    '''
    Armazena as informações da lista para um arquivo JSON.

    Parameters:
    -----------
    folder_name: str
        Nome da pasta onde o arquivo JSON será armazenado.
    file_name: str
        Nome do arquivo JSON.
    data: list
        Lista com as informações a serem armazenadas.
    column_name: list
        Lista com os nomes das colunas da lista.
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Se a pasta não existir, cria a pasta
    if not os.path.exists(os.path.join(current_dir, folder_name)):
        os.makedirs(os.path.join(current_dir, folder_name))
    
    file_path = os.path.join(current_dir, folder_name, file_name + '.json')
    data_json = [{k:v for k,v in zip(column_name, restaurant)} for restaurant in data]
    with open(file_path, 'w') as f:
        json.dump(data_json, f, indent=4)

if __name__ == '__main__':
    # Cria uma lista referente aos restaurantes para serem salvos
    restaurants = [['Restaurante A', 'Endereço A', 'Telefone A', 'Especialidade A'], ['Restaurante B', 'Endereço B', 'Telefone B', 'Especialidade B']]
    # Cria uma lista com os nomes das colunas
    column_names = ['Nome', 'Endereço', 'Telefone', 'Especialidade']
    # Salva a lista no arquivo JSON
    save_json_file('Cadastro', 'Restaurante', restaurants, column_names)
    # Carrega a lista do arquivo JSON
    result = load_json_file('Cadastro', 'Restaurante')
    # Imprime a lista
    print(result)
