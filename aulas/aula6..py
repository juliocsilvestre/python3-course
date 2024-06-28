# Conversão de tipos, coerção
# type convertion, coercion, type casting
# é o ato de converter um tipo em outro
# tipos imutáveis e primiitivos: str,int, float e bool

print (1+1)
print ('a' + 'b')

## print ("1" + 1) ## Somar string com int não é possível
print (int("1"), type(int("1")))
print (int("1") + 1)
print (float("1"))

print (bool(''))
print (bool('a'))

print (str(11) + "b")