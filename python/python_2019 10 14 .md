#python
```
#10-1

root@kali:/# gedit test1.py

print("hello!")
print(3*2*(17-2.1))
print("abc"+"def")
word = "art"
print(word.replace("r", "n"))

root@kali:/# python3 test1.py
1 / 2 = 0.5
1/2=0.5
```


```
#10-2

root@kali:/# gedit test2.py

a= 1
b= 2
c = a/b
print(a, "/", b, "=", c) 
add = str(a)+"/"+str(b)+"="+str(c)
print(add) 

root@kali:/# python3 test2.py
1 / 2 = 0.5
1/2=0.5
```

```
#10-3

root@kali:/# gedit test3.py

input("Where do you live? ")
print("I live in Boston. ")

root@kali:/# python3 test3.py
Where do you live?  輸入:123
I live in Boston.
```

```
#10-4

root@kali:/# gedit test4.py

user_place = input("Where do you live? ")
text = user_place.capitalize()+ "!"
print(text) 
print("I hear it's nice there!") 

root@kali:/# python3 test4.py
Where do you live? 
輸入:123
123!
I hear it's nice there!

```

```
#10-5

root@kali:/# gedit test5.py

num = int(input ("Enter a number to find the square of: "))
user_input = input("Enter a integer to find the square of: ")
num = int(user_input) 
print(num*num)

root@kali:/# python3 test5.py

Enter a number to find the square of: 12  輸入:12
Enter a integer to find the square of: 21  輸入:21
441
```

```
#10-6

root@kali:/# gedit test6.py

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(num1, "*", num2, "=", num1*num2)
 
root@kali:/# python3 test6.py
Enter a number: 12 輸入:12
Enter another number: 21  輸入:21
12.0 * 21.0 = 252.0
```
