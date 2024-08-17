#Tupla
#Tuplas são inalteraveis
#Toda tupla é definida com parêntesis e vírgula
tuplaUm = (1,2)
print("O tipo da variável é", type(tuplaUm))

for i in tuplaUm:
    print(i)

#Matriz em Tupla
tuplaDois = (('A2','B2','C2'),(3,2,1))
for j in tuplaDois:
    print(j)

#Esse tipo de alteração, realiza uma mudança definitiva na variável de memória.
print("Tupla UM ", tuplaUm)
print("Tupla DOIS ", tuplaDois)
tuplaDois += tuplaUm
print("Tupla UM somado a tupla DOIS ", tuplaUm+tuplaDois)

