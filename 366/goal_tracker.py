import calendar
from datetime import date
from typing import Tuple

"""
Sample text if on-track:
Congratulations! You are on track with your steps goal. The target for 2023-01-12 is 164,383 steps and you are 11 ahead.

Sample text if not on track:
You have some catching up to do! The target for 2023-09-30 is 27,300 pages read and you are 2 behind.
"""


def goal_tracker(desc: str, annual_target: int, current_score: int, score_date: Tuple[int, int, int]):
    """Return a string determining whether a goal is on track
    by calculating the current target and comparing it with the current achievement.
    The function assumes the goal is to be achieved in a calendar year. Think New Year's Resolution :)
    """
    score_date_obj = date(*score_date)
    day_of_year = score_date_obj.timetuple().tm_yday
    days_in_year = 366 if calendar.isleap(score_date_obj.year) else 365
    per_day_goal = annual_target/days_in_year
    goal_at_target_day = int(per_day_goal*day_of_year)
    goal_delta = current_score - goal_at_target_day
    score_date_formatted = score_date_obj.strftime('%Y-%m-%d')
    print(f"{goal_delta}")
    if int(goal_delta) >= 0:
        return (
            f"Congratulations! You are on track with your {desc} goal. "
            f"The target for {score_date_formatted} is {int(goal_at_target_day):,d} "
            f"{desc} and you are {int(goal_delta):,d} ahead."
        )
    return (
        f"You have some catching up to do! "
        f"The target for {score_date_formatted} is {int(goal_at_target_day):,d} "
        f"{desc} and you are {abs(int(goal_delta)):,d} behind."
    )


if __name__ == "__main__":
    print(goal_tracker(
        "healthy snacks",
        722,
        119,
        (2000, 2, 29)))
