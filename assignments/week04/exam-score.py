i = 0
scores = []
while i < 5:
    score = int(input(f"Enter score of student {i+1}: "))
    i = i + 1
    scores.append(score)

for i in range(5):
    if scores[i] >= 50:
        print(f"Student {i+1}: {scores[i]} -> ผ่าน")
    else:
        print(f"Student {i+1}: {scores[i]} -> ไม่ผ่าน")