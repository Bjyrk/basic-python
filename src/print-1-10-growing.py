
# Print the numbers described in the exercise

tal=''

for i in range(10):
    ny = str(i+1)
    if i == 0:
        svar = tal+ny
        tal = svar
    else:
        svar = tal+' '+ny
        tal = svar
    print(svar)