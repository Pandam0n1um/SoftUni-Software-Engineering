line=input()

counts={}

for char in line:
    if char not in counts:
        counts[char]=0
    counts[char]+=1

counts_sorted=sorted(counts.items(),key=lambda x: ord(x[0]))

for letter,occurence in counts_sorted:
    print(f"{letter}: {occurence} time/s")