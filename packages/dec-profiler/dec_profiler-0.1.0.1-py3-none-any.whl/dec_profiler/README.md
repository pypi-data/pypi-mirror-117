# Что это ?
Проект для профилирования кода


# Описание модулей


## time_dec - Замерить Время

Пример работы
```python
import random
from time_dec import time_s


@time_s(3)
def test():
    a = []
    for i in range(7000):
        a.append(random.randint(0, 9))

n = 100
a = []
test()
```


+ `time_s(count_loop)` = Замерить время выполнения в секундах
    + `count_loop` = Количество повторений функции


+ `time_ns(count_loop)` = Замерить время выполнения в наносекундах
    + `count_loop` = Количество повторений функции