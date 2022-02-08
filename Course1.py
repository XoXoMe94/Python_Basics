
##ex1
x=2
print(x)


##ex2
x=5
if x<10:
    print('smaller')
if x>20:
    print('bigger')
print('finish')



##ex3
n=5
while n>0:
    print(n)
    n=n-1
print('Sara')


##ex4 add int
a=1+2
print(a)

#ex5 add str
a='hello ' + 'Sara'
print(a)


#ex6 error type
a='sa' + 'ra'
a=a+1
print(a)


#ex7 get type
a='sara'
type(a)


#ex8  change type
a=float(13)
print(a)


#ex9 division
print(10/2)


#ex10 input
name=input('your name?')
print('welcome',name)


#ex11 if else 
x=4
if x>2:
    print('bigger')
else:
        print('smaller')
print('all done')



#ex12 elif
x=4
if x<2:
    print('small')
elif x<10:
    print('medium')
else:
    print('large')
print('All done')



#ex13 try and except
astr='Hello bob'
try:
    print('sara')
    astr=int(astr)
except:
    astr= -1
print('First',astr)



#ex14 def
def thing():
    print('sara')
    print("Haghighi")
thing()
print('hey')
thing()



#ex15 max
big=max('Sara Haghighi')
print(big)



#ex16 min
small=min('Sara haghighi')
print(small)



#ex17 parameters def
def greet(lang):
    if lang=='en' :
        print('hello')
    elif lang=='es' :
        print('Hola')
    else :
        print('Bonj')
        
greet('en')


#ex18 parameters def return
def greet(lang):
    if lang=='en' :
        return ('hello')
    elif lang=='es' :
        return ('Hola')
    else :
        return ('Bonj')
        
print(greet('es') , 'sara')



#ex19 def 
def add(a,b):
    added=a+b
    return added

x=add(3,5)
print(x)



#ex20 loop
n=5
while n>0:
    print('lather')
    print('rinse')
print('Dry off')



#ex21 break loop
while True:
    line=input('>')
    if line=='done' :
        break 
    print(line)
print('done')



#ex22 continue
while True :
    line=input('>')
    if line[0]=='#':
        continue
    elif line=='done' :
        break
    print(line)
print('done')



#ex23 for
for i in [5,4,3,2,1]:
    print(i)
print('done')



#ex24 for list
friends=['sara','Alex','rose']
for friend in friends:
    print('happy new year', friend)
print('done')



#ex25 finding the largest
largest_so_far=-1
print('before',largest_so_far)
for num in [9,41,12,3,74,15]:
    if num>largest_so_far :
        largest_so_far=num
    print(largest_so_far, num)
print('after',largest_so_far)
    
    
    
#ex26 avg 
count=0
sum=0
print('before', count, sum)
for i in [3,5,6]:
    count=count+1
    sum=i+sum 
    print(count,sum,i)
print('after',count,sum,sum/count)



#ex27 search
found=False
print('before',found)
for i in [3,4,7]:
    if i==3:
        found=True
    print(found,i)
print('after',found)
    


#ex28 smallest value
smallest = None
print('before')
for i in [3,5,7]:
    if smallest is None :
        smallest=i
    elif i<smallest:
        smallest=i
    print(smallest,i)
print('after',smallest)
        
    
    
    
    
    
    
    