import numpy as np
import glob
import os

#number half steps from A
above = [0, 2, 3, 5, 7, 8, 10, 12]


# add songs to data
def convert2chroma(path):
    files = glob.glob('{}/*.txt*'.format(path))
    chromas = []
    for f in files:
        fr = open(f, "r")
        idx = 0
        chroma = np.zeros((13, 100))
        while (True):
            # read next line
            line = fr.readline()
            # if line is empty, you are done with all lines in the file
            if not line:
                break
            text = line.strip()
            if (len(text) == 1):
                # major triad, letter note
                shift = above[ord(text[0]) - 65]
                shift = (shift + 10) % 13
                chroma[shift, idx] = 1
                chroma[(shift + 4) % 13, idx] = 1
                chroma[(shift + 7) % 13, idx] = 1
            elif (len(text) == 2):
                if (text[1] == 'm'):
                    # minor triad, letter note
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 10) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 3) % 13, idx] = 1
                    chroma[(shift + 7) % 13, idx] = 1
                elif (text[1] == '7'):
                    # dom 7, letter note
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 10) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 4) % 13, idx] = 1
                    chroma[(shift + 7) % 13, idx] = 1
                    chroma[(shift + 10) % 13, idx] = 1
                elif (text[1] == '#'):
                    # major triad, sharp
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 11) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 4) % 13, idx] = 1
                    chroma[(shift + 7) % 13, idx] = 1
                elif (text[1] == 'b'):
                    # major triad, flat
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 9) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 4) % 13, idx] = 1
                    chroma[(shift + 7) % 13, idx] = 1
            elif (len(text) == 3):
                if (text[1] == 'M'):
                    # major 7, letter note
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 10) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 4) % 13, idx] = 1
                    chroma[(shift + 7) % 13, idx] = 1
                    chroma[(shift + 11) % 13, idx] = 1
                elif (text[1] == 'm'):
                    # minor 7, letter note
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 10) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 3) % 13, idx] = 1
                    chroma[(shift + 7) % 13, idx] = 1
                    chroma[(shift + 10) % 13, idx] = 1
                elif (text[2] == 'm'):
                    if (text[1] == '#'):
                        # minor chord, sharp
                        shift = above[ord(text[0]) - 65]
                        shift = (shift + 11) % 13
                        chroma[shift, idx] = 1
                        chroma[(shift + 3) % 13, idx] = 1
                        chroma[(shift + 7) % 13, idx] = 1
                    elif (text[1] == 'b'):
                        # minor chord, flat
                        shift = above[ord(text[0]) - 65]
                        shift = (shift + 9) % 13
                        chroma[shift, idx] = 1
                        chroma[(shift + 3) % 13, idx] = 1
                        chroma[(shift + 7) % 13, idx] = 1
                elif (text[2] == '7'):
                    if (text[1] == '#'):
                        # dom7, sharp
                        shift = above[ord(text[0]) - 65]
                        shift = (shift + 11) % 13
                        chroma[shift, idx] = 1
                        chroma[(shift + 4) % 13, idx] = 1
                        chroma[(shift + 7) % 13, idx] = 1
                        chroma[(shift + 10) % 13, idx] = 1
                    elif (text[1] == 'b'):
                        # dom7, flat
                        shift = above[ord(text[0]) - 65]
                        shift = (shift + 9) % 13
                        chroma[shift, idx] = 1
                        chroma[(shift + 4) % 13, idx] = 1
                        chroma[(shift + 7) % 13, idx] = 1
                        chroma[(shift + 10) % 13, idx] = 1
            elif (len(text) == 4):

                shift = above[ord(text[0]) - 65]
                if (text[1] == '#'):
                    shift = (shift + 11) % 13
                elif (text[2] == 'b'):
                    shift = (shift + 9) % 13
                chroma[shift, idx] = 1
                chroma[(shift + 4) % 13, idx] = 1
                chroma[(shift + 7) % 13, idx] = 1
                chroma[(shift + 11) % 13, idx] = 1

                if (text[2] == 'm'):
                    chroma[(shift + 4) % 13, idx] = 0
                    chroma[(shift + 3) % 13, idx] = 1
                    chroma[(shift + 11) % 13, idx] = 0
                    chroma[(shift + 10) % 13, idx] = 1



            elif (len(text) == 5):
                if (text[1] == 'd' and text[2] == 'i' and text[3] == 'm'):
                    shift = above[ord(text[0]) - 65]
                    shift = (shift + 10) % 13
                    chroma[shift, idx] = 1
                    chroma[(shift + 3) % 13, idx] = 1
                    chroma[(shift + 6) % 13, idx] = 1
                    chroma[(shift + 9) % 13, idx] = 1

            idx += 1
            chromas.append(chroma)
    return chromas