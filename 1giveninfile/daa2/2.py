# DAA2. Implement job sequencing with deadlines using a greedy method.


def job_sequencing(jobs):
    # Each job is represented as (job_id, deadline, profit)
    jobs.sort(key=lambda job: job[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        # Find the latest available slot before the deadline
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    scheduled_jobs = [job for job in slots if job is not None]
    return scheduled_jobs, total_profit


jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

scheduled_jobs, total_profit = job_sequencing(jobs)

print("Scheduled jobs:", scheduled_jobs)
print("Total profit:", total_profit)