# J. Два прямоугольника

Недавно один известный художник-абстракционист произвел на свет новый шедевр — картину «Два черных непересекающихся прямоугольника». Картина представляет собой прямоугольник m &times; n, разбитый на квадраты 1 &times; 1, некоторые из которых закрашены любимым цветом автора — черным. Федя — не любитель абстрактных картин, однако ему стало интересно, действительно ли на картине изображены два непересекающихся прямоугольника. Помогите ему это узнать. Прямоугольники не пересекаются в том смысле, что они не имеют общих клеток.
## Input

Первая строка входного файла содержит числа m и n (1 &le; m, n &le; 200). Следующие m строк содержат описание рисунка. Каждая строка содержит ровно n символов. Символ «.» обозначает пустой квадрат, а символ «#» — закрашенный.
## Output 

Если рисунок можно представить как два непересекающихся прямоугольника, выведите в первой строке «YES», а в следующих m строках выведите рисунок в том же виде, в каком он задан во входном файле, заменив квадраты, соответствующие первому прямоугольнику на символ «a», а второму — на символ «b». Если решений несколько, выведите любое.

Если же этого сделать нельзя, выведите в выходной файл «NO».


## Example1
**Input:**
```
2 1
#
.
```
**Output:**
```
NO
```

## Example2
**Input:**
```
2 2
..
##
```
**Output:**
```
YES
..
ab
```  

## Example3
**Input:**
```
1 3
###
```
**Output:**
```
YES
..
abb
```  

## Example4
**Input:**
```
1 5
####.
```
**Output:**
```
YES
..
abbb.
```  