import readline
import re
import item
#import delete
COMMANDS=sorted(['add-budget-item', 'del-budget-item', 'version', 'quit'])
def complete(text, state):
     for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1


readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
readline.set_completer_delims(' ')

while True:
    cli = str(input('> '))
    cli = re.sub('  ',' ', cli.rstrip())
#    print(cli)
#    print(cli[0])
    command = cli.split(' ', 1)
#    print(command)
#    print(command[0])
    command[0]
    if cli == 'quit':
        quit()
    if command[0] == 'add-budget-item':
        print('not implemented yet')
    if command[0] == 'del-budget-item':
        print('not implemented yet')
