# combinatorial_algorithms
Some scripts written for my university course.

## Задача 1. Двудольный граф.
Определить, является ли данный связный неориентированный граф двудольным.

**Метод решения**: Поиск в ширину.

**Файл исходных данных**:
Граф, заданный матрицей смежности.
N - количество вершин в графе.
Далее построчно расположена матрица смежности размерности N x N.

**Файл результатов**:
Если граф не двудольный, то в файл результатов необходимо записать
"N", иначе "Y" и далее вершины входящие в доли графа. Вершины в долях
должны быть упорядочены по возрастанию номеров. Первой печатается доля в
состав которой входит вершина с минимальным номером. Доли разделяются нулем
и печатаются каждая с новой строки

## Задача 2. Конь.
На шахматной доске стоят белый конь и черная пешка. Напечатать маршрут коня, позволяющий уничтожить пешку.

**Примечание**: пешка - неподвижная, конь не должен попадать под удар пешки.

**Метод решения**: Поиск в глубину.

**Файл исходных данных**: Координаты коня и пешки.

Сначала располагаются координаты коня затем пешки. Координаты даются в шахматной нотации, т.е. в виде AB, где A может принимать значения от a до h, B от 1 до 8.

**Формат файла результатов**: Маршрут в шахматной нотации. Маршрут должен начинаться координатами коня и заканчиваться координатами пешки. Каждый ход записывается с новой строки.

## Задача 3. Путь.
Найти кратчайший v-w путь в бесконтурной сети.

**Метод решения**: алгоритм построения пути в бесконтурной сети.
 
**Файл исходных данных**: Сеть, заданная матрицей весов.
N - количество вершин.
Далее построчно  расположена  матрица весов размерности NxN.  В конце
файла записаны источник и цель.  Число 32767 означает, что данная дуга от-
сутствует.
 
**Файл результатов**:
 В случае  отсутствия пути в файл результатов необходимо записать "N",
при наличии пути - "Y" и далее с новой строки весь путь.  Путь начинается
источником и заканчивается целью. Узлы отделяются друг от друга пробелами,
вес пути вычисляется как сумма весов всех дуг, входящих в него и записыва-
ется в третьей строке.
