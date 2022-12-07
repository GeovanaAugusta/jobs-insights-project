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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


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
