# Ultimate Trap Brute Force Solver

## Run
```bash
pip install -r requirements.txt
python solve.py
```

## Answer
> python solve.py
--  ---  ---  ---  ---  ---  ---  ---  ---  ---  -  --  --  ---  ---  ---  ---  ---  ---  ---  ---  ---
*     0    1    2    3    4    5    6    7    8  9  10  11   12   13   14   15   16   17   18   19   20
0   nan  nan  nan  nan  nan  nan  nan  nan  nan  4   7   7  nan  nan  nan  nan  nan  nan  nan  nan  nan
1   nan  nan  nan  nan  nan  nan    5    4    4  8   3   3    4    6    3  nan  nan  nan  nan  nan  nan
2   nan  nan  nan  nan    1    4    5    1    1  1   4   5    1    7    1    3    5  nan  nan  nan  nan
3   nan  nan  nan    4    9    4    9    6    7  5   5   5    8    7    6    6    8    5  nan  nan  nan
4   nan  nan    3    7    2    9    8    3    5  6   7   3    9    1    8    7    5    8    5  nan  nan
5   nan  nan    1    4    7    8    4    2    9  2   7   1    1    8    2    2    7    6    3  nan  nan
6   nan    7    2    1    8    5    5    3    1  1   3   1    3    3    4    2    8    6    7    3  nan
7   nan    4    2    6    7    2    5    2    4  2   2   5    4    3    2    8    1    7    7    3  nan
8   nan    4    1    6    5    1    1    1    9  1   4   3    4    4    3    1    9    8    2    7  nan
9     4    3    5    2    3    2    2    3    2  4   2   5    3    5    1    1    3    5    5    3    7
10    2    7    1    5    1    1    3    1    5  3   3   2    4    2    3    7    7    5    4    2    7
11    2    5    2    2    6    1    2    4    4  6   3   4    1    2    1    2    6    5    1    8    8
12  nan    4    3    7    5    1    9    3    4  4   5   2    9    4    1    9    5    7    4    8  nan
13  nan    4    1    6    7    8    3    4    3  4   1   3    1    2    3    2    3    6    2    4  nan
14  nan    7    3    2    6    1    5    3    9  2   3   2    1    5    7    5    8    9    5    4  nan
15  nan  nan    1    6    7    3    4    8    1  2   1   2    1    2    2    8    9    4    1  nan  nan
16  nan  nan    2    5    4    7    8    7    5  6   1   3    5    7    8    7    2    9    3  nan  nan
17  nan  nan  nan    6    5    6    4    6    7  2   5   2    2    6    3    4    7    4  nan  nan  nan
18  nan  nan  nan  nan    2    3    1    2    3  3   3   2    1    3    2    1    1  nan  nan  nan  nan
19  nan  nan  nan  nan  nan  nan    7    4    4  5   7   3    4    4    7  nan  nan  nan  nan  nan  nan
20  nan  nan  nan  nan  nan  nan  nan  nan  nan  3   3   4  nan  nan  nan  nan  nan  nan  nan  nan  nan
--  ---  ---  ---  ---  ---  ---  ---  ---  ---  -  --  --  ---  ---  ---  ---  ---  ---  ---  ---  ---
15
[('3', 10, 10, 'START'),
 ('2', 13, 10, 'E'),
 ('7', 15, 10, 'E'),
 ('5', 8, 10, 'W'),
 ('5', 3, 10, 'W'),
 ('6', 3, 15, 'S'),
 ('2', 9, 15, 'E'),
 ('4', 7, 13, 'NW'),
 ('6', 3, 17, 'SW'),
 ('6', 9, 11, 'NE'),
 ('2', 15, 5, 'NE'),
 ('5', 17, 3, 'NE'),
 ('4', 12, 8, 'SW'),
 ('4', 8, 12, 'SW'),
 ('4', 4, 16, 'SW')]
('EXIT', 8, 20)
----------------

15
[('3', 10, 10, 'START'),
 ('2', 13, 10, 'E'),
 ('7', 15, 10, 'E'),
 ('5', 8, 10, 'W'),
 ('5', 3, 10, 'W'),
 ('6', 3, 15, 'S'),
 ('2', 9, 15, 'E'),
 ('4', 7, 13, 'NW'),
 ('6', 3, 17, 'SW'),
 ('6', 9, 11, 'NE'),
 ('2', 15, 5, 'NE'),
 ('5', 17, 3, 'NE'),
 ('4', 12, 8, 'SW'),
 ('4', 8, 12, 'SW'),
 ('4', 4, 16, 'SW')]
('EXIT', 0, 12)
----------------

