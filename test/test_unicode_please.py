import chardet

from unicode_please import unicode_please, encode_please, decode_please
from .sample_ascii import sample_ascii
from .sample_utf8 import sample_utf8
from .sample_unicode import sample_unicode_from_ascii, sample_unicode_from_utf8

def test_ascii_to_unicode():
    assert isinstance(sample_ascii, str)
    unicode_text = unicode_please(sample_ascii)
    assert isinstance(unicode_text, unicode)
    assert unicode_text.encode('ascii') == sample_ascii


def test_utf8_to_unicode():
    assert isinstance(sample_utf8, str)
    unicode_text = unicode_please(sample_utf8)
    assert isinstance(unicode_text, unicode)
    assert unicode_text.encode('utf-8') == sample_utf8


def test_unicode_to_ascii():
    assert isinstance(sample_unicode_from_ascii, unicode)
    ascii_text = encode_please(sample_unicode_from_ascii, encoding='ascii')
    assert isinstance(ascii_text, str)
    assert ascii_text.decode('ascii') == sample_unicode_from_ascii


def test_unicode_to_utf8():
    assert isinstance(sample_unicode_from_utf8, unicode)
    utf8_text = encode_please(sample_unicode_from_utf8, encoding='utf-8')
    assert isinstance(utf8_text, str)
    assert utf8_text.decode('utf-8') == sample_unicode_from_utf8


def test_utf8_to_ascii():
    assert isinstance(sample_utf8, str)
    ascii_text = encode_please(sample_utf8, 'ascii')
    assert isinstance(ascii_text, str)

    # lossy process
    assert ascii_text != sample_utf8


def test_ascii_to_utf8():
    assert isinstance(sample_ascii, str)
    utf8_text = encode_please(sample_ascii, 'utf-8')
    assert isinstance(utf8_text, str)
    assert utf8_text == sample_ascii
