string = input().split("\\")
tot_file = string[-1].split('.')
file = tot_file[0]
ext = tot_file[1]
print(f'File name: {file}')
print(f'File extension: {ext}')
