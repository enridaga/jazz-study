#!/usr/bin/env python3
"""iReal Pro charts for I Got It Bad (run by make.sh)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import ireal

M7, m7, D7 = "^7", "-7", "7"
I=("1",M7); ii=("2",m7); V=("5",D7); vi=("6",m7); IV=("4",M7)
# Handout changes (qualities chosen for playback where the handout gives none)
A1 = [[I], [("3",D7),vi], [("2",D7)], [("2",D7)], [ii,V],
      [("b7",D7),("6",D7),("b6",D7),("5",D7)], [I,vi], [ii,V]]
A2 = A1[:6] + [[I], [("5",m7),("1",D7)]]
B  = [[IV], [IV], [("b7",D7)], [("b7",D7)], [I], [("3",m7),("6",D7)], [ii], [("5","7b9")]]
MAIN = A1 + A2 + B + A1
# Ellington/Webster score (concert), bar -> chords, where different
def a_alt(o):  # bars of an A section, offset o
    return {o+1:[I,IV], o+2:[("3",D7),vi], o+3:[("2","11")], o+4:[("2","11"),("2","13"),("2","7b13")],
            o+5:[("5","11"),("6","11")], o+6:[("b7","7#11"),("6",D7),("b6",D7),("5",D7)]}
ALT = {}
ALT.update(a_alt(0)); ALT.update({7:[("1","","3"),("b3","o")], 8:[ii,V]})
ALT.update(a_alt(8))
ALT.update({17:[("4","6")], 18:[IV], 21:[I,IV], 22:[("3",m7),("6","7b9")],
            23:[("2","-"),("6","7b9")], 24:[ii,V]})
ALT.update(a_alt(24)); ALT.update({31:[I], 32:[ii,V]})

EXERCISES = ["main", "secondary", "all-keys"]

if __name__ == "__main__":
    for f, _ in ireal.build(HERE, "I Got It Bad", "Ellington Duke", "Ballad", "G",
                            MAIN, ALT, [("A",8),("A",8),("B",8),("A",8)], EXERCISES):
        print(f)
