from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    job_list = read(path)

    return max(
        [
            int(job["max_salary"])
            for job in job_list
            if job["max_salary"].isdigit()
        ]
    )
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    job_list = read(path)

    return min(
        [
            int(job["min_salary"])
            for job in job_list
            if job["min_salary"].isdigit()
        ]
    )
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or not str(job["max_salary"]).isdigit()
        or not str(job["min_salary"]).isdigit()
        or type(salary) not in [int, str]
        or not int(job["max_salary"]) > int(job["min_salary"])
    ):
        raise ValueError("Something is wrong")

    return (
        (
            job["min_salary"]
            if type(job["min_salary"]) == int
            else int(job["min_salary"])
        )
        <= (salary if type(salary) == int else int(salary))
        <= (
            job["max_salary"]
            if type(job["max_salary"]) == int
            else int(job["max_salary"])
        )
    )
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    job_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list.append(job)
        except ValueError as erro:
            print(f"Error: {erro}")
    return job_list
    raise NotImplementedError
