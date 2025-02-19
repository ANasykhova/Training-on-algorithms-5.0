# H. Забег по стадиону

Стадион представляет собой окружность длиной L метров, на которой отмечена точка старта. По стадиону бегают Кирилл и Антон. У каждого мальчика есть своя точка старта (она представляет собой расстояние в метрах от старта, отсчитанное по часовой стрелке) и своя скорость в метрах в секунду (положительная скорость означает, что мальчик бежит по часовой стрелке, отрицательная — что бежит против часовой, а нулевая — что он стоит на месте).
Вам нужно сказать, через какое минимальное время мальчики окажутся на одинаковом расстоянии от точки старта. Обратите внимание, что в этот момент они могли находиться в разных точках. Расстоянием от точки
A до точки B называется минимальное из расстояний, которое нужно пробежать из точки A по или против часовой стрелки, чтобы оказаться в B.  


## Input  
В единственной строке вводится 5 целых чисел L, x1, x2, v1, v2 (1 &le; L &le; 10<sup>9</sup>, 1 &le; x1, x2 &le; L, |v1|, |v2| &le; 10<sup>9</sup>) — длины стадиона в метрах, начальная точка Кирилла, скорость Кирилла, начальная точка Антона, скорость Антона.

## Output
В первой строке выведите слово «YES», если случится момент, когда мальчики будут на одинаковом расстоянии от старта, или «NO», если такого момента не произойдёт.
Если ответ «YES», то во второй строке выведите одно вещественное число — через какое минимальное количество времени мальчики окажутся на одинаковом расстоянии от старта.
Вы можете выводить каждую букву в любом регистре (строчную или заглавную). Например, строки «yEs», «yes», «Yes» и «YES» будут приняты как положительный ответ.
Ваш ответ будет считаться правильным, если его абсолютная или относительная ошибка не превосходит 10<sup>-9</sup>.  
Формально, пусть ваш ответ равен a, а ответ жюри равен b. Ваш ответ будет зачтен, если и только если
|a - b| / max(1, |b|) &le; 10<sup>-9</sup>.

## Example1
**Input:**
```
6 3 1 1 1
```
**Output:**
```
YES
1.0000000000
``` 

## Example2
**Input:**
```
12 8 10 5 20
```
**Output:**
```
YES
0.3000000000
``` 

## Example3
**Input:**
```
5 0 0 1 2
```
**Output:**
```
YES
2.0000000000
``` 

## Example4
**Input:**
```
10 7 -3 1 4
```
**Output:**
```
YES
0.8571428571
``` 

**Примечания**

В первом тесте Кирилл изначально находится в точке 3 и бежит по часовой стрелке со скоростью 1. Антон находится в точке 1 и также бежит по часовой стрелке со скоростью 1.  
Через 1 секунду мальчики окажутся в точках 4 и 2 соответственно. Обе эти точки расположены на расстоянии 2 метра от старта (точки 0, совпадающей с точкой 6).  
Можно показать, что до этого они всегда находились на разном расстоянии от старта. Значит, ответ — 1.
Во втором тесте оба мальчика окажутся в точке 11 через 0.3секунды.
В третьем Антон прибежит к Кириллу в точку 0 за 2 секунды.