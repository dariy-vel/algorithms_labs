from Calendar import Calendar

calendar = Calendar([(0, 1), (3, 5), (4, 8), (10, 12), (9, 11)])
calendar.optimize()
print(calendar.output_list)
