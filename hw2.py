password = 'a123456'
i = 3
while i > 0:
	user_password = input('請輸入密碼：')
	if user_password == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print('密碼錯誤 還有', i,'次機會')
