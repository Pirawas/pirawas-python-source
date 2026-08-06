i = 0
items = []
print("Enter price of 6 items:")
while i < 6:
    item = int(input(f"Item {i+1}: "))
    i = i + 1
    items.append(item)
print("\n")

budget = int(input("Enter total budget: "))
print("\n")

cur_total = 0
items_buy = []
for i in range(6):  
        if cur_total + items[i] <= budget:
            print(f"Item {i+1} = {items[i]} -> buy")
            cur_total = cur_total + items[i]
            print(f"Current total = {cur_total}")
            items_buy.append(items[i])
            print("\n")
        else:
             print(f"Item {i+1} = {items[i]} -> cannot buy")
             print(f"Current total = {cur_total}")
             print("\n")

remaining_budget = 0
remaining_budget = budget - cur_total

print(f"Bought items: {items_buy}")
print(f"Total spent: {cur_total}")
print(f"Remaining budget: {remaining_budget}")

