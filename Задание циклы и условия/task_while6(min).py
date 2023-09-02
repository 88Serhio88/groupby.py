A = []
for _ in range(5):
    a = int(input("Enter the integer number"))
    A.append(int(a))
m_min = A[0]

for i in A:
    if m_min > i:
        m_min = i
print(f"Min: {m_min}")


