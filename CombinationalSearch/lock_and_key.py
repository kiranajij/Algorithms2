"""
Given the classic problem of lock and key, this program tries to solve
the problem.
Input format
N           # Number of inputs
abc c p     # test case, number of correct digits, write places
.
.
. (N lines)
"""
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)


def to_digits(num):
    """
    returns an integer array of the digits of a given string corresponding
    to a number
    """
    return list(map(int, num))


class State:
    """
    This is the class to represent a state in statevector.
    We needed a different class for this because we need to keep track of
    the digit is correct or not and if well placed.
    """
    def __init__(self, digit: int, corr: bool, place: bool):
        self.digit = digit          # the current digit
        self.is_correct = corr      # if the digit is correct
        self.is_placed = place      # if the position is correct

    def __repr__(self):
        c = 'T' if self.is_correct else 'F'
        w = 'T' if self.is_placed else 'F'
        return f"{self.digit}({c}{w})"


class LockAndKey:
    def __init__(self, ndigs, n, cases, correct_digs, correct_places):
        self.n              = n                     # number of cases
        self.ndigs          = ndigs
        self.cases          = cases                 # the cases
        self.correct_digs   = correct_digs          # number of correct digits
        self.correct_places = correct_places        # number of well_placed digits

        self.sv             = [None for i in range(ndigs)]    # state vector

        logging.debug(f"{cases}\n{correct_digs}\n{correct_places}")

    def generate_candidate(self, k):
        global State

        current_state       = self.sv[:k]   # currect state vecotor
        cands               = []            # to store possible candidates

        # number of correct digit left for each case
        corr_digits_left    = self.correct_digs[:]

        # number of well placed digits left for each case
        well_digits_left    = self.correct_places[:]

        # update the correct digit and well placed digit count for each case
        for si, state in enumerate(current_state):
            digit = state.digit
            # for each case, check if the digit is in the case
            for i, case in enumerate(self.cases):
                if digit in to_digits(case):
                    corr_digits_left[i] -= 1
                    # update the well_placed digit count
                    if state.is_placed and state.digit == to_digits(case)[si]:
                        well_digits_left[i] -= 1

        logging.debug(f"{current_state}, {corr_digits_left}, {well_digits_left}")
        # now calculate the possible candidate for i'th place
        # given a digit, if the i'th place is the same with a case,
        # and correct_ditis left for that case is > 0 then add it for 
        # a possible candidate.

        all_digits = list(range(10))
        for i, case in enumerate(self.cases):
            # If no correct digit left, then all the digits from k'th pos
            # are false digits
            if corr_digits_left[i] == 0:
                # Don't add anyting to the cands
                for d in to_digits(case)[k:]:
                    # remove d from possible digits
                    try:
                        all_digits.remove(d)
                    except:
                        pass

        for d in all_digits:
            nstate1 = State(d, True, True)      # considering it's well placed
            nstate2 = State(d, True, False)     # not well placed

            for case, c, w in zip(self.cases, corr_digits_left, well_digits_left):
                case_digits = to_digits(case)

                # Covers if the cnads_left is 0 for any case, then it cannot possibly
                # be a correct digit.
                if c == 0 and d in case_digits:
                    nstate1.is_correct = False
                    nstate2.is_correct = False

                    logging.debug(f"case {case} gives 0, removing {d}")

                # If c > 0 then there are more than one correct digit, now if the k'th
                # digit of a case equals d, and w=0 then it cannot be correctly placed,so
                # d cannot be the k'th digit.
                elif d == case_digits[k] and w == 0:
                    nstate1.is_correct = False
                elif d == case_digits[k] and w > 0:
                    nstate2.is_correct = False


            if nstate1.is_correct:
                cands.append(nstate1)
            if nstate2.is_correct:
                cands.append(nstate2)
        logging.debug(f"New Candidate for pos {k} {cands}")

        return cands


    def is_solution(self, k):
        if k == self.ndigs: return True
        return False

    def search(self, k):
        if self.is_solution(k):
            self.process_solution(k)
        else:
            cands = self.generate_candidate(k)
            for c in cands:
                self.sv[k] = c
                self.search(k+1)

    def process_solution(self, k):

        current_state       = self.sv[:k]   # currect state vecotor

        # number of correct digit left for each case
        corr_digits_left    = self.correct_digs[:]

        # number of well placed digits left for each case
        well_digits_left    = self.correct_places[:]

        # update the correct digit and well placed digit count for each case
        for si, state in enumerate(current_state):
            digit = state.digit
            # for each case, check if the digit is in the case
            for i, case in enumerate(self.cases):
                if digit in to_digits(case):
                    corr_digits_left[i] -= 1
                    # update the well_placed digit count
                    if state.is_placed and state.digit == to_digits(case)[si]:
                          well_digits_left[i] -= 1

        all_zero = True
        all_placed = True
        for c, w in zip(corr_digits_left, well_digits_left):
            if c != 0 or w != 0:
                all_zero = False

        for state in current_state:
            if not state.is_placed:
                all_placed = False
        if all_zero and all_placed:
            # This is the solution
            sol = "".join(list(\
                map(lambda x: str(x.digit), current_state)))
            print(f"Solution: {sol}")


def another_method(cases, corrects, well_placed):
    #! Doesnot work
    probablities = defaultdict(int)
    for d in range(10):
        for i, (case, c, w) in enumerate(zip(cases, corrects, well_placed)):
            if d in digits(case):
                if c == 0:
                    probablities[d] = -10
                elif c == 3:
                    probablities[d] = 10
                else:
                    probablities[d] += c/3
            else:
                probablities[d] += (3-c)/7

    return probablities

if __name__ == '__main__':
    ndigs, n = list(map(int, input().split()))
    cases = []
    corrs = []
    wells = []
    for i in range(n):
        case, c, w = input().split()
        c = int(c)
        w = int(w)
        cases.append(case)
        corrs.append(c)
        wells.append(w)

    klp = LockAndKey(ndigs, n, cases, corrs,wells)
    klp.search(0)
