from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    # """Reads a file from a given path and returns its contents

    # Parameters
    # ----------
    # path : str
    #     Full path to file

    # Returns
    # -------
    # list
    #     List of rows as dicts
    # """
    with open(path, encoding="utf-8") as file:
        dic_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(dic_reader)


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

# SOURCE 1
# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/b436f9e0-dfde-4a16-9bad-82f0c559dd45/day/61e88b4a-b97a-4f96-b5a0-abaa50651e37/lesson/293603be-ede4-41d6-8921-963ecdb0bc44
# import csv

# with open("graduacao_unb.csv", encoding = "utf-8") as file:
#     graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
#     # Usando o conceito de desempacotamento
#     header, *data = graduacao_reader

# print(data)
# https://linuxhint.com/use-python-csv-dictreader/
# https://docs.python.org/3/library/csv.html
