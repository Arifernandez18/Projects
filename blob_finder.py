import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        self._blobs= []
        marked= stdarray.create2D(pic.width(),pic.height(),False)
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob= Blob()
                self._findBlob(pic,tau,i,j,marked,blob)
                if blob.mass()> 0:
                    self._blobs.append(blob)

        ...

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        beads = []
        for blob in self._blobs:
            if blob.mass() >= pixels:
                beads.append(blob)
        return beads
        ...

    # Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    # threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    # being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        if i<0 or i>=pic.width() or j<0 or j>=pic.height() or marked[i][j] or pic.get(i,j).luminance() < tau:
            return
        marked[i][j]= True
        blob.add(i,j)

        self._findBlob(pic, tau, i - 1, j, marked, blob)  # Left
        self._findBlob(pic, tau, i + 1, j, marked, blob)  # Right
        self._findBlob(pic, tau, i, j - 1, marked, blob)  # Up
        self._findBlob(pic, tau, i, j + 1, marked, blob)  # Down


    ...


# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == "__main__":
    _main()
