n = int(input())
scores = list(map(int, input().split()))

# remove duplicates
unique_scores = list(set(scores))

# sort in descending order
unique_scores.sort(reverse=True)

# runner-up score
print(unique_scores[1])
