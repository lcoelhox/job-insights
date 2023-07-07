from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        job_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        job_list = [row for row in job_reader]

        return job_list


def get_unique_job_types(path: str) -> List[str]:
    job_list = read(path)

    types = []

    for job in job_list:
        if not job["job_type"] in types:
            types.append(job["job_type"])

    return types
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_jobs = [job for job in jobs if job["job_type"] == job_type]
    if len(list_jobs) != 0:
        return list_jobs
    else:
        return []
