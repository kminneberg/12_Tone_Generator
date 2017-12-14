from abjad import *

def generateCircle(myList):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    start = notes.index(myList[0])
    circle = notes[start:] + notes[:start]
    return circle

def generateFirstLine(myList, circle):
    newList = []
    for eachNote in myList:
        newList.append(circle.index(eachNote))
    return newList

def generateNextLine(column, firstList):
    line = [column]
    for nextCol in range(1, 12):
        nextNum = firstList[nextCol] + column
        if nextNum >= 12:
            nextNum -= 12
        line.append(nextNum)
    return line

def validateInput(myStr):
    validNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    chosen = []
    for note in myStr.split():
        if note not in validNotes:
            return (False, "Note " + note + " is not a valid note!")
        elif note in chosen:
            return (False, "Note " + note + " has been entered more than once!")
        else:
            chosen.append(note)
    if len(myStr.split()) != 12:
        return (False, "Only " + str(len(myStr)) + " notes have been entered. 12 are required.")
    return (True, "Input is valid")

def main():
    matrix = []
    abjadMatrix = []
    firstLine = input("Enter your notes on a single line: ")
    result = validateInput(firstLine)
    while not result[0]:
        print(result[1])
        firstLine = input("Enter your notes on a single line: ")
        result = validateInput(firstLine)
    firstLine = firstLine.split()

    #Generate first line in numbers
    circle = generateCircle(firstLine)
    row0 = generateFirstLine(firstLine, circle)
    for item in row0:
        abjadMatrix.append(item+9)
    matrix.append(row0)

    #Generate remaining lines in numbers
    for num in range(1,12):
        colNum = 12- matrix[0][num]
        newLine = generateNextLine(colNum, row0)
        matrix.append(newLine)
        for item in newLine:
            abjadMatrix.append(item+9)

    print("Matrix (Numbers Forms)")
    for row in matrix:
        print("{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}{:4d}".
              format(row[0], row[1], row[2], row[3], row[4], row[5], row[6],\
                     row[7], row[8], row[9], row[10], row[11]))

    musicMatrix = []
    #Transform into letters
    for row in matrix:
        tmpList = []
        for note in row:
            tmpList.append(circle[note])
        musicMatrix.append(tmpList)

    #format the output
    print("\nMatrix (Notes Forms)")
    for row in musicMatrix:
        
        print("{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}".
              format(row[0], row[1], row[2], row[3], row[4], row[5], row[6],\
                     row[7], row[8], row[9], row[10], row[11]))

    #Generate music notation form
    duration = Duration(1, 8)
    time_sig = TimeSignature((4, 4))
    notes = [Note(pitch, duration) for pitch in abjadMatrix]
    staff = Staff(notes)
    attach(time_sig, staff[0])
    show(staff)

    print("PDF created...")
    print("\tTime Signature: 4/4")
    print("\tNote Duration: 8th Notes")
main()
        
