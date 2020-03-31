gen1= open ('AY274119.txt', 'r+')
gen2= open('AY278488.2.txt', 'r+')
gen3= open('MN908947.txt', 'r+')
gen4= open('MN988668.txt', 'r+')
gen5= open('MN988669.txt', 'r+')
lista1= [gen1, gen2, gen3, gen4, gen5]
lista2=[]
#Vamos a convertir los archivos en una lista de strings, y la formula a emplear será:
# ( Número de caractéres iguales / Cantidad más larga de caractéres )  * 100
#Se hará una tabla que muestre el porcentaje de similitud
for x in lista1:
    x= x.read().replace('\n', '')
    lista2.append(x)
def mas_l(a, b):                        
    if len(a)>=len(b):
        return len(a)        
    else:
        return len(b)
def iguales(a,b):
    cont=0
    for x in range(min(len(a),len(b))):
        if a[x]==b[x]:
            cont+=1
    return cont
def comparo(a,b):
    eq=(iguales(a,b)/mas_l(a,b))*100
    eq=round(eq,2)
    return eq
#print(comparo(lista2[0],lista2[1]))
def tabla(list,a,b):
    for i in range(6):
        if i==0:
            print('\t', end='')
        else:
            print('gen'+str(i), end='\t')
    print()                
    for j in range(1,6):
        for i in range(6):
            if i == 0:
                print('gen'+str(j), end='\t')
            else:
                print(comparo(lista2[i-1],lista2[j-1]), end='\t')
        print()
print(tabla(lista2,lista2[0],lista2[1]))

#listo=['ambrosia', 'armoniaa']

#        lista_x=[line.rstrip('\n') for line in x]
##        list_x=x.readlines()
##        for y in list_x:
##            print(y)
#        for line in x:
#            print(line)
#            return lista_x
#hacerlista(lista)
#print(hacerlista(lista))
#m=lista_gen1=[line.rstrip('\n') for line in gen1]


