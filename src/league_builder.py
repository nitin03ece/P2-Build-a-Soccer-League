import csv


# writeIndividualTextfile function creates, separate 18 text files(named after the player name)
# each file begins with the text "Dear" followed by the guardian(s) name(s). 
# Also include the additional required information: player's name, team name, and date & time of first practice.
def writeIndividualTextfile(Sharks, Dragons, Raptors):
    teams = Sharks + Dragons + Raptors
    for team in teams:
        if teams.index(team) < 6:
            teamName = 'Sharks'
        elif teams.index(team) >= 6 and teams.index(team) < 12:
            teamName = 'Dragons'
        else:
            teamName = 'Raptors'
        name = team[0].split()
        fileName = 'players/' + name[0] + '_' + name[1] + '.txt'
        with open(fileName, 'w') as file:
            letter = """Dear {},\n\nYour ward {} have been selected in {} team. The first practice session is on 1st march at 7 A.M morning. 
Please make sure you dont miss it.\n\nThank You\nSoccer League Selctors""".format(team[2], team[0], teamName)
            file.write(letter)


# writeTextFile function finally creates the "teams.txt file" that includes the name of a team,
# followed by the players on that team. List all three teams and their players.
def writeTextFile(Sharks, Dragons, Raptors):
    with open('teams.txt', 'w') as file:
        file.write("Team Sharks\n")
        file.write("===========\n")
        for row in Sharks:
            file.write(", ".join(row))
            file.write("\n")

        file.write("\nTeam Dragons\n")
        file.write("============\n")
        for row in Dragons:
            file.write(", ".join(row))
            file.write("\n")

        file.write("\nTeam Raptors\n")
        file.write("============\n")
        for row in Raptors:
            file.write(", ".join(row))
            file.write("\n")


# conquer function uses the two variable from divide function
# to equally distribute the players among three teams.
def conquer(Exp_Player, inExp_Player):
    # Assuming that number of Experienced and inexperienced 
    # players are equally divisible between the three team.
    inExpPlayer_perTeam = len(inExp_Player)/3
    ExpPlayer_perTeam = len(Exp_Player)/3

    Sharks = [player for player in inExp_Player if inExp_Player.index(player) % inExpPlayer_perTeam == 0]
    Dragons = [player for player in inExp_Player if inExp_Player.index(player) % inExpPlayer_perTeam == 1]
    Raptors = [player for player in inExp_Player if inExp_Player.index(player) % inExpPlayer_perTeam == 2]    
    
    Sharks.extend([player for player in Exp_Player if Exp_Player.index(player) % ExpPlayer_perTeam == 0])
    Dragons.extend([player for player in Exp_Player if Exp_Player.index(player) % ExpPlayer_perTeam == 1])
    Raptors.extend([player for player in Exp_Player if Exp_Player.index(player) % ExpPlayer_perTeam == 2])  

    writeTextFile(Sharks, Dragons, Raptors)
    writeIndividualTextfile(Sharks, Dragons, Raptors)


# divide function groups the experienced and 
# inexperienced player in two separate variables
def divide(teams):
    Exp_Player = []
    inExp_Player = []
    for team in teams:
        # Updating the info of single team in a variable
        row = []
        row.extend([team['Name'], team['Soccer Experience'], team['Guardian Name(s)']])
        if team['Soccer Experience'] == 'YES':
            Exp_Player.append(row)
        elif team['Soccer Experience'] == 'NO':
            inExp_Player.append(row)
        else:
            pass
    conquer(Exp_Player, inExp_Player)


# Function to read the "soccer_player.csv" file.
def readCSVFile():
    with open('soccer_players.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        # rows variable becomes list of ordereddict variables
        rows = list(reader)
        divide(rows)

def start():
    readCSVFile()

if __name__ == "__main__":
    start()
