from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Python") == 1639

# SOURCE 10
# Exercício 4 - Testes
