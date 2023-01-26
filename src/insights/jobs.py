from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, encoding="utf-8") as file:
        dic_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(dic_reader)


def get_unique_job_types(path: str) -> List[str]:

    all_jobs = read(path)
    types_of_jobs = set()

    for job in all_jobs:
        types_of_jobs.add(job["job_type"])
    return list(types_of_jobs)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:

        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
