#def tail(filename, n=10):
n=10
with open('''C:\\Users\\Sharif\\Desktop\\sharif\\req.txt''',"r") as f:
    lines = f.readlines()
for line in lines.pop(n):
    print(line)
    print(lines)
    print(lines,'by sharif')
    print('xxx')
        
        
#tail(req.txt)