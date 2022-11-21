# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

print("Please input a list of scores")
scores = input()

clean_scores = scores.replace(",", "")
scores_list = clean_scores.split()

highest_score = 0

for score in scores_list:
    score_int = int(score)
    if score_int >= highest_score:
        highest_score = score_int

print(highest_score)
