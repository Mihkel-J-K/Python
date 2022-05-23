metadata = input().split(" ")
K = int(metadata[0])
M = int(metadata[1])
data = []
for i in range(K):
    data += [input().split(" ")]
analyzed = sorted(data, key= lambda f: [[int((f**2)%M)]], reverse= True)
print(data)