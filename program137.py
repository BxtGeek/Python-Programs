"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
"""

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)
    runner_up_score = unique_scores[1] if len(unique_scores) > 1 else unique_scores[0]
    print(runner_up_score)