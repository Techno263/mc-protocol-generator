import re

def format_field_name(string):
    words = re.sub(r'[^a-zA-Z0-9]+', ' ', string).strip().split(' ')
    return '_'.join(word.lower() for word in words)

def format_class_name(string):
    words = re.sub(r'[^a-zA-Z0-9]+', ' ', string).strip().split(' ')
    return ''.join(word.lower().capitalize() for word in words)

def replace_string(input_str, replacements):
    locator = re.compile('|'.join(re.escape(s) for s in replacements.keys()))
    return locator.sub(lambda x: replacements[x.group()], input_str)
