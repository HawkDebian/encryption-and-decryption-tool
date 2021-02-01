import sys

sys.ps1 = '\033[94m'

print(sys.ps1)

print('''
 ████████╗██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚════██╗╚════██╗
   ██║   ██████╔╝ █████╔╝ █████╔╝
   ██║   ██╔══██╗ ╚═══██╗ ╚═══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 


''')

msg = input('Enter the message ya wanna encrypt: ')

algorithm = 'kPYCBmyvdwhPypsrvY72rfI1xlTVXmFVcEiox7A3xlomCw9wLJ5aEkuZU04PHntBEfRi2gb24FAh7iNWU4f2mZ1wrOy4IdcHo1AFUrI6hFP5ZWAkL90pm8ZKai4jjfhFRLO4bV2jJmtgQ15wgvzpBq4InO32zeozjbyDR63Og1hhTQyARVyrAPJKFY5cnNQyNzOxdgMpRzogCPEK2uEMI9U0cuxQPIiSdCAPGlEJwMMM9Yl6VMyG6LCS9OeuhUcBOqwVkvIklnoeCXgTgThwvsHUR2ws05yuIjf00mlZ5BLEkg3XlIn6Ift8Jv9krj3ZlAPNEnbMzcdHNYsjAHCUOj9QtFJXYftzeP7jO41JMNYZB3V1H9dixIQvB6qkXFoYUxpddscrydgGYjYjcQx0c0fPaqowcIRpuFS3mQWyiIan6Gye21yrNi2hUGHdxbow5EJdhrPTIwEUK67fjaeXci1ZCUKcrM8aCWFMvvJAsZ6mROc9lMyb1fiqYGvtSruUWEwagMREy6kskFlAMic22YZgzqOD0lUYvBHfhAJuhQhWVLaeULx53DOHiCIDufNUecftUWaaaCQhE5YBwundsSe6MRqWO8xUL0ennT8jxu1ti2AnyoBWovU47wvFiq29buNNheK001ML4Wa9UzPhAybIukkTnhcFy4N5pdBenA0qqu8SeRoysUofqJmBeg01Py9eMoqkylvQBHxEUcIqzfRfUR4COXw6vDFqfV2Gh3tOJ0nCOdL1u4I'

key = int(input('Enter your key: '))

enc = ''
for i in msg:
    ps = algorithm.find(i)
    newps = (ps + key) % 50
    enc += algorithm[newps]

print(enc)
