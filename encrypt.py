import sys


sys.ps1 = '\033[94m'

print(sys.ps1)

print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')


msg = input('Enter the message ya wanna encrypt: ')

algorithm = 'elfghijkzmadnopcqrbstuvwxy'

key = int(input('Enter your key: '))


enc = ''
for i in msg:
    ps = algorithm.find(i)
    newps = (ps+key)%26
    enc +=algorithm[newps]
    
print(enc)
