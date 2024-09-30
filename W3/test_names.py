from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("", "") == ";"
    assert make_full_name("Jack", "Brown") == "Brown;Jack"
    assert make_full_name("Christian", "Martinez") == "Martinez;Christian"
    assert make_full_name("David","Bowie") == "Bowie;David"

def test_extract_family_name():
    assert extract_family_name("Brown; Jack") == "Brown"
    assert extract_family_name("Martinez; Christian") == "Martinez"
    assert extract_family_name("Bowie; David") == "Bowie"

def test_extract_given_name():
    assert extract_given_name("Brown; Jack") == "Jack"
    assert extract_given_name("Martinez; Christian") == "Christian"
    assert extract_given_name("Bowie; David") == "David"
 

pytest.main(["-v", "--tb=line", "-rN", __file__])