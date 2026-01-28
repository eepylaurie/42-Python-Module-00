def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_days(day: int, days_total: int) -> None:
        if day > days_total:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_days(day + 1, days_total)

    count_days(1, days)
