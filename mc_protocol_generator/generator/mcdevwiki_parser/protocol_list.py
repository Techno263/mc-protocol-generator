import requests
from bs4 import BeautifulSoup

base_url = r'https://wiki.vg'
protocol_version_num_url = r'https://wiki.vg/Protocol_version_numbers'

def table_filter(tag):
    self_check = tag.name == 'tr'
    parent_check = tag.parent.name == 'tbody'
    child_check = any(c.name == 'td' for c in tag.children)
    return self_check and parent_check and child_check

def get_row_data(row):
    try:
        name_tag, _, page_tag = row.find_all('td')
        name = name_tag.text.strip()
        page = page_tag.find('a', string='page')['href'].strip()
        if 'wiki.vg' not in page:
            if page[0] not in ['/', '\\']:
                page = '/' + page
            page = base_url + page
        return name, page
    except:
        return None

def get_protocol_links():
    r = requests.get(protocol_version_num_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    rows = [row for table in tables for row in table.find_all(table_filter)]
    data = {}
    for row in rows:
        rd = get_row_data(row)
        if rd != None:
            name, page = rd
            data[name] = page
    return data

if __name__ == '__main__':
    data = get_protocol_links()
    with open('data.json', 'wt') as fp:
        import json
        json.dump(data, fp, indent=4)
