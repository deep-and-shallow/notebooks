input_folder = 'mozartdicegame'  # Folder containing your original MIDI files
output_folder = 'mozartdicegame2'  # Folder to save the new MIDI files

import os
import mido
from mido import MidiFile, MidiTrack, Message,  MetaMessage



# List all MIDI files in the input folder
midi_files = [f for f in os.listdir(input_folder) if f.endswith('.mid')]

for midi_file in midi_files:
    # Load the MIDI file
    midi_path = os.path.join(input_folder, midi_file)
    midi_data = MidiFile(midi_path)
    
    # Create a new MIDI file with 2/4 time signature
    new_midi = MidiFile(ticks_per_beat=midi_data.ticks_per_beat)
    new_track = MidiTrack()
    
    # Add a time signature event (manually create bytes)
    time_signature_msg = MetaMessage('time_signature', time=0, numerator=2, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8)
    new_track.append(time_signature_msg)
    
    ticks_per_beat = midi_data.ticks_per_beat
    ticks_per_measure = ticks_per_beat * 2
    
    for msg in midi_data.tracks[0]:
        if msg.time <= ticks_per_measure:
            new_msg = msg.copy(time=msg.time)
            new_track.append(new_msg)
        else:
            break
    
    new_midi.tracks.append(new_track)
    
    # Save the new MIDI file
    new_midi_path = os.path.join(output_folder, midi_file)
    new_midi.save(new_midi_path)

print("Conversion complete.")