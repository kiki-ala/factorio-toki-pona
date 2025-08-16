#!/bin/python

for i in range(0, 512):
    bs = f"{i:>128b}"
    acc = ""
    bpairs = []
    for ch in bs:
        acc += ch
        if len(acc) == 4:
            if acc.strip():
                bpairs.append(acc.strip())
            acc = ""
    nimi = ""
    for bp in bpairs:
        match int(bp, 2):
            case 0:
                nimi += "nu"
            case 1:
                nimi += "wa"
            case 2:
                nimi += "tu"
            case 3:
                nimi += "wi"
            case 4:
                nimi += "po"
            case 5:
                nimi += "pa"
            case 6:
                nimi += "si"
            case 7:
                nimi += "se"
            case 8:
                nimi += "ke"
            case 9:
                nimi += "na"
            case 10:
                nimi += "te"
            case 11:
                nimi += "le"
            case 12:
                nimi += "we"
            case 13:
                nimi += "so"
            case 14:
                nimi += "lo"
            case 15:
                nimi += "pi"
    if i < 2:
        match i:
            case 0:
                nimi = "nu"
            case 1:
                nimi = "wa"
    print(f"{i}\t{nimi}")
    # print(f"{i}\t{bs.strip()}\t{bpairs}\t{nimi}")
