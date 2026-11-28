# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-28, 08:24 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        cmd = input().split()
        operation = cmd[0]
        
        if operation == "insert":
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif operation == "print":
            print(arr)
        elif operation == "remove":
            arr.remove(int(cmd[1]))
        elif operation == "append":
            arr.append(int(cmd[1]))
        elif operation == "sort":
            arr.sort()
        elif operation == "pop":
            arr.pop()
        elif operation == "reverse":
            arr.reverse()
