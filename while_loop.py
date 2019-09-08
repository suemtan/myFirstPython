#user input and while loop
banned_users = ['eve', 'Fred','Gary', 'Helen', 'Fab']

prompt = "Add a player to your team."
prompt += "\n Enter 'quit' when you are done."

players =[]

while True:
    player = raw_input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print player, "is banned!"
    else:
        players.append(player)

print "\nYour team : "

for player in players:
    print(player)