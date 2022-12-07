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

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Min_salary é maior que o valor de max_salary")


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
# Como checar se uma coluna existe numa lista
# https://www.tutorialspoint.com/how-to-check-if-a-column-exists-in-pandas
# https://statisticsglobe.com/check-if-column-exists-in-pandas-dataframe-python
# 'x1' in data.columns
# Como negar em python
# https://stackoverflow.com/questions/6117733/negation-in-python#:~:text=The%20negation%20operator%20in%20Python,just%20replace%20your%20!%20with%20not%20.&text=For%20your%20specific%20example%20(as,with%20added%20exception%20handling%20goodness.
# Checar se é string
# https://www.geeksforgeeks.org/python-check-if-a-variable-is-string/
