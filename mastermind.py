import random

class MastermindGame:
    def __init__(self, colors, positions):
        self.colors = colors
        self.positions = positions
        self.solution = self.generate_solution()
        self.rounds = 0

    def generate_solution(self):
        return [random.choice(self.colors) for _ in range(self.positions)]

    def provide_feedback(self, guess):
        feedback = ''
        for i in range(self.positions):
            if guess[i] == self.solution[i]:
                feedback += '*'
            elif guess[i] in self.solution:
                feedback += 'o'
            else:
                feedback += ' '
        return feedback

    def play(self):
        print(f"Playing Mastermind with {len(self.colors)} colors and {self.positions} positions")
        while True:
            user_guess = input("What is your guess?: ")
            self.rounds += 1
            # print(self.solution) solution answer if you want to see solution command out

            feedback = self.provide_feedback(user_guess)

            print(f"Your guess is: {user_guess}")
            print(feedback)

            if '*' * self.positions == feedback:
                print(f"\nYou solved it after {self.rounds} rounds!")
                break

colors = ['1', '2', '3', '4', '5', '6']
positions = 4

mastermind_game = MastermindGame(colors, positions)
mastermind_game.play()
