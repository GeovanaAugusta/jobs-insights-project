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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

# SOURCE 3
# [{"Operator \"<>\" is not supported in Python 3; use \"!=\" instead"
# Poderia usar o len também -> len(jobInfo["industry"]) != 0:
# ou len(jobInfo["industry"]) > 0:
# https://stackoverflow.com/questions/11060506/is-there-a-not-equal-operator-in-python
