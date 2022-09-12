from re import search as sr


text = input("введи юникод: ")


def decoding(code: str) -> str:
	# -----Данные-----
	data = []
	code = code.split("\\")
	for i in code:
		# -----Данные после unicode-----
		end_symbols = ''
		if len(i) >= 6:
			end_symbols = i[5:]
		# -----Unicode-----
		i = i[0:5]
		# -----Decode-----
		if 'u0430' == i:  #--- a ---
			data.append('a')
		elif 'u0431' == i:  #--- б ---
			data.append('б')
		elif 'u0432' == i:  #--- в ---
			data.append('в')
		elif 'u0433' == i:  #--- г ---
			data.append('г')
		elif 'u0434' == i:  #--- д ---
			data.append('д')
		elif 'u0435' == i:  #--- е ---
			data.append('е')
		elif 'u0451' == i:  #--- ё ---
			data.append('ё')
		elif 'u0436' == i:  #--- ж ---
			data.append('ж')
		elif 'u0437' == i:  #--- з ---
			data.append('з')
		elif 'u0438' == i:  #--- и ---
			data.append('и')
		elif 'u0439' == i:  #--- й ---
			data.append('й')
		elif 'u043a' == i:  #--- к ---
			data.append('к')
		elif 'u043b' == i:  #--- л ---
			data.append('л')
		elif 'u043c' == i:  #--- м ---
			data.append('м')
		elif 'u043d' == i:  #--- н ---
			data.append('н')
		elif 'u043e' == i:  #--- о ---
			data.append('о')
		elif 'u043f' == i:  #--- п ---
			data.append('п')
		elif 'u0440' == i:  #--- р ---
			data.append('р')
		elif 'u0441' == i:  #--- с ---
			data.append('с')
		elif 'u0442' == i:  #--- т ---
			data.append('т')
		elif 'u0443' == i:  #--- у ---
			data.append('у')
		elif 'u0444' == i:  #--- ф ---
			data.append('ф')
		elif 'u0445' == i:  #--- х ---
			data.append('х')
		elif 'u0446' == i:  #--- ц ---
			data.append('ц')
		elif 'u0447' == i:  #--- ч ---
			data.append('ч')
		elif 'u0448' == i:  #--- ш ---
			data.append('ш')
		elif 'u0449' == i:  #--- щ ---
			data.append('щ')
		elif 'u044a' == i:  #--- ъ ---
			data.append('ъ')
		elif 'u044b' == i:  #--- ы ---
			data.append('ы')
		elif 'u044c' == i:  #--- ь ---
			data.append('ь')
		elif 'u044d' == i:  #--- э ---
			data.append('э')
		elif 'u044e' == i:  #--- ю ---
			data.append('ю')
		elif 'u044f' == i:  #--- я ---
			data.append('я')
		elif 'u0410' == i:  #--- a ---
			data.append('А')
		elif 'u0411' == i:  #--- б ---
			data.append('Б')
		elif 'u0412' == i:  #--- в ---
			data.append('В')
		elif 'u0413' == i:  #--- г ---
			data.append('Г')
		elif 'u0414' == i:  #--- д ---
			data.append('Д')
		elif 'u0415' == i:  #--- е ---
			data.append('Е')
		elif 'u0401' == i:  #--- ё ---
			data.append('Ё')
		elif 'u0416' == i:  #--- ж ---
			data.append('Ж')
		elif 'u0417' == i:  #--- з ---
			data.append('З')
		elif 'u0418' == i:  #--- и ---
			data.append('И')
		elif 'u0419' == i:  #--- й ---
			data.append('Й')
		elif 'u041a' == i:  #--- к ---
			data.append('К')
		elif 'u041b' == i:  #--- л ---
			data.append('Л')
		elif 'u041c' == i:  #--- м ---
			data.append('М')
		elif 'u041d' == i:  #--- н ---
			data.append('Н')
		elif 'u041e' == i:  #--- о ---
			data.append('О')
		elif 'u041f' == i:  #--- п ---
			data.append('П')
		elif 'u0420' == i:  #--- р ---
			data.append('Р')
		elif 'u0421' == i:  #--- с ---
			data.append('С')
		elif 'u0422' == i:  #--- т ---
			data.append('Т')
		elif 'u0423' == i:  #--- у ---
			data.append('У')
		elif 'u0424' == i:  #--- ф ---
			data.append('Ф')
		elif 'u0425' == i:  #--- х ---
			data.append('Х')
		elif 'u0426' == i:  #--- ц ---
			data.append('Ц')
		elif 'u0427' == i:  #--- ч ---
			data.append('Ч')
		elif 'u0428' == i:  #--- ш ---
			data.append('Ш')
		elif 'u0429' == i:  #--- щ ---
			data.append('Щ')
		elif 'u042d' == i:  #--- э ---
			data.append('Э')
		elif 'u042e' == i:  #--- ю ---
			data.append('Ю')
		elif 'u042f' == i:  #--- я ---
			data.append('Я')
		elif ' ' == i:
			data.append(' ')
		else:
			data.append(i)
		# -----Данные после unicode-----
		data.append(end_symbols)
	# -----Итоговый текст-----
	words = ''
	for i in data:
		words = words + i
	
	return words

print(decoding(text))	
