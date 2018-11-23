def profit(work_time_week, normal):
    if work_time_week < normal:
        print("Not soo!")
    else:
        print("Good gob!")

amount_of_time = int(input("How much time for a work you spend last week:"))

profit(amount_of_time, 40)
