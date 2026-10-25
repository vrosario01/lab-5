from problem3 import print_range
### because the function print_range prints the values instead of returning them, you need to use capsys from pytest for the test files 
### capsys is a fixture that allows you to capture the output of the print statements in your function. using this you can then compare the actual output to the expected output .

def test_print_range_decimals(capsys):
    print_range(0.5, 2.5, 0.5)
    assert capsys.readouterr().out == "0.5\n1.0\n1.5\n2.0\n"
    print_range(0, 3, 1.5)
    assert capsys.readouterr().out == "0\n1.5\n"

def test_print_range_negatives(capsys):
    print_range(-2, 4, 2) 
    assert capsys.readouterr().out == "-2\n0\n2\n"
    print_range(-10, -5, 2)
    assert capsys.readouterr().out == "-10\n-8\n-6\n"

def test_print_range(capsys):
    print_range(1, 5, 2)
    assert capsys.readouterr().out == "1\n3\n"
