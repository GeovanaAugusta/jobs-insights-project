from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:

    all_infos = read(path)
    salaries = set()
    max_salary = 1

    for salrs in all_infos:
        if salrs["max_salary"].isdigit():
            integers_salaries = int((salrs["max_salary"]))
            salaries.add(integers_salaries)
            # print(salaries)

    max_salary = max(salaries)
    # print(max_salary)
    return max_salary


# print(get_max_salary("data/jobs.csv"))


def get_min_salary(path: str) -> int:

    all_infos = read(path)
    salaries = set()
    min_salary = 1

    for salrs in all_infos:
        if salrs["min_salary"].isdigit():
            integers_salaries = int((salrs["min_salary"]))
            salaries.add(integers_salaries)
            # print(salaries)

    min_salary = min(salaries)
    # print(min_salary)
    return min_salary


# print(get_min_salary("data/jobs.csv"))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Alguma chave está ausente, min_salary ou max_salary")

    # int só pode ser usado em string, então tem que converter tudo
    # ou o teste questiona isso, str e int com > <
    if int(str(job["min_salary"])) > int(str(job["max_salary"])):
        raise ValueError("Min_salary é maior que o valor de max_salary")

    # Transformar tudo em string para assim verificar se tem alguma que não
    # vem com valor num, afinal, os inteiros que vierem já tenho essa garantia
    if ((not str(job["min_salary"]).lstrip('-+').isdigit())
            or (not str(job["max_salary"]).lstrip('-+').isdigit())):
        raise ValueError("Alguma chave tem valores não numéricos")

    # Teste falha quando testa um salário -1 e isdigit não abrange número -
    # print(not str(salary).isdigit())
    # if not str(salary).isdigit():
    if not str(salary).lstrip('-+').isdigit():
        raise ValueError("Salário recebe um valor não numérico")

    # TypeError: '<=' not supported between instances of 'int' and 'str'
    # Mesma coisa, tudo deve ficar como int
    return ((int(str(job["min_salary"])) <= int(str(salary)))
            and (int(str(job["max_salary"])) >= int(str(salary))))


# print(matches_salary_range({'max_salary': 10000, 'min_salary': 200}, -1))


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

# SOURCE 4
# Checar se um número é inteiro:
# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
# Como é o && no python
# https://stackoverflow.com/questions/2485466/pythons-equivalent-of-logical-and-in-an-if-statement
# https://www.w3schools.com/python/ref_func_max.asp#:~:text=The%20max()%20function%20returns,an%20alphabetically%20comparison%20is%20done.

# SOURCE 5
# https://realpython.com/python-min-and-max/

# SOURCE 8
# Como lançar erro
# https://dcc.ufrj.br/~jonathan/python/docs/Excecoes%20em%20Python.pdf
# https://stackoverflow.com/questions/4393268/how-to-raise-a-valueerror
# Como checar se uma coluna existe numa lista
# https://www.tutorialspoint.com/how-to-check-if-a-column-exists-in-pandas
# https://statisticsglobe.com/check-if-column-exists-in-pandas-dataframe-python
# 'x1' in data.columns
# Como negar em python
# https://stackoverflow.com/questions/6117733/negation-in-python#:~:text=The%20negation%20operator%20in%20Python,just%20replace%20your%20!%20with%20not%20.&text=For%20your%20specific%20example%20(as,with%20added%20exception%20handling%20goodness.
# Checar se é string
# https://www.geeksforgeeks.org/python-check-if-a-variable-is-string/
# Transformar em número
# https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=To%20convert%2C%20or%20cast%2C%20a,int(%22str%22)%20.
# isdigit não considera negativo como numérico, e aí?
# https://stackoverflow.com/questions/37472361/how-do-i-check-if-a-string-is-a-negative-number-before-passing-it-through-int
# https://www.folkstalk.com/tech/python-isdigit-negative-with-code-examples/
# lstrip() remove espaço ou algum item específico que esteja pela esquerda,
# rstrip pela direita.
# Mais de uma condição num if em py
# https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/
# if ((age>= 8) and (age<= 12)):
