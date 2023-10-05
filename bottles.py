def bottle_song(num):
	beer = num
	while beer > -1:
		if beer > 1:
			print(f"{beer} bottles of beer on the wall, {beer} bottles of beer! Take one down, pass it around: {beer - 1} bottles of beer on the wall!")
			beer = beer - 1
		elif beer == 1:
			print(f"1 bottle of beer on the wall, 1 bottle of beer! Take one down, pass it around. No more bottles of beer on the wall.")
			beer = beer - 1
		else: 
			print(f"No more bottles of beer on the wall, no more bottles of beer! Go to the store and buy some more, {num} bottles of beer on the wall.")
			beer = beer - 1
	pass

bottle_song(9)
