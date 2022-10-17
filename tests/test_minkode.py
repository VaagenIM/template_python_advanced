import pytest
"""
tests / pytest er en metode å simulere programvare på, for å sjekke at alt stemmer.

Alle python filer som starter med 'test_', f.eks. 'test_abc.py', 
kan kjøres via 'pytest' i terminalen (gitt at det er installert).

Alle funksjoner som heter 'test_*' vil da kjøres.
"""


def test_kode():
    assert (1 == 1)


def test_andreting():
    assert (1 == 1)