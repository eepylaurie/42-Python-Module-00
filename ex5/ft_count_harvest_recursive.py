def print_days(i, days_until_harvest):
    if i > days_until_harvest:
        return
    print(f"Day {i}")
    print_days(i + 1, days_until_harvest)


def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    print_days(1, days_until_harvest)
    print("Harvest time!")
