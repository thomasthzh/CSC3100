match={')':'(','}':'{',']':'['}
prio={'(':1,'{':3,'[':2}

T=int(input())
for _ in range(T):
    S=input().strip()
    stack=[]
    d=0
    valid=1

    for i in S:
        if i in "([{":
            if stack and prio[stack[-1]]<=prio[i]:
                valid=0
                break
            stack.append(i)
            d=max(d,len(stack))
        else:
            if not stack or stack[-1]!=match[i]:
                valid=0
                break
            stack.pop()
    if valid and stack:
        valid=0
    if valid:
        print(f"YES {d}")
    else:
        print("NO")