a = "AAA"
b = "BCD"
c = 1.1312312

# formato = 'a={}, b={}, c={:.2f}'.format(a, b, c)
# formato = 'a={1}, b={0}, c={2:.2f}'.format(a, b, c)

formato = 'a={1}, b={0}, c={nome3:.2f}'.format(
    a, b, nome3=c
) # Parametro Nomeado

print(formato)