import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    pixels= int(sys.argv[1])
    tau= float(sys.argv[2])
    delta= float(sys.argv[3])
    frames= sys.argv[4: ]
    bf= BlobFinder(Picture(frames[0]),tau)
    prevBeads= bf.getBeads(pixels)

    for i in range(1,len(frames)):
        bf= BlobFinder(Picture(frames[i]),tau)
        currBeads= bf.getBeads(pixels)
        for currBead in currBeads:
            mindist= math.inf
            closestBead=None
            for prevBead in prevBeads:
                distance= prevBead.distanceTo(currBead)
                if distance<= delta and distance<mindist:
                    mindist= distance
                    closestBead=prevBead

            if closestBead is not None:
                stdio.writef("%.4f\n", mindist)

        # Write a newline character after processing all beads in the current frame
        stdio.writeln()
        # Update prevBeads for the next iteration
        prevBeads = currBeads

    ...


if __name__ == "__main__":
    main()
