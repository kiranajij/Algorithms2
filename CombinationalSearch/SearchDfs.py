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
        elems = [self.elements[i] for i in range(self.n) if self.state_vector[i+1]]
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
