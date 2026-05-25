from music21 import stream, note, midi
import random

output_notes = []

for i in range(50):
    new_note = note.Note(random.randint(60, 72))
    output_notes.append(new_note)

midi_stream = stream.Stream(output_notes)

midi_stream.write('midi', fp='output/generated_music.mid')

print("Music Generated")
