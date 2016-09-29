"""
Utilities to prevent you from tearing your hair out 
dealing with unicode and text encodings in python 2.7
"""

import chardet


def unicode_please(text, encoding='detect', errors='ignore'):
    if isinstance(text, unicode):
        return text

    if encoding == 'detect':
        encoding = chardet.detect(text).get('encoding')

    unicode_text = text.decode(encoding, errors=errors)
    return unicode_text


def encode_please(text, encoding='detect', errors='ignore'):
    if isinstance(text, str):
        text = unicode_please(text, encoding=encoding, errors=errors)
    
    encoded_text = text.encode(encoding, errors=errors) 
    return encoded_text


"""
Aliases
"""
decode_please = unicode_please

