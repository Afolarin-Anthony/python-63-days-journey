# Class Score Analyzer

import statistics

scores = [75, 80, 92, 67, 88, 95, 72]

print(f"Number of Students : {len(scores)}")
print(f"Highest Score      : {max(scores)}")
print(f"Lowest Score       : {min(scores)}")
print(f"Average Score      : {statistics.mean(scores):.2f}")
print(f"Median Score       : {statistics.median(scores)}")
