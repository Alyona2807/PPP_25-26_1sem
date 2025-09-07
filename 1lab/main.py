#я выбрала задачу номер 4  
import random
N = 10
shuffles = 1000
deck = list(range(1, N + 1))
counts = [dict() for _ in range(N)]

def shuffle(arr):
    for i in range(N-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

for _ in range(shuffles):
    d = deck[:]
    shuffle(d)
    for i, num in enumerate(d):
        counts[i][num] = counts[i].get(num, 0) + 1

for i in range(N):
    print(f"Позиция {i+1}:")
    for num in range(1, N+1):
        c = counts[i].get(num, 0)
        print(f"{num}: {c} раз")

if __name__ == "__main__":
    pass 
