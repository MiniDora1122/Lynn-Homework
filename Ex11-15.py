#Ex 11
def calculate(num1,operator,num2):
    if(operator=="+"):
        return num1+num2
    elif (operator=="-"):
        return num1-num2
    elif (operator=="*"):
        return num1*num2
    elif (operator=="/"):
        return num1/num2

print(calculate(10,"+",10))
print(calculate(10,"-",10))
print(calculate(10,"*",10))
print(calculate(10,"/",10))


#Ex 12
def check_string(input):
    if input.startswith("The"):
        return "Yes!"
    else:
        return "No!"
    
str1 = "The"
str2 = "Thumbs up"
str3 = "Theatre can be boring"
print(check_string(str1))
print(check_string(str2))
print(check_string(str3))


#Ex 13
count=0
while count <5:
    count +=1
    print(count)


#Ex 14
countries = ['Malaysia','Japan','Armenia','Brazil','Australia']
for country in countries:
 print("come and visit " + country)
 
 
#Ex15
import random
flowers = ['rose','tulip','lily']
n = random.randint(0,100)
print(random.choice(flowers))
print(n)
