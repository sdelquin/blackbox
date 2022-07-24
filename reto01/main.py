def filter_by_year(dates: list[str], year: int) -> list[str]:
    return [date for date in dates if int(date.split('-')[0]) == year]


assert filter_by_year(['2020-1-4', '2019-4-7', '2021-12-11', '2020-8-9'], 2020) == [
    '2020-1-4',
    '2020-8-9',
]
