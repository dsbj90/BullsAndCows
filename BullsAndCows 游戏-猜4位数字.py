import random

print ('''Hello！我是猜数字（又称 Bulls and Cows ）小游戏！游戏的开始，我会出一个4位数，这4个数没有重复，在0~9之间，然后就到你的柯南时间啦！你给我4个数后，我会回答你 × A × B，A前面的数字表示位置正确的数的个数，而B前的数字表示数字正确而位置不对的数的个数……
\n有点晕？等等啊，我们举个栗子啊：如果正确答案为 5234，而你猜 5346，则是 1A2B，其中有一个5的位置对了，记为1A，而3和4这两个数字对了，而位置没对，因此记为 2B，合起来就是 1A2B。\n\n\n如果猜不出来，可按“q”键放弃。\n\n据说正常人一般8次左右就能猜中呢……\n\n\n''')

num = random.sample(range(10), 4)    # random已提供从列表中随机抽样（提取不重复的元素）
x = list(str(input("开始猜咯，请告诉我4位不重复的数字: ")))   # 把输入的数变成数组，注意整数int类型不能这么换，会显示“不是可迭代对象”
ci=0     # 猜的次数
wan=0    # 你玩我的次数（输错次数）

while x != ["q"] :    # 一开始这一大块用的用的if，纠结怎么循环来着……
	if len(x) == 4 and str.isdigit(''.join([str(i) for i in x])):    # str.isdigit来检查是否为数字，返回true。join只能join字符串str，后面那坨是个循环，网上找的
		a=0
		b=0
		wan=0
		for i in range(4):
			s=num[i]
			if s == int(x[i]):   # 要把x的元素换回整数，才可与num比较
				a+=1
			else:
				for i in range(4):
					if s == int(x[i]):
						b+=1
		# 判断结果
		ci+=1
		if a != 4 :
			print (ci,"次啦	",a,"A",b,"B")
			x = list(str(input("再猜？：")))
		else: 
			print ("猜对了！么么哒！用了",ci,"次哦")
			break

	# 输错提示
	else:
		wan+=1
		if wan==1:
			x = list(str(input("要输入4位不重复的数字哦！：")))
		elif wan==2:
			x = list(str(input("要输入【4】位不重复的【数字】哦！：")))  # 没有检查重不重复，whatever
		elif wan==3:
			x = list(str(input("哼，你不乖：")))
		elif wan==4:
			x = list(str(input("你玩我啊：")))
		elif wan==5:
			x = list(str(input("别欺负我了！！：")))
		else :
			print ("不跟你玩了！！大坏蛋！！！！")
			break

# 按q放弃
else:
	print ("正确数字为：")
	for i in num:
		print (i,end=' ')   # 不自动换行


input("\nPrease <enter>")   # 执行完后不自动关闭
