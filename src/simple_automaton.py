"""https://www.codewars.com/kata/5268acac0d3f019add000203/train/python

Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:

q1 is our start state, we begin reading commands from here
q2 is our accept state, we return true if this is our last state
And the transitions:

q1 moves to q2 when given a 1, and stays at q1 when given a 0
q2 moves to q3 when given a 0, and stays at q2 when given a 1
q3 moves to q2 when given a 0 or 1
The automaton should return whether we end in our accepted state (q2), or not (true/false).

Your task
You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2, and q3 for the myAutomaton instance. The test fixtures will be calling against myAutomaton.

As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'

Here are some resources on DFAs (the automaton this Kata asks you to create):

http://en.wikipedia.org/wiki/Deterministic_finite_automaton
http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html
http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf
Example
a = Automaton()
a.read_commands(["1", "0", "0", "1", "0"])  ==> False
We make these transitions:

input: ["1", "0", "0", "1", "0"]

1: q1 -> q2
0: q2 -> q3
0: q3 -> q2
1: q2 -> q2
0: q2 -> q3
We end in q3 which is not our accept state, so we return false
"""

from typing import List
from enum import Enum, auto


class State(Enum):
    Q1 = auto()
    Q2 = auto()
    Q3 = auto()


class BinarySymbol(Enum):
    Zero = "0"
    One = "1"


class Automaton:
    def __init__(self):
        self.state = State.Q1

    def transition(self, input_symbol: BinarySymbol):
        if self.state == State.Q1:
            if input_symbol == BinarySymbol.One:
                self.state = State.Q2
        elif self.state == State.Q2:
            if input_symbol == BinarySymbol.Zero:
                self.state = State.Q3
            elif input_symbol == BinarySymbol.One:
                self.state = State.Q2  # Explicitly showing staying in Q2 for clarity
        elif self.state == State.Q3:
            self.state = State.Q2  # Q3 transitions to Q2 on any input

    def read_commands(self, commands: List[str]):
        for command in commands:
            input_symbol = BinarySymbol(command)
            self.transition(input_symbol)
        return self.state == State.Q2


# Example usage
if __name__ == "__main__":
    automaton = Automaton()
    commands = [
        BinarySymbol.One,
        BinarySymbol.Zero,
        BinarySymbol.Zero,
        BinarySymbol.One,
        BinarySymbol.Zero,
    ]
    result = automaton.read_commands(commands)
    print("Automaton result:", result)  # Expected: False
