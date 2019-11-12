'''
Ujian Job Connector Data Science
Purwadhika startup & Coding School
Selasa, 12 November 2019

S O A L  # 1
'''

'''
Diketahui : 
A = himpunan (set) bilangan genap antara 1 dan 20.
B = himpunan (set) bilangan ganjil antara 1 dan 20.
C = himpunan (set) bilangan negatif lebih dari -10.
D = himpunan (set) bilangan prima antara 1 dan 20.
E = himpunan (set) bilangan komposit antara 1 dan 20.
Definisi & kategori bilangan dapat Anda simak di laman Wikipedia. Buatlah sebuah file python (.py) yang dapat menyelesaikan permasalahan himpunan berikut:

a. A ∪ B ∪ C ∪ D ∪ E = gabungan 

b. (A ∩ B) ∪ (D ∩ E) = lirisan dalam gabungan

c. (A ∪ B) ∩ (D ∪ E) = gabungan dalam irisan

d. (A ∪ B) - (D ∪ E) = pengurangan antara gabungan

e. (A ∪ B ∪ C) - (A ∩ E) = pengurangan antara gabungan dengan irisan
'''

A = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
B = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
C = {-8, -6, -4, -2}
D = {2, 3, 5, 7, 11, 13, 17, 19}
E = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18}

op_1 = (A | B | C | D | E)
op_2 = (A & B)
op_3 = (D | E)
op_4 = (op_2 | C)
op_5 = (A & E)
op_6 = (op_2 | op_3)
op_7 = (op_2 & op_3)
op_8 = (op_2.difference(op_3))
op_9 = (op_4.differnce(op_5))

print(op_1)
print(op_6)
print(op_7)
print(op_8)
print(op_9)