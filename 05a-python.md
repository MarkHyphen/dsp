# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?  

>> Lists and tuples are sequence data types and act as an ordered collection of objects.  Lists are denoted by brackets while tuples are denoted by parentheses.  Tuples are immutable meaning that their contents cannot be changed via indexing while lists are mutable and thus objects at a specified index can be altered.  However, tuples can contain mutable objects within them such as lists.  The contents of lists and tuples can still be accessed via indexing, though. The contents of a tuple can also be accessed via unpacking.  Also, because a tuple is lacking the mutable functionality, a tuple will use less memory relative to a list.  

>> Tuples can be used as keys in dictionaries while lists cannot.  This is because of the mutable nature of the list data type and the requirement of a dictionary that a key be unique and unchanging.  Using a hashing function, a key is itself converted into an integer which acts to point to a location within a table of key,value pairs (a bucket).  Given the hash value (computed integer) will change if the key is changed, using a data type that is mutatble and thus able to be changed would promote a position where a key no loger points to the appropriate bucket (key, value pair).  Tuples, being immutatble, have the constancy that provides for stable key, value mappings.  

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?  

>> lists and sets are similar in the sense that they are data containers with the ability to have multiple elements.  Sets are datatypes that provide a means to store unordered collections of unique elements (hashable), meaning that no two elements in a set are the same.  This is different from lists where any element can contain any object, including ones that are not unique.  Given sets do not track the position of its elements, it does not support indexing and indexing-dependent methods.  Sets provide for using many mathmatical operations from within set theory (intersection, union, etc...).  Sets are implimented using dictionaries and thus have the same requirements as them in that the contents of a set must themselves be immutable.  Thus, the contents of a set can contain strings, tuples and special immutable instances of the set datatype.  Performance for finding an element within a list or set heavily favors a set for objects with large numbers of elements (it may be for lists with  elements<5 that it is faster than searching in a set).  This is because when searching a list, you are doing some form of iterative method on the whole list, which requires a lot of computational power.  Sets, however, use hashing and thus a query for membership of a set involves computing a hash value from the query that will point directly to a position within a table.  If the hash value indexed by the hashed query match, then the element is present within the set.  This is almost instantaneous.  

>> List:  
my_List=['sdf', 'sehrh', 45, 19]  
for i in range(len(my_List)):  
	print(myList[i])  

>> set:  
a = set("sdhfjkhksdf")  
b = set("hjksdfkhooasdkjhkjsdf")  
c = a.union(b)  
print(c)  


---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.  

>> Lambda functions are small code snips that act as unnamed functions that can be inserted anywhere that a normal function can be used.  Lambda functions do not need to be formally defined but rather are implimented at runtime only when needed.  They do not need to be explicitly told to return a value as they must do so by definition.  Reasons to use lamda include (1) readability of code in that you do not need to go back 300 lines to understand what the function does, (2) being concise in that explicitly declaring a formal function may take more code to impliment than using lamda, (3)  there is less "namespace" pollution in that there is not another function name that must remember, (4) lambda can be used as a value in a dictionary to make a "switch" type command that depending on an input an operation can be performed.  

>> example:  
a= [('Frank', 'USA', 'PHD'),('Antje','German','MS'),('Nathalie','French','BS')]  
sorted(a, key = lambda nation: nation[1])  

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.  

>> LIst, set, and dictionary comprehensions are a way to create a new list, set, or dictionary from iterable sequences.  This function of comprehensions are equivalent to using the map() python function.  List, set, and dictionary comprehensions also permit one to filter seqences of objects.  This function is similar to using the filter() python function.  Generally, comprehensions are preferred over using iterable built-in functions as it is considered easier to read.  However it may be more clever and more concise to use map() when using an already created function as you will need to create a dummy variable if using comprehensions (ex: map(sum, myLIst) rather than [sum(x) for x in myList]  where you must create the dummy variable x).   

>> example 1 of list comprehensions:  
new_list = [x**2 for x in [2, 4, 6]]  
print(new_list)  

>>same listcomp as example 1 using map():  
def sqr(x): return x ** 2  
new_list = list(map(sqr, [2, 4, 6]))  
print(new_list)  

>>example 2 of list comprehensions:  
new_list=[x**2 for x in [2, 3, 6] if X>4]  
print(new_list)  

>>same listcomp as example 2 using filter() and map():  
def sqr(x): return x ** 2  
new_list = list(map(sqr, filter(lambda x: x > 4, [2, 3, 6])))  
print(new_list)  

>>example of a set comprehension:  
my_set = set(range(10))  
new_set = {x**2 for x in my_set if x > 5}  
print(new_set)  

>> example of a dictionary comprehension:  
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}  
my_dict_rev = {value:key for key, value in my_dict.items()}  
print(my_dict_rev)  

---


### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'  
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





