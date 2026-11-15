#!/usr/bin/env python3
"""iReal Pro charts for My Romance (run by make.sh)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import ireal

M7, m7, D7, H7 = "^7", "-7", "7", "h7"
I=("1",M7); ii=("2",m7); V=("5",D7); vi=("6",m7); IV=("4",M7)
MAIN = [  # 32 bars
 [I],[I],[ii,V],[I],          [vi],[vi],[ii,V],[I],
 [IV],[I],[IV],[I],           [("#4",H7),("7",D7)],[("3",m7),("6",D7)],[("2",D7)],[ii,V],
 [I],[I],[ii,V],[I],          [vi],[vi],[ii,V],[I],
 [IV],[IV],[("7",H7),("3",D7)],[vi],  [I,vi],[ii,V],[I],[ii,V]]
ALT = {  # Ben Webster changes (bar -> chords); other bars as MAIN
 1:[I,("4",D7)], 2:[("3",m7),("6",D7)], 4:[I,("3","7b9")],
 5:[vi,("6","-","#5")], 6:[("6","-","5"),("3",m7),("6",D7)], 8:[I,("1",D7)],
 9:[IV,ii,V], 10:[I,("1",D7)], 11:[IV,ii,V],
 14:[("3",m7),("b3",D7)], 16:[V],
 17:[I,("4",D7)], 18:[("3",m7),("6",D7)], 20:[I,("3","7b9")],
 22:[vi,("3",m7),("6",D7)], 24:[I,("1",D7)], 28:[vi,("b6",D7)], 29:[("1",M7,"5"),vi]}

# iReal exercises for this tune (ids from tools/ireal.py EXERCISES)
EXERCISES = ["all-keys", "main", "secondary"]

if __name__ == "__main__":
    for f, _ in ireal.build(HERE, "My Romance", "Rodgers Richard", "Medium Swing", "Bb",
                            MAIN, ALT, [("A", 16), ("B", 16)], EXERCISES):
        print(f)
