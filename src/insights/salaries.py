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

    max_salary = max(salaries)

    return max_salary


def get_min_salary(path: str) -> int:

    all_infos = read(path)
    salaries = set()
    min_salary = 1

    for salrs in all_infos:
        if salrs["min_salary"].isdigit():
            integers_salaries = int((salrs["min_salary"]))
            salaries.add(integers_salaries)

    min_salary = min(salaries)

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Alguma chave está ausente, min_salary ou max_salary")

    if int(str(job["min_salary"])) > int(str(job["max_salary"])):
        raise ValueError("Min_salary é maior que o valor de max_salary")

    if ((not str(job["min_salary"]).lstrip('-+').isdigit())
            or (not str(job["max_salary"]).lstrip('-+').isdigit())):
        raise ValueError("Alguma chave tem valores não numéricos")

    if not str(salary).lstrip('-+').isdigit():
        raise ValueError("Salário recebe um valor não numérico")

    return ((int(str(job["min_salary"])) <= int(str(salary)))
            and (int(str(job["max_salary"])) >= int(str(salary))))


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
