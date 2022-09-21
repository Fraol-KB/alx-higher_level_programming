#!/usr/bin/python3
for ch in range(97, 123):
    if ch not in [113,101]:
        print(f"{ch:c}", end='')
