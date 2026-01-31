def ft_count_harvest_recursive(
        days_left: int | None = None, day: int = 1) -> None:
    if days_left is None:
        days_left = int(input("Days until harvest: "))
    if days_left == 0:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(days_left - 1, day + 1)
