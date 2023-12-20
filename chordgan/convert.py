import sys
import numpy as np
import pretty_midi
import matplotlib.pyplot as plt


def forward(t):
    #prettymidi piano roll to ganmidi piano roll
    #midi_data = pretty_midi.PrettyMIDI('Barbie Girl - Chorus.mid')
    #t = midi_data.get_piano_roll(fs=16)
    ret = t[24:102, :]
    for i in np.arange(np.shape(ret)[0]):
        for j in np.arange(np.shape(ret)[1]):
            if(ret[i,j]>0):
                ret[i,j] = 1
    rhythm = np.zeros((78, np.shape(ret)[1]))
    for i in np.arange(np.shape(ret)[0]):
        if(ret[i, 0] > 0):
            rhythm[i, 0] = 1

    for i in np.arange(np.shape(ret)[0]):
        for j in np.arange(np.shape(ret)[1]):
            if(j == 0):
                 continue

            if(ret[i, j] > 0 and ret[i, j-1] == 0):
                rhythm[i, j] = 1
    res = np.concatenate((ret, rhythm))
    res = res[:, ::2]
    res = np.transpose(res)
    return res


def back(res):
    #ganmidi piano roll to prettymidi piano roll
    #res = np.transpose(res)
    inputnotes = res[:78, :np.shape(res)[1]]
    inputrhythm = res[78:, :np.shape(res)[1]]
    midiback = np.zeros((78, 2*np.shape(inputnotes)[1]))
    for i in np.arange(np.shape(inputnotes)[0]):
        for j in np.arange(np.shape(inputnotes)[1]):
            midiback[i, 2*j] = inputnotes[i, j]
            midiback[i, 2*j+1] = inputnotes[i, j]
    for i in np.arange(np.shape(inputnotes)[0]):
        for j in np.arange(np.shape(inputrhythm)[1]):
            if(j == 0):
                continue
            if(inputrhythm[i, j] == 1):
                midiback[i, 2*j-1] = 0
            
    for i in np.arange(np.shape(midiback)[0]):
        for j in np.arange(np.shape(midiback)[1]):
            if(midiback[i, j] > 0):
                midiback[i, j] = 100
                
    tempblock = np.zeros((24, np.shape(midiback)[1]))
    tempblock2 = np.zeros((26, np.shape(midiback)[1]))

    tomidi = np.concatenate((tempblock, midiback))
    fina = np.concatenate((tomidi, tempblock2))
    
    return fina
    #test2 = reverse_pianoroll.piano_roll_to_pretty_midi(fina, fs=16)
    #test2.write('helpp.mid')
            
            
            
            
            
            
            
