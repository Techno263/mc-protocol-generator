import requests
from bs4 import BeautifulSoup, element

def sort_tag_by_pos(tag):
    return (tag.sourceline, tag.sourcepos)

def parse_table(table_tag):
    table_data = [[t for t in row_tag if type(t) == element.Tag and not t.has_attr('rowspan')] for row_tag in table_tag.tbody.contents if type(row_tag) == element.Tag]
    table_head, table_rows = table_data[0], table_data[1:]
    table_head = [t.text.strip() for t in table_head]
    if (len(table_head) != 6 or 'Packet ID' not in table_head or
        'State' not in table_head or 'Bound To' not in table_head or
        'Field Name' not in table_head or 'Field Type' not in table_head or
        'Notes' not in table_head):
        return None
    table_rows = [[t for t in row_tag if type(t) == element.Tag] for row_tag in table_tag.tbody.contents if type(row_tag) == element.Tag][1:]
    packet_id = table_rows[0][0].text.strip()
    state = table_rows[0][1].text.strip()
    bound_to = table_rows[0][2].text.strip()
    table_rows = [[t for t in row if not t.has_attr('rowspan')] for row in table_rows]
    table_rows = [row[-3:] for row in table_rows if len(row) >= 2]
    if any(len(row) < 2 for row in table_rows):
        breakpoint()
    fields = [{'name': table_row[0].text.strip(), 'type': table_row[1].text.strip()} for table_row in table_rows]
    return packet_id, state, bound_to, fields

def get_gamestate_packets(tag):
    game_state = tag.text.strip()
    tag = tag.next_sibling
    destination_state = None
    packet_name = None
    packet_data = []
    while tag != None and tag.name != 'h2':
        '''
        if tag.name == 'h3':
            if tag.text != 'Clientbound' and tag.text != 'Serverbound':
                raise Exception('Invalid packet destination', tag.text)
            destination_state = tag.text
            packet_data[destination_state] = []
        '''
        if tag.name == 'h4':
            packet_name = tag.text
        elif tag.name == 'table':
            #if packet_name != None and destination_state != None:
            table_data = parse_table(tag)
            if table_data != None:
                packet_id, state, bound_to, fields = table_data
                packet_data.append({
                    'name': packet_name,
                    'packet_id': packet_id,
                    'state': state,
                    'bound_to': bound_to,
                    'fields': fields
                })
            #packet_data[destination_state][packet_name] = table_data
        tag = tag.next_sibling
    return packet_data

def get_protocol(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser').find('div', class_='mw-parser-output')
    tags = soup.find_all(['h2', 'h3', 'h4', 'table'])
    soup = BeautifulSoup(''.join(str(t) for t in tags), 'html.parser')

    #breakpoint()
    #for p_tag in soup.find_all('p'):
    #    p_tag.decompose()
    #with open('temp.html', 'wt', encoding='utf8') as fp:
    #    fp.write(''.join(str(t) for t in tags))
    #    fp.write(soup.prettify())
    game_state_tags = [
        soup.find('h2', string='Handshaking'),
        soup.find('h2', string='Status'),
        soup.find('h2', string='Login'),
        soup.find('h2', string='Play')
    ]
    game_state_tags = sorted(game_state_tags, key=sort_tag_by_pos)
    packet_data = [packet for game_state_tag in game_state_tags for packet in get_gamestate_packets(game_state_tag)]
    #packet_data = {k: v for k, v in packet_data}
    #for tag in game_state_tags:
    #    get_gamestate_packets(tag)
    return packet_data

if __name__ == '__main__':
    from protocol_list import get_protocol_links
    #links = get_protocol_links()
    #protocol = get_protocol(links['1.16.5'])
    protocol = get_protocol(r'https://wiki.vg/Protocol')
    #protocol = get_protocol(r'https://wiki.vg/index.php?title=Protocol&oldid=6003')
    with open('protocol.json', 'wt') as fp:
        import json
        json.dump(protocol, fp, indent=4)
