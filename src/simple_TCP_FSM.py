"""https://www.codewars.com/kata/54acc128329e634e9a000362
Automatons, or Finite State Machines (FSM), are extremely useful to programmers when it comes to software design. 
You will be given a simplistic version of an FSM to code for a basic TCP session.

The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.

The input array of events will consist of one or more of the following strings:

APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK
The states are as follows and should be returned in all capital letters as shown:

CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT
The input will be an array of events. The initial state is CLOSED. Your job is to traverse the FSM as determined by the events, 
and return the proper final state as a string, all caps, as shown above.

If an event is not applicable to the current state, your code will return "ERROR".

Action of each event upon each state:
(the format is INITIAL_STATE: EVENT -> NEW_STATE)

CLOSED: APP_PASSIVE_OPEN -> LISTEN
CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
LISTEN: RCV_SYN          -> SYN_RCVD
LISTEN: APP_SEND         -> SYN_SENT
LISTEN: APP_CLOSE        -> CLOSED
SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
SYN_RCVD: RCV_ACK        -> ESTABLISHED
SYN_SENT: RCV_SYN        -> SYN_RCVD
SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
SYN_SENT: APP_CLOSE      -> CLOSED
ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
FIN_WAIT_1: RCV_FIN      -> CLOSING
FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
CLOSING: RCV_ACK         -> TIME_WAIT
FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
TIME_WAIT: APP_TIMEOUT   -> CLOSED
CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
LAST_ACK: RCV_ACK        -> CLOSED

Examples
["APP_PASSIVE_OPEN", "APP_SEND", "RCV_SYN_ACK"] =>  "ESTABLISHED"

["APP_ACTIVE_OPEN"] =>  "SYN_SENT"

["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"] =>  "ERROR"

# Lookup Closed State and map to New State.
# The first value must be Closed State
# Lookup New State and Event and return New State 
"""

from typing import List
from enum import Enum, auto


# Define the State enum
class State(Enum):
    CLOSED = auto()
    LISTEN = auto()
    SYN_RCVD = auto()
    SYN_SENT = auto()
    ESTABLISHED = auto()
    FIN_WAIT_1 = auto()
    CLOSING = auto()
    FIN_WAIT_2 = auto()
    TIME_WAIT = auto()
    CLOSE_WAIT = auto()
    LAST_ACK = auto()
    ERROR = auto()


# Define the Event enum
class Event(Enum):
    APP_PASSIVE_OPEN = "APP_PASSIVE_OPEN"
    APP_ACTIVE_OPEN = "APP_ACTIVE_OPEN"
    RCV_SYN = "RCV_SYN"
    APP_SEND = "APP_SEND"
    APP_CLOSE = "APP_CLOSE"
    RCV_ACK = "RCV_ACK"
    RCV_SYN_ACK = "RCV_SYN_ACK"
    RCV_FIN = "RCV_FIN"
    RCV_FIN_ACK = "RCV_FIN_ACK"
    APP_TIMEOUT = "APP_TIMEOUT"


class FiniteStateMachine:
    def __init__(self):
        self.current_state = State.CLOSED

    def transition_state_map(self, event: Event) -> State:
        transition_map = {
            (State.CLOSED, Event.APP_PASSIVE_OPEN): State.LISTEN,
            (State.CLOSED, Event.APP_ACTIVE_OPEN): State.SYN_SENT,
            (State.LISTEN, Event.RCV_SYN): State.SYN_RCVD,
            (State.LISTEN, Event.APP_SEND): State.SYN_SENT,
            (State.LISTEN, Event.APP_CLOSE): State.CLOSED,
            (State.SYN_RCVD, Event.APP_CLOSE): State.FIN_WAIT_1,
            (State.SYN_RCVD, Event.RCV_ACK): State.ESTABLISHED,
            (State.SYN_SENT, Event.RCV_SYN): State.SYN_RCVD,
            (State.SYN_SENT, Event.RCV_SYN_ACK): State.ESTABLISHED,
            (State.SYN_SENT, Event.APP_CLOSE): State.CLOSED,
            (State.ESTABLISHED, Event.APP_CLOSE): State.FIN_WAIT_1,
            (State.ESTABLISHED, Event.RCV_FIN): State.CLOSE_WAIT,
            (State.FIN_WAIT_1, Event.RCV_FIN): State.CLOSING,
            (State.FIN_WAIT_1, Event.RCV_FIN_ACK): State.TIME_WAIT,
            (State.FIN_WAIT_1, Event.RCV_ACK): State.FIN_WAIT_2,
            (State.CLOSING, Event.RCV_ACK): State.TIME_WAIT,
            (State.FIN_WAIT_2, Event.RCV_FIN): State.TIME_WAIT,
            (State.TIME_WAIT, Event.APP_TIMEOUT): State.CLOSED,
            (State.CLOSE_WAIT, Event.APP_CLOSE): State.LAST_ACK,
            (State.LAST_ACK, Event.RCV_ACK): State.CLOSED,
        }
        return transition_map.get((self.current_state, event), State.ERROR)


def traverse_TCP_states(events: List[str]) -> str:
    s = FiniteStateMachine()
    for event in events:
        event_enum = Event(event)
        s.current_state = s.transition_state_map(event_enum)
        if s.current_state == State.ERROR:
            return State.ERROR.name
    return s.current_state.name


if __name__ == "__main__":
    events = ["APP_ACTIVE_OPEN"]
    result = traverse_TCP_states(events)
    print(result)
