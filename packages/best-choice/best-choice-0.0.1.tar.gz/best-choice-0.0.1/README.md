# best-choice
## 1 - pip Install
```
pip install best-choice
```
## 2 - all function
```
#library
from bestchoice import Generate

#data
#object,price,importance level
table = [['pants',75,10],
         ['jeans',50,7],
         ['shirt',45,8],
         ['dress',65,7],
         ['ball',25,5]]

#call function generate
gen = Generate(table)

#all possibilities
for x in gen.list_all():
  print(x)

#call function to generate calculation results
#parameters 1 and 2 are columns for calculation
#in this case, the price and importance level
calc = gen.list_results([1,2])

#all calculated results
for x in calc:f
  print(x)

#new table after filter
#the first parameter 1 and 2 are index columns
#the second parameter 1 <= 200 filter your new table  
new = gen.list_best([1,2],[[1,'<=',200]])

#all filtered results
for x in new:
  print(x)
```

## 3 - example to find best choice
```
#library
from bestchoice import Generate

#data
#object,price,importance level
table = [['pants',75,10],
         ['jeans',50,7],
         ['shirt',45,8],
         ['dress',65,7],
         ['ball',25,5]]

#column for calculation
#in this case, the price and importance level
columns = [1,2]

#index of column importance
importance = 2

#filters where 1 is the price <= 200 dollars
filters = [[1,'<=',200]]

#call function generate
gen = Generate(table)

#get all possibilities
lista = gen.list_all()

#new table after filter
#the first parameter 1 and 2 are index columns
#the second parameter 1 <= price filter your new table 
res = gen.list_best(columns,filters)

#saves the best filtered result
top = max([sublist[-1] for sublist in res])

filters.append([importance,'==',top])
#table with new result
new = gen.list_best(columns,filters)

#set index of top values
best = [x[0] for x in new][0]

#result
print(f'This is your best choice: {", ".join([str(x[0]) for x in lista[best]])}')

```