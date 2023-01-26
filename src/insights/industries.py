from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:

    all_industries = read(path)
    industries = set()

    for inds in all_industries:

        if inds["industry"] != '':
            industries.add(inds["industry"])

    return list(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered = []

    for job in jobs:

        if job["industry"] == industry:
            filtered.append(job)

    return filtered
