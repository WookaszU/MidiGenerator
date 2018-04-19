try:
    from mido import MidiFile
except ImportError:
    raise ImportError("You dont have mido module which is required to run this program. Innstall mido with pip: "
                      "pip install mido")

import random

class algorithm:

    def makeStatistics(self, paths):

        notePropability = [[0.0] * 128 for i in range(128)]
        velocityPropability = [[0.0] * 128 for i in range(128)]
        notecount = [0] * 128
        notes = []
        velocity = []

        for path in paths:
            midiin = MidiFile(path)
            for msg in midiin:

                if not msg.is_meta and msg.type == 'note_on':
                    notecount[msg.note] += 1  # zliczam ilosc wystapien nut
                    notes.append(msg.note)
                    velocity.append(msg.velocity)

            # zliczam wystapienia nut po innych nutach na podstawie listy nut z poprzedniej petli
            for note in range(len(notes) - 1):
                notePropability[notes[note]][notes[note + 1]] += 1
                velocityPropability[notes[note]][notes[note + 1]] += 1

            # obliczanie prawdopodobienst wystapienia nut i velocity po poprzednich
            for i in range(128):
                sumN = 0
                sumV = 0
                for j in range(128):
                    sumN += notePropability[i][j]
                    sumV += velocityPropability[i][j]
                if sumN != 0:
                    for k in range(128):
                        notePropability[i][k] /= sumN
                if sumV != 0:
                    for k in range(128):
                        velocityPropability[i][k] /= sumV

        return (notePropability,velocityPropability,notes,velocity)


    # funkcja losujaca z okreslonych prawdopodobienstw
    def choose_propabil(self, propability_table, prev_value, in_midi):
        notes = []
        propabilities = []

        for i in range(128):
            if (propability_table[prev_value][i] != 0.0):
                notes.append(i)
                propabilities.append(propability_table[prev_value][i])

        sumprop = 0

        # jesli jakas nuta bez nastepcow to losujemy z puli wystepujacych
        if len(propabilities) == 0:
            randindex = random.randint(0, len(in_midi) - 1)
            return in_midi[randindex]

        #print(notes)
        #print(propabilities)

        randgive = random.random()
        #print(randgive)

        tmp = propabilities[0]

        length = len(propabilities)
        choosen = 0
        while tmp <= randgive and choosen < length - 1:
            choosen += 1
            tmp += propabilities[choosen]

        #print(notes[choosen], "\n")
        return notes[choosen]


    def compose(self, length, path, nutes_max):

        statistics = self.makeStatistics(path)
        notes = statistics[2]
        velocity = statistics[3]
        notePropability = statistics[0]
        velocityPropability = statistics[1]

        add_note = notes[random.randint( 0, len(notes)-1) ]  #start_note  #64
        add_velocity = velocity[random.randint( 0, len(velocity)-1) ]  #start_velocity  #30

        midinotes = []

        for i in range(length):
            duration = random.randint(1,10)
            nutes_number = random.randint(1,nutes_max)

            for k in range(nutes_number):
                add_note = self.choose_propabil(notePropability, add_note, notes)
                add_velocity = self.choose_propabil(velocityPropability, add_velocity, velocity)
                element = [i, add_note, add_velocity, duration]
                midinotes.append(element)

        return midinotes







