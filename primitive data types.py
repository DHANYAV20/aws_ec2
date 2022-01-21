#strings
a = 'hello world'

print(a[3])
print(a[2])
print(a[6])
#list
a = [1,2,3,4]
print(a[0])
print(a[-1])
#if it is do modification it change address 
print(a[0] is a[-4])
#types of way to print 
name='batman'
msg= f"Bruce Wyane is {name}"
print(msg)
msg = "Bruce Wyane is {name}".format(name=name)
print(msg)
msg = "Bruce Wyane is {}".format(name) 
print(msg)
#1 + operator functionality in string
a1 = 'hello'
b1 = 'world'
c = a1 + b1
#2
print(c)
c = "hello" "world"
print(c)
#3
a = "hello"
b ="world"
print(a+b)
#4
c = a + ""+ b
print(c)
