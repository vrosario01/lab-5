
from problem1 import pythagorean_triples

def test_pythagorean_triples_True ():
    assert pythagorean_triples(8,15,17) == True
    assert pythagorean_triples(20,21,29) == True
    assert pythagorean_triples(9,40,41) == True

def test_pythagorean_triples_False ():
    assert pythagorean_triples(8,17,15) == False
    assert pythagorean_triples(90,10,5) == False
    assert pythagorean_triples(7,5,5) == False

def test_pythagorean_triples_still_a_triangle_butfalse():
    assert pythagorean_triples(4,5,6) == False
    assert pythagorean_triples(2,2,3) == False
    assert pythagorean_triples(1,1,1) == False



