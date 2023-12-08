def study_schedule(permanence_period, target_time):
    if target_time is None or any(
        period is None or len(period) != 2 or not all(isinstance(val, int)
                                                      for val in period)

        for period in permanence_period
    ):
        return None

    count_of_periods = sum(start <= target_time <=
                           end for start, end in permanence_period)
    return count_of_periods
