from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:

    all_industries = read(path)
    industries = set()

    for inds in all_industries:

        # A função desconsidera valores vazios
        # print(inds["industry"])
        if inds["industry"] != '':
            industries.add(inds["industry"])

    return list(industries)


# print(get_unique_industries("data/jobs.csv"))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered = []

    for job in jobs:
        # Coluna industry corresponde ao param industry
        if job["industry"] == industry:
            filtered.append(job)

    return filtered


# SOURCE 3
# [{"Operator \"<>\" is not supported in Python 3; use \"!=\" instead"
# Poderia usar o len também -> len(jobInfo["industry"]) != 0:
# ou len(jobInfo["industry"]) > 0:
# https://stackoverflow.com/questions/11060506/is-there-a-not-equal-operator-in-python

# SOURCE 7
# Como filtrar uma lista
# https://www.pythontutorial.net/python-basics/python-filter-list/

# scores = [70, 60, 80, 90, 50]

# filtered = []

# for score in scores:
#     if score >= 70:
#         filtered.append(score)

# print(filtered)
