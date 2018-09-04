# coding=utf-8
import  datetime
import json
if(52<2):
    print '5 greater than 111111111112'

else:
    print '111111111111'

x = '5'
y = 'John'
z= float(x)
a = "Hello. World!"
print(a[2:12])
print (len(a))
print(a.lower())
print(a.upper())
print(a.split("."))
thislist = ["apple", "banana", "cherry"]
print(thislist[2])
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# print all list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print(thisdict)

  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
      print(x)
      if x == "banana":
          break


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)


x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])

# try catch
try:
    tester = 1/0
  # print(tester)
except:
  print("An exception occurred")
