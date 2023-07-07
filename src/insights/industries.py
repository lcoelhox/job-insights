from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    job_list = read(path)

    industries_list = [
        item["industry"] for item in job_list if item["industry"] != ""
    ]

    return list(set(industries_list))
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]

    raise NotImplementedError
