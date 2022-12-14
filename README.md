# Lab10PerfectionistPancakes
Recursion Warmup Lab

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input.

# Scenario
You have been hired as a new employee at a perfectionist-run cafe. The owners are very particular about how they like things organized, so they have decided to implement a robot to do some of the work for them. You are in charge of coding the robot. Attached is some of the code you have already written.

# Step 1
Complete the following questions in the comments at the top of your code. If your answer is multiple lines, use these: \``` around your answer:

1. Take a look at the flow diagram below. This is the flow diagram for separateOrders(str). On a piece of paper, or something separate, make a flow diagram for onePlateToAnother() and show it to a TA when you're done.
2. What is the output for onePlateToAnother(\[“blueberry”, “strawberry”, “choco chip”]?
3. What is the base case for onePlateToAnother(pancakes)?
4. What is the output for main() when this is the input?:
maple
Y
strawberry 
y 
birthday cake
n 
double chocolate

```mermaid
graph TD;
    A{separateOrders} -->|has more than one item| B(has a Comma);
    B --> C[remove left-most item before the comma and add to list];
    C --> |loop with new string| A;
    A --> |last item| D(no commas) --> E[add last item to list] --> F{return the finished list};
```


# Step 2: Coding orderUp(totalNum, orders)
Now it’s your turn! Write a function that takes in the initial number of orders and a list of orders (this will be a list of strings) and then RECURSIVELY adds each order to a string as: “Order #_, your order of _ pancakes is up!\n".

For Example, for 
```python
orderUp(3, [“blueberry, strawberry”, “plain, whole wheat”, “banana nut, birthday cake, chocolate chip”])
# the output would be:
# “Order #1, your order of [“strawberry”, “blueberry”] pancakes is up!”
# “Order #2, your order of [“whole wheat”, “plain”] pancakes is up!”
# “Order #3, your order of [“chocolate chip”, “banana nut”, “birthday cake”] pancakes is up!”
```
(Hint: there is already a function for turning strings into lists, and there is a function for reversing the pancakes)

# Step 3: Test orderUp(totalNum, orders)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().
```python
print("TESTING", orderUp(3, [“blueberry, strawberry”, “plain, whole wheat”, “banana nut, birthday cake, chocolate chip”]))
```
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Lists
Think of lists as cubbies or drawers. Each entry in the list contains an item, and you can access them by using the number on the drawer, or the index of the entry. Technically, strings are lists of characters, so we can do things like substring our lists, as you will see in the example code, and it works the same way. You give it a range of indexes that you want to look at.

# Reminder on Using Functions Within Functions
If you are ever writing a function and you already have a function that does part of the work, just call that function in your function! For example, if I am writing a function called fact3(num) that finds the factorial of a number and multiplies it by 3 and I have a function called factorial(number) that gets the factorial, then I may write fact3(num) like this:
```python
def fact3(num):
   facto = factorial(num)
   return facto * 3
```
# Reminder on Recursion
This warmup uses pancake stacks to try to emulate the order of operations for recursion. When writing anything with recursion, it can help to write out what is happening or what your pancake stack looks like. Recursion works like making a stack fo pancakes and moving it from one plate to another. You stack up the pancakes on the first plate in order, in the same way that your code will stack up calls to the recursive function, until it reaches the last pancake, or the base case. Now you're done making pancakes and you can start moving them to the other plate--in your code, this is where the code will read the code that comes after the function call. However, if you're moving pancakes, you have to start with the top pancake or they might tear. WHich means you start with the LAST function call and work all the way back to the first time the function is called. 

# Reminder on Base Cases
A base case is the condition the code must meet in recursion to stop looping. Typically, this is a special if statement and if the if statement is false, it calls itself again. For example, with 
```python
def recurs(num):
    if num <= 0:
        return 1
    return num + recurs(num - 1)
```
The function will continue looping until num reaches 0.
