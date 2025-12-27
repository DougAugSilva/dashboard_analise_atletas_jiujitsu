import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import product
import time

# Extrai o html da pagina toda
def get_page_content(url, headers, params):
    # Corrigido: usando os argumentos passados para a função
    try:
        response = requests.get(url=url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

def parse_athletes(soup, k, c, g, b, d):
    table = soup.find('table')
    if not table:
        return None
    
    athletes = []
    # Busca o corpo da tabela para evitar o header
    tbody = table.find('tbody')
    rows = tbody.find_all('tr') if tbody else table.find_all('tr')[1:]
    
    if not rows:
        return None

    for row in rows:
        try:
            # Posição
            position_cell = row.find('td', class_='position')
            position = position_cell.get_text(strip=True) if position_cell else "N/A"

            # Foto
            photo_cell = row.find('td', class_='photo reduced')
            photo = photo_cell.find('img')['src'] if photo_cell and photo_cell.find('img') else None

            # Nome e Links
            name_div = row.find('div', class_='name')
            if not name_div: continue
            name_tag = name_div.find('a')
            name = name_tag.get_text(strip=True)
            details = DOMAIN + name_tag['href']

            # Academia
            academy_cell = row.find('div', class_='academy')
            academy = academy_cell.get_text(strip=True) if academy_cell else "N/A"

            # Pontuação
            points_cell = row.find('td', class_='pontuation')
            points = points_cell.get_text(strip=True) if points_cell else "0"

            athlete = {
                'Position': position,
                'Photo': photo,
                'Name': name,
                'Details': details,
                'Academy': academy,
                'Points': points,
                'Kimono': k,
                'Category': c,
                'Gender': g,
                'Belt': b,
                'Division': d
            }
            athletes.append(athlete)
        except Exception as e:
            continue
            
    return athletes                                            

# Retorna os filtros que mudam as tabelas no site
def list_filters(soup, filter_id):
    if not soup: return []
    select_box = soup.find(id=filter_id)
    if not select_box: return []
    filters = select_box.find_all('option')
    # Retorna o valor se existir, pulando o primeiro item (geralmente o "Select All")
    return [item['value'] for item in filters if item.get('value') and item['value'] != ""]


# Configurações Iniciais
DOMAIN = 'https://ibjjf.com'
URL = f'{DOMAIN}/2025-athletes-ranking'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

# https://ibjjf.com/2025-athletes-ranking

# Parâmetros base
PARAMETERS = {
    'filters[age_division]': 'adult',
    'filters[belt]': 'black',
    'filters[gender]': 'male',
    'filters[limit]': '10',
    'filters[s]': 'ranking-geral-gi',
    'page': 1
}

# Coleta inicial para pegar os filtros
filter_soup = get_page_content(URL, HEADERS, PARAMETERS)

# Mapeamento dos filtros baseados no ID do HTML
kimono = list_filters(filter_soup, 'filters_s')
category = list_filters(filter_soup, 'filters_ranking_category')
gender = list_filters(filter_soup, 'filters_gender')
belt = list_filters(filter_soup, 'filters_belt')
division = list_filters(filter_soup, 'weight_filter')

all_athletes = []
limit = 30

# Filtrando
category = ['adult']
belt = ['black']
kimono = ['ranking-geral-gi']

# Loop de Extração
for k, c, g, b, d in product(kimono, category, gender, belt, division):
    page = 1 # Reinicia a página para cada nova combinação
    while True and page <= limit:
        # Corrigido: Uso de = para atribuição
        PARAMETERS['filters[s]'] = k
        PARAMETERS['filters[age_division]'] = c
        PARAMETERS['filters[gender]'] = g 
        PARAMETERS['filters[belt]'] = b
        PARAMETERS['filters[limit]'] = d
        PARAMETERS['page'] = page
        
        print(f"Extraindo: {k}, {c}, {g}, {b}, {d} | Página: {page}")
        
        soup_athletes = get_page_content(URL, HEADERS, PARAMETERS)
        athletes = parse_athletes(soup_athletes, k, c, g, b, d)
        
        # Se não houver mais atletas ou a tabela sumir, para o loop daquela categoria
        if not athletes:
            break
            
        all_athletes.extend(athletes)
        page += 1
        time.sleep(1) # Delay amigável para o servidor

# Exportação
if all_athletes:
    df_atletas = pd.DataFrame(all_athletes)
    df_atletas.to_csv('atletas.csv', sep=';', index=False, encoding='utf-8-sig')
    print(f"Sucesso! {len(all_athletes)} atletas exportados.")
else:
    print("Nenhum dado foi coletado.")