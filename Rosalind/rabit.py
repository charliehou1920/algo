"""
例子：
1    1
2    1
3    1+3*1
4    4+3*1
5    7+3*4


所以就是： 1 --> 1+0*3 --> 1+1*3 --> 1+1*3 + (1+0*3 )*3
"""

def rabit(n, k):
    if n < 3:
        return 1
    else:
        return rabit(n-1, k) + rabit(n-2, k) * k
    
result = rabit(5, 3)
print(result)