N = int(input())
m = N//60
N = N % 60
h = m // 60
m = m - h*60
print('{}:{}:{}'.format(h,m,N))