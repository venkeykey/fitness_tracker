from scipy.constants import calorie

gym_data =[]

for _ in range(1):
    name = input("Enter your name: ")
    calorie = int(input(f"Enter calories burned by {name}: "))
    gym_data.append({"name": name, "calories": calorie})
target_calories = 400
sorted_gym_data = sorted(gym_data, key=lambda k:k['calories'], reverse=True)
print("Top calorie burners")
for i, gym in enumerate(sorted_gym_data, start=1):
    print(f"{i}. {gym['name']}- {gym['calories']} calories burned")

top_calorie_burners= sorted_gym_data[:3]

print("\n 🏆 Top Performers: ")
for i, gym in enumerate(top_calorie_burners, start=1):
    print(f"{i}. {gym['name']} - {gym['calories']} calories burned")

met_target = [gym for gym in sorted_gym_data if gym['calories'] >= target_calories]
print("\nIndividuals who met the target: ")
if met_target:
    for i, gym in enumerate(met_target, start=1):
        print(f"{i}.{gym['name']}: {gym['calories']} calories burned")
else:
        print("No one met target")