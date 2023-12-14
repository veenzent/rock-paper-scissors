import random
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class Interface(BoxLayout):
    choices = ['rock', 'paper', 'scissors']
    user_choice = StringProperty(" ")
    user_score = StringProperty("0")
    u_score = 0
    computer_choice = StringProperty(" ")
    computer_score = StringProperty("0")
    com_score = 0
    weapon_choice = StringProperty("SELECT WEAPON")
    result = StringProperty("")
    play_button_disabled = BooleanProperty(True)

    def on_toggle_rock(self, rock):
        if rock.state == "down":
            self.ids.outcome.text = ""
            self.weapon_choice = "ROCK SELECTED"
            self.user_choice = "rock"
            self.computer_choice = random.choice(self.choices)
            self.play_button_disabled = False
            print("User choice: rock")
            print("Computer choice: " + self.computer_choice)
        else:
            self.weapon_choice = "SELECT WEAPON"
            self.play_button_disabled = True

    def on_toggle_paper(self, paper):
        if paper.state == "down":
            self.ids.outcome.text = ""
            self.weapon_choice = "PAPER SELECTED"
            self.user_choice = "paper"
            self.computer_choice = random.choice(self.choices)
            self.play_button_disabled = False
            print("User choice: paper")
            print("Computer choice: " + self.computer_choice)
        else:
            self.weapon_choice = "SELECT WEAPON"
            self.play_button_disabled = True

    def on_toggle_scissors(self, scissors):
        if scissors.state == "down":
            self.ids.outcome.text = ""
            self.weapon_choice = "SCISSORS SELECTED"
            self.user_choice = "scissors"
            self.computer_choice = random.choice(self.choices)
            self.play_button_disabled = False
            print("User choice: scissors")
            print("Computer choice: " + self.computer_choice)
        else:
            self.weapon_choice = "SELECT WEAPON"
            self.play_button_disabled = True

    # play_outcome returns Win or Lose
    def play_outcome(self):
        if self.user_choice == self.computer_choice:
            self.result = 'You both made same choice: That\'s a tie'
# ROCK
        elif self.user_choice == 'rock' and self.computer_choice == 'paper':
            self.result = 'Rock is covered by paper: You Lose'
        elif self.user_choice == 'rock' and self.computer_choice == 'scissors':
            self.result = 'Rock smashes scissors: You Win'
# PAPER
        elif self.user_choice == 'paper' and self.computer_choice == 'scissors':
            self.result = 'Paper is cut by scissors: You Lose'
        elif self.user_choice == 'paper' and self.computer_choice == 'rock':
            self.result = 'Paper covers rock: You Win'
# SCISSORS
        elif self.user_choice == 'scissors' and self.computer_choice == 'rock':
            self.result = 'Scissors is smashed by rock: You Lose'
        elif self.user_choice == 'scissors' and self.computer_choice == 'paper':
            self.result = 'Scissors cuts paper: You Win'
        return self.result

    # Play button
    def on_play_button(self):
        self.ids.rock.state = "normal"
        self.ids.paper.state = "normal"
        self.ids.scissors.state = "normal"
        if self.play_outcome().endswith("Win"):
            self.u_score += 2
            self.user_score = str(self.u_score)
            self.ids.outcome.text = self.play_outcome()
        elif self.play_outcome().endswith("Lose"):
            self.com_score += 2
            self.computer_score = str(self.com_score)
            self.ids.outcome.text = self.play_outcome()
        elif self.user_choice == self.computer_choice:
            self.ids.outcome.text = self.play_outcome()


class rpsApp(App):
    pass


rpsApp().run()