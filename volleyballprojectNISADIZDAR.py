import datetime

class VolleyballPlayer:
    def __init__(self, name, jersey_number):
        self.name = name
        self.jersey_number = jersey_number
        self.attacks = 0
        self.blocks = 0
        self.aces = 0
        self.digs = 0       
        self.assists = 0    
        self.errors = 0

    def get_total_points(self):
        return self.attacks + self.blocks + self.aces

    def get_efficiency(self):
        total_actions = self.get_total_points() + self.digs + self.assists + self.errors
        if total_actions == 0:
            return 0.0
        return (self.get_total_points() + self.digs + self.assists - self.errors) / total_actions
    
def display_menu():
        print("\n" + "="*30)
        print("  VOLLEYBALL STATS TRACKER")
        print("="*30)
        print("1. Add a New Player")
        print("2. Record an Action")
        print("3. Show Team Statistics")
        print("4. Finish Match & Save Report (File I/O)")
        print("5. Exit Program")
        print("="*30)

def find_player(roster, number):
        for player in roster:
            if player.jersey_number == number:
                return player
        return None
    
def save_match_report(roster):
        now = datetime.datetime.now()
        filename = "Match_Report_{}.txt".format(now.strftime("%Y%m%d_%H%M%S"))
        
        with open(filename, "w") as file:
            file.write("--- VOLLEYBALL MATCH REPORT ---\n")
            file.write("Date: {}\n\n".format(now.strftime("%Y-%m-%d %H:%M:%S")))
            
            team_total = 0
            for p in roster:
                file.write("[{}] {}\n".format(p.jersey_number, p.name))
                file.write("  Attacks: {}, Blocks: {}, Aces: {}, Digs: {}, Assists: {}, Errors: {}\n".format(
                    p.attacks, p.blocks, p.aces, p.digs, p.assists, p.errors))
                file.write("  Points Contributed: {}\n".format(p.get_total_points()))
                file.write("  Efficiency: {:.2f}\n\n".format(p.get_efficiency()))

                team_total += p.get_total_points()

            file.write("-" * 30 + "\n")
            file.write("Team Total Points: {}\n".format(team_total))
            file.write(',' * 30 + "\n")

        print('\n[SUCCESS] Match report saved securely as {}'.format(filename))
          

def main():
    team_roster = []

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == "1":
            name = input("Enter player's name: ")

            try:
                jersey = int(input('Enter jersey number'))
            except ValueError:
                print('[ERROR] Invalid input! Jersey number must be a whole number.')
                continue
            

            if find_player(team_roster, jersey) != None:
                print('[ERROR] A player with jersey {} already exists!'.format(jersey))
            else:
                new_player = VolleyballPlayer(name, jersey)
                team_roster.append(new_player)
                print("[SUCCESS] Player {} added to the roster.".format(name))

        elif choice == '2':
            if len(team_roster) == 0:
                print('[ERROR] Roster is empty! Please add players first.')
                continue

            try:
                jersey = int(input('Enter players jersey number: '))
            except ValueError:
                print('[ERROR] Invalid input! Please enter a valid number.')
                continue
                
            player = find_player(team_roster, jersey)

            if player == None:
                print('[ERROR] Player not found!')
            else:
                print("\nAction Types: ")
                print("A - Attack (Kill)")
                print("B - Block")
                print("S - Ace (Serve)")
                print("D - Defense (Dig / Reception)")
                print("P - Perfect Set (Assist)")
                print("E - Error")

                action = input('Select aciton type: ').upper()

                if action == 'A':
                    player.attacks += 1
                    print("Attack recorded for {}!".format(player.name))
                elif action == 'B':
                    player.blocks += 1
                    print("Block recorded for {}!".format(player.name))
                elif action == 'S':
                    player.aces += 1
                    print("Ace recorded for {}!".format(player.name))
                elif action == 'D':
                    player.digs += 1
                    print("Great defense recorded for {}!".format(player.name))
                elif action == 'P':
                    player.assists += 1
                    print("Perfect set (assist) recorded for {}!".format(player.name))
                elif action == 'E':
                    player.errors += 1
                    print("Error recorded for {}!".format(player.name))
                else:
                    print("[ERROR] Invalid action type.")


        elif choice == '3':
            if len(team_roster) == 0:
                print('[INFO] No players to show')
            else: 
                print('\n--- TEAM STATISTICS ---')
                for p in team_roster:
                    print("[{}] {} -> Pts: {} | Digs: {} | Assists: {} | Eff: {:.2f}".format(
                        p.jersey_number, p.name, p.get_total_points(), p.digs, p.assists, p.get_efficiency()))
        
        elif choice == '4':
            if len(team_roster) == 0:
                print("[ERROR] Cannot save an empty report.")
            else: 
                save_match_report(team_roster)

        elif choice == '5':
            print('Existing tracker. Have a good game!')
            break
            
        else:
            print("[ERROR] Invalid choice. Please select from 1 to 5.")

if __name__ == '__main__':
    main()