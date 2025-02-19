# F. Замена слов

С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте. Для этого был составлен словарь слов, до которых можно сокращать более длинные слова. Слово из текста можно сократить, если в словаре найдется слово, являющееся началом слова из текста. Например, если в списке есть слово "лом", то слова из текста "ломбард", "ломоносов" и другие слова, начинающиеся на "лом", можно сократить до "лом".

Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого короткого слова.

## Input

В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв. Гарантируется, что словарь не пуст и количество слов в словаре не превышет 1000, а длина слов — 100 символов.

Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв). Количество слов в тексте не превосходит 10<sup>5</sup>, а суммарное количество букв в них — 10<sup>6</sup>.

## Output

Выведите текст, в котором осуществлены замены.  

## Example1
**Input:**
```
a b
abdafb basrt casds dsasa a
```
**Output:**
```
a b casds dsasa a
``` 

## Example2
**Input:**
```
aa bc aaa
a aa aaa bcd abcd
```
**Output:**
```
a aa aa bc abcd
``` 