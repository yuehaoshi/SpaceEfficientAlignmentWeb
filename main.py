import globall
import global_base
import fitting
import fitting_base
import local
import local_base

# generate random integer values
from random import seed
from random import randint
from datetime import datetime

seed(datetime.now())

keys = ['A', 'C', 'T', 'G', '-']
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}

def compute_score(va, wa):
    if not len(va) == len(wa):
        print("invalid alignment")
        return -1919810
    else:
        score = 0
        for i in range(len(va)):
            score += delta[va[i]][wa[i]]
        return score

def generate_sequence(l):
    ret = ""
    for i in range(l):
        it = randint(0, len(keys) - 2)
        ret += keys[it]
    return ret

def test_global(n):
    for i in range(n):
        vl = randint(1, 20)
        wl = randint(10, 100)
        v = generate_sequence(vl)
        w = generate_sequence(wl)
        (score_base, a_base) = global_base.global_align(v, w, delta)
        (va, wa) = globall.get_alignment(v, w, globall.hirschberg(v, w, delta))
        score = compute_score(va, wa)
        if not score == score_base:
            print(v, w, "optimal score:", score_base, "your_score:", score, va, wa)

def test_fitting(n):
    for i in range(n):
        vl = randint(1, 20)
        wl = randint(10, 100)
        v = generate_sequence(vl)
        w = generate_sequence(wl)
        (score_base, a_base) = fitting_base.fitting_align(v, w, delta)
        (va, wa) = fitting.fitting(v, w, delta)
        score = compute_score(va, wa)
        if not score == score_base:
            print(v, w, "optimal score:", score_base, "your_score:", score)

def test_local(n):
    for i in range(n):
        vl = randint(1, 20)
        wl = randint(10, 100)
        v = generate_sequence(vl)
        w = generate_sequence(wl)
        (score_base, a_base) = local_base.local_align(v, w, delta)
        (va, wa) = local.local(v, w, delta)
        score = compute_score(va, wa)
        if not score == score_base:
            print(v, w, "optimal score:", score_base, "your_score:", score)

test_local(50)