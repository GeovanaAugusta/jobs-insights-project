from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[2] == {
        "title": "Analista de Software",
        "salary": "4000",
        "type": "full time",
    }


# SOURCE 11
# Exercício 4 - Testes
