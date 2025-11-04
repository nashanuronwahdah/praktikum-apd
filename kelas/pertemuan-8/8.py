num = int("42") # 42
name = str(123) # "123"
data = list("abc") # ['a', 'b', 'c']
data = dict(a=1, b=2) # {'a': 1, 'b': 2}
print(type(num)) # <class 'int'>

angka = 20
print(bin(angka))

buah = frozenset(["apel", 'jeruk', 'mangga'])

# angka = [1, 2,3,4,5]
# print(max(angka))

angka = 3.999
print(round(angka))


# pangkat
angka = 3
print(pow(angka, 5))

print(pow(2,2,5))

print(divmod(17,5))

buah = ['apel','pisang','mangga']
angka = 0 
for item in buah:
    angka += 1
    print(angka, item)
    
    
angka = [1,2,3,4,5,6]
genap = filter(lambda x: x % 2 == 0, angka)
print(list(genap))

angka = [10, 20, 30]
it = iter(angka)
print(next(it))
print(next(it))
print(next(it))

nama = 'daFFa anak jahat'
# print(nama.lower())
# print(nama.replace('jahat', 'baik'))

huruf = 'a,b,c'
print(huruf.split(","))
print(huruf.split("."))

huruf = 'a.b.c'
print(nama.find('z'))



