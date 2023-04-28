# Introducao as generator functions em python
# generator = (n for n in range(10000))

def generator(n=0, maximum=10):
  while True:
    yield n
    n += 1

    if n >= maximum:
      return

gen = generator(n=0)

for n in gen:
  print(n)