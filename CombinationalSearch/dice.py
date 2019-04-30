from CombinationalSearch.SearchDfs import AbstractBacktrackDFS


class Dice(AbstractBacktrackDFS):
    def __init__(self, n_dices, sum):
        super().__init__()

        self.n_dices = n_dices
        self.sum = sum

        self.state_vector = [0 for i in range(n_dices+1)]

    def is_solution(self, k, *args, **kwargs):
        return self.n_dices == k

    def process_solution(self, k, *args, **kwargs):
        if self.sum == 0:
            print(self.state_vector[1::])

    def generate_candidates(self, k, candidates, *args, **kwargs):
        for i in range(1, 7):
            if i < self.sum:
                candidates.append(i)

    def make_move(self, k, *args, **kwargs):
        self.sum += self.state_vector[k]

    def unmake_move(self, k, *args, **kwargs):
        self.sum -= self.state_vector[k]