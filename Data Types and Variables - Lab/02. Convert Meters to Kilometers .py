# Format to second decimal

meters = int(input())
kilometers = meters/1000
print(f"{kilometers:.2f}")

# Can use Round if I want to not show the 0 in the example above
# print(f"{round(kilometers,2)}") - Result 1.5 not 1.50