import readline
import add
import delete
COMMANDS=sorted(['add-budget-item', 'del-budget-items', 'version', 'quit'])
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
