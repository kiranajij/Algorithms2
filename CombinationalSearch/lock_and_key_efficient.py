class LockAndKeyEfficient:
    def __init__(self, ndigs, n, cases, corr, wells):
        self.ndigs = ndigs
        self.n     = n
        self.cases = cases
        self.corrs = corrs
        self.wells = wells
        self.sv    = [None for i in range(n)]
    