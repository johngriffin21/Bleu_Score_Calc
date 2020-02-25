from __future__ import division
import math


def compute_da_grams(x):
    onegram = []
    twogram = []
    threegram = []
    fourgram = []

    t = x.split()

    # OneGram
    i = 0
    while i < len(t):
        onegram.append(t[i])
        i += 1

    # twogram
    i = 0
    x = 2
    while i + 1 < len(t):
        twogram.append(t[i:x])
        i += 1
        x += 1

    # threegram
    i = 0
    x = 3
    while i + 2 < len(t):
        threegram.append(t[i:x])
        i += 1
        x += 1

    # fourgram
    i = 0
    x = 4
    while i + 3 < len(t):
        fourgram.append(t[i:x])
        i += 1
        x += 1

    return onegram, twogram, threegram, fourgram


def compute_da_grams_long(x):
    onegrams = []
    twograms = []
    threegrams = []
    fourgrams = []

    for i in x:
        a, b, c, d = compute_da_grams(i)
        onegrams.append(a)
        twograms.append(b)
        threegrams.append(c)
        fourgrams.append(d)

    return onegrams, twograms, threegrams, fourgrams


def bleuscore(t, r):
    print("started")
    onegramt, twogramt, threegramt, fourgramt = compute_da_grams(t)
    onegram, twogram, threegram, fourgram = compute_da_grams_long(r)
    li = [onegramt, twogramt, threegramt, fourgramt]
    xi = [onegram, twogram, threegram, fourgram]
    print("this is xi {} ".format(xi))

    number_measures = [0, 0, 0, 0]

    tots = [len(onegramt), len(twogramt), len(threegramt), len(fourgramt)]
    lengths = []

    for i in onegram:
        lengths.append(len(i) - 1)
    brevity_penalty = min(1.0, (len(onegramt) / max(lengths)))
    z = 0
    while z < len(li):
        for mainword in li[z]:
            sentence_tracker = 0
            for gram in xi[z]:

                tmp = 0
                for sentence in gram:
                    if mainword == sentence:
                        tmp += 1
                    if tmp > sentence_tracker:
                        sentence_tracker = tmp
            number_measures[z] += sentence_tracker

        z += 1
    i = 0
    p1 = number_measures[0] / tots[0]
    p2 = number_measures[1] / tots[1]
    p3 = number_measures[2] / tots[2]
    p4 = number_measures[3] / tots[3]
    jack = p1 * p2 * p3 * p4
    brev = round(brevity_penalty, 4)
    x = math.pow(jack, 1.0 / 4)
    ans = x * brev
    return ans


def main():
    print("main")
    t = "The gunman was shot dead by police ."
    r = ["The gunman was shot to death by the police .", "The gunman was shot to death by the police .",
         "Police killed the gunman .", "The gunman was shot dead by the police ."]
    print(bleuscore(t, r))


if __name__ == "__main__":
    main()
