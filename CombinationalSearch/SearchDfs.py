"""
Backtracking is a technique where you create a partial solution and then
advance one step at a time and keep doing it until desired result is acquired.
=============================================================================
    An recursive implementation of this algorithm is given is pseudo code bellow.

    BacktrackDFS(A, k)
        if A = (a1, a2, a3, ..., an) is a solution, report it
        else
            k = k+1
            compute candidate array (S_k), i.e. possible successors
            for each candidate in S_k
                set A[k] = candidate
                BacktrackDFS(A, k)

"""
import sys
from abc import abstractmethod, ABCMeta


class AbstractBacktrackDFS(metaclass=ABCMeta):

    def __init__(self):
        self.finished = False
        self.state_vector = None

    @abstractmethod
    def is_solution(self, k, *args, **kwargs):
        pass

    @abstractmethod
    def process_solution(self, k, *args, **kwargs):
        pass

    @abstractmethod
    def generate_candidates(self, k, candidates, *args, **kwargs):
        pass

    @abstractmethod
    def make_move(self, k, *args, **kwargs):
        pass

    @abstractmethod
    def unmake_move(self, k, *args, **kwargs):
        pass

    def _run(self, k, *args, **kwargs):
        candidates = []
        n_candidates = 0

        if self.is_solution(k, *args, **kwargs):
            self.process_solution(k, *args, **kwargs)

        else:
            k += 1
            n_candidates = self.generate_candidates(k, candidates, *args, **kwargs)
            for cand in candidates:
                self.state_vector[k] = cand
                self.make_move(k, *args, **kwargs)
                self._run(k, *args, **kwargs)
                self.unmake_move(k, *args, **kwargs)
                if self.finished:
                    return

    def run(self):
        self._run(0)


class Subsets(AbstractBacktrackDFS):

    def __init__(self, n, elements: list = None):
        super().__init__()
        self.n = n
        self.state_vector = [False] * (n + 1)
        self.finished = False
        if elements is None:
            self.elements = [i for i in range(1, n + 1)]
        else:
            self.elements = elements

    def is_solution(self, k, *args, **kwargs):
        return k == self.n

    def process_solution(self, k, *args, **kwargs):
        elems = [self.elements[i] for i in range(self.n) if self.state_vector[i + 1]]
        # print(elems)
        if sum(elems) == 5:
            print(elems)
        # print(self.state_vector)

    def generate_candidates(self, k, candidates, *args, **kwargs):
        candidates.append(True)
        candidates.append(False)

    def make_move(self, k, *args, **kwargs):
        pass

    def unmake_move(self, k, *args, **kwargs):
        pass


class Permutations(AbstractBacktrackDFS):
    def __init__(self, n_elements, elements: list = None):
        super().__init__()
        self.n_elements = n_elements
        if elements is None:
            self.elements = [i + 1 for i in range(n_elements)]
        else:
            self.n_elements = elements
        self.state_vector = [None for i in range(n_elements + 1)]

    def is_solution(self, k, *args, **kwargs):
        return k == self.n_elements

    def process_solution(self, k, *args, **kwargs):
        print(self.state_vector[1::])

    def generate_candidates(self, k, candidates, *args, **kwargs):
        current_sv = self.state_vector[1:k]
        for elem in self.elements:
            if elem not in current_sv:
                candidates.append(elem)
        # print(candidates)
        # print(self.state_vector)
        return candidates

    def make_move(self, k, *args, **kwargs):
        pass

    def unmake_move(self, k, *args, **kwargs):
        pass


class AssignmentProblem(AbstractBacktrackDFS):
    def is_solution(self, k, *args, **kwargs):
        return k == self.n

    def process_solution(self, k, *args, **kwargs):
        cost = 0

        for i in range(n):
            cost += self.costMatrix[self.state_vector[i+1]][i]
        # print(self.state_vector[1:], cost)
        if cost < self.min_cost:
            self.min_cost = cost
            self.min_sv = self.state_vector.copy()

    def generate_candidates(self, k, candidates, *args, **kwargs):
        # candidate = []
        current_cv = self.state_vector[1:k]
        for i in range(n):
            if i not in current_cv:
                candidates.append(i)
        return candidates

    def make_move(self, k, *args, **kwargs):
        pass

    def unmake_move(self, k, *args, **kwargs):
        pass

    def __init__(self, n, costMatrix, *args, **kwargs):
        super().__init__()
        self.costMatrix = costMatrix
        self.n = n
        self.min_cost = sys.maxsize
        self.state_vector = [None for i in range(n+1)]
        self.min_sv = None


if __name__ == '__main__':
    n = int(input())  # order of the payoff matrix
    costs = []

    for i in range(n):
        line = str(input())  # rows of the payoff matrix
        line_split = list(line.split(" "))
        costs.append(list(map(lambda x: float(x), line_split)))

    assp = AssignmentProblem(n, costs)
    assp.run()
    print(assp.min_sv[1:])
    print(assp.min_cost)
