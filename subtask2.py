n = 0
s = 0
a = 0
m = 1234567890

print("Enter numbers for the sequence:")

while True:
    x = int(input("Enter number:"))
    if x == -1:
        break
    n += 1
    s += x
    if m > x:
        m = x

if n == 0:
    m = -1
    a = -1
else:
    a = s / n
print(f"Count(n): {n}") 
print(f"Sum(s): {s}") 
print(f"Minimum(m): {m}") 
print(f"Mean(a): {a}")
# it looks like I learned how to use
git today