import operator as o
from random import randint
a=randint(11,20)
b=randint(1,11)
print("number 1: ",a,"\nnumber 2: ",b)
print("Here we are goingn to see all the unctions which are available in operator library")
val=o.add(a,b)
print("Add function result is: ",val)
val=o.sub(a,b)
print("Sub function result is: ",val)
val=o.mul(a,b)
print("Mul function result is: ",val)
val=o.truediv(a,b)
print("Div function result is: ",val)
val=o.floordiv(a,b)
print("Floordiv function result is: ",val)
val=o.mod(a,b)
print("Mod function result is: ",val)
val=o.pow(a,b)
print("Pow function result is: ",val)
val=o.is_(a,b)
print("Is function result is: ",val)
val=o.is_not(a,b)
print("Is_not function result is: ",val)
val=o.or_(a,b)
print("Or function result is: ",val)
val=o.invert(a)
print("Invert function result is: ",val)
val=o.and_(a,b)
print("And function result is: ",val)
val=o.xor(a,b)
print("XOR function result is: ",val)
val=o.lt(a,b)
print("lt function result is: ",val)
val=o.le(a,b)
print("le function result is: ",val)
val=o.gt(a,b)
print("gt function result is: ",val)
val=o.ge(a,b)
print("ge function result is: ",val)
val=o.eq(a,b)
print("ep function result is: ",val)
val=o.ne(a,b)
print("ne function result is: ",val)