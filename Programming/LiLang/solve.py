grp = [input() for _ in range(10)]
grp2 = [input() for _ in range(10)]

longest = max(grp, key=len)
shortest = min(grp2, key=len)

out = "".join([
        (shortest[(i//2) % len(shortest)] if i%2 == 0 else "" ) + longest[i] 
            for i in range(len(longest))])
print(out)