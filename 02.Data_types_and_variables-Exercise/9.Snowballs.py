import sys
snowballs = int(input())
max_snowball = -sys.maxsize
max_snow = -sys.maxsize
max_time = -sys.maxsize
max_quality = -sys.maxsize
for snowball in range(snowballs):
    snow = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = int((snow/time) ** quality)
    if snowball_value > max_snowball :
        max_snowball = snowball_value
        max_snow = snow
        max_time = time
        max_quality = quality
print(f'{max_snow} : {max_time} = {max_snowball} ({max_quality})')