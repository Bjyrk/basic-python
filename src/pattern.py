
# Print the pattern

start ='*'

for i in range(9):
    if i == 0:
            print(start)
    elif i <= 4:
        ny = ' *'
        mønster = start+ny
        start = mønster
        print(mønster)
    elif i > 4:
        mindre = 9-(i*2)
        mindre_mønster = mønster[0:mindre]
        print(mindre_mønster)
