A = []
for _ in range(5):
    a = int(input('Введите целое число...'))
    A.append(int(a))
m_max = A[0]
for i in A:
    if m_max < i:
        m_max = i

print(f'Максимальное: {m_max}')




