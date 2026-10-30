import random

print("游戏规则：猜数字，只能猜整数,范围在0~100之中")
a=int(random.randint(0,100))
b=int(input('请输入你要猜的数字；'))
cout=1
while a!=b:
 if a>b:
    print('你猜小了！怎么和猪一样。。')
 elif a<b:
    print('你猜大了，臭傻逼')
 elif a==b:
     break
 b = int(input('请输入你要猜的数字；'))
 cout+=1
 continue
print('猜对了你也是傻逼！你用了%d次'%cout)



