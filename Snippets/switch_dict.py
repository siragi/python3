#! python3
"""Source: https://data-flair.training/blogs/python-switch-case/."""


def week(i):
    """Switch Case."""
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        }
    return switcher.get(i, 'Invalid day of week')


week(2)
week(0)
week(4.5)  # 'Invalid day of week'
