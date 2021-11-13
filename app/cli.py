import readline

COMMANDS=sorted(['add-budget-item'])

PROMPT ='> '

def complete(text, state):
     for cmd in COMMANDS:
        if cmd.starswith(text):
            if not state:
                return cmd
            else:
                state -= 1
def cli():
    while True:
        valid = 0
        if 'libedit' in readline.__doc__:
                readline.parse_and_bind("bind ^I rl_complete")
        else:
                readline.parse_and_bind("tab: complete")

        readline.set_completer(complete)
        readline.set_completer_delims(' ')
       
        cli = str(input(PROMPT))
        cli = re.sub('  ',' ', cli.rstrip())
