state_vectr = []
debug = False
unique = False
major_order = True
pprint_enabled = True

pprint_config = {
    'header': True,
    'footer': True,
    'partions': True
}

counter = 0

def log(msg, **kwargs):
    if debug:
        print(msg, **kwargs)

def pprint(msg="", **kwargs):
    if pprint_enabled:
        print(msg, **kwargs)

def pprint_header(n):
    if not pprint_config['header']: return
    pprint_dash()
    pprint_dash()
    pprint(f"Printing Partions of: {n: >10}")
    pprint(f"Major Order: {major_order}\tUnique: {unique}")
    pprint_dash()

def pprint_footer(n):
    if not pprint_config['footer']:
        pprint()
        return

    global counter
    pprint_dash()
    pprint(f"Number of partitions: {counter: >10}")
    pprint_dash()
    pprint_dash()
    pprint()

def pprint_dash():
    pprint("-" * 40)

def initialize(n):
    global state_vectr, counter, pprint_enabled
    counter = 0
    state_vectr = [None for i in range(n)]

    if debug:
        pprint_enabled = False

    log(f"Initialize: state vector of size: {n=}")
    log(f"initialize: {debug=}, {unique=}, {major_order=}")

def is_solution(k, n):
    log(f"checking solution for {state_vectr[:k]=}", end="")
    if sum(state_vectr[:k]) == n:
        log("\tyes")
        return True
    log("\tno")
    return False

def process_solution(k, n):
    global counter
    counter += 1

    log(f"processing solution ({n=}, {k=}): {state_vectr=}| {counter=}")
    if pprint_config['partions']:
        pprint(f"|--({counter})--", end="")
        print(state_vectr[:k])


def generate_candidate(k, n):
    current_sum = sum(state_vectr[:k])
    candidates = []

    if major_order:
        iter_over = (i-1 for i in range(n-current_sum, 0, -1))
    else:
        iter_over = (i for i in range(n-current_sum))

    for i in iter_over:
        if not unique:
            candidates.append(i+1)
            continue
        try:
            if i+1 >= state_vectr[k-1]:
                candidates.append(i+1)
        except:
            candidates.append(i+1)

    log(f"candidates: ({n=}, {k=}): {candidates=}")
    return candidates

def run(k, n):
    if k==0:
        pprint_header(n)
        pprint(f"{n}")

    log(f"running: ({n=}, {k=}): {state_vectr=}")
    if is_solution(k, n):
        process_solution(k, n)
    else:
        cands = generate_candidate(k, n)
        for i in cands:
            state_vectr[k] = i
            run(k+1, n)

    if k==0:
        pprint_footer(n)
        if not pprint_enabled:
            print(f"count = {counter}\n")

if __name__ == "__main__":
    for i in range(5, 10):
        initialize(i)
        run(0, i)
