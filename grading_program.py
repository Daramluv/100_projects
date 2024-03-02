student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

for i in student_scores:
    score = student_scores[i]
    if 91 <= score <= 100:
        student_scores[i] = "Outstanding"
    elif 81 <= score <= 90:
        student_scores[i] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_scores[i] = "Good"
    elif 61 <= score <= 70:
        student_scores[i] = "Not Good"
    else:
        student_scores[i] = "Fail"

print(student_scores)