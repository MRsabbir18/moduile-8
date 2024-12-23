def full_name(frist, last):
    name = f'{frist}{last}'
    return name

#name = full_name('alu', 'kodu')
#name = full_name('Alu', 'kodu')
name = full_name(last='kodu', first='Alu')
print(name)

def famus_name(first, last, title, addition):
  name = f'{title} {first} {last}'
  return name

name = famus_name(first='Taher' , last='Ali', title='hujur', addition='taheirr')
print(name) 
