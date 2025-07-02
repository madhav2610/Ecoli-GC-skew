import matplotlib.pyplot as plt


def Minimumskew(genome):
    position = []
    skew = SkewArray(genome)
    m = min(skew)
    for i in range(len(skew)):
        if(m==skew[i]):
            position.append(i)
    return position

def SkewArray(genome):
    skew= [0]
    n = len(genome)
    for i in range(n):
        if(genome[i]=="A"or genome[i]=="T"):
            skew.append(skew[-1])
        elif(genome[i]=="G"):
            skew.append(skew[-1]+1)
        elif(genome[i]=="C"):
            skew.append(skew[-1]-1)
    return skew


with open("ecoli.fna") as f:
    lines = f.readlines()


genome = ""
for line in lines:
    if line.startswith(">"):
        continue
    cleaned_line = line.strip()
    genome = genome + cleaned_line

result = Minimumskew(genome)


with open("result.txt","w") as f1:
    f1.write("Minimum Skew Positions(likely origin of replication): \n")
    f1.write(str(result))

skew_values = SkewArray(genome)
positions = list(range(len(skew_values)))
plt.figure(figsize=(15,5))
plt.plot(positions,skew_values,color = 'red')
plt.title("Skew diagram of e.coli")
plt.xlabel("Positions")
plt.ylabel("skew(G-C)")
plt.grid(True)
plt.tight_layout()

for i in range(len(result)):
  pos = result[i]
  skew_value = skew_values[pos]
  if(i==0):
    plt.scatter(pos,skew_value,color ='blue',label = "Minimum skew")
  else:
    plt.scatter(pos,skew_value,color='blue')

plt.tight_layout()
plt.legend()
plt.savefig("SkewMinimumGraph")
plt.show()

