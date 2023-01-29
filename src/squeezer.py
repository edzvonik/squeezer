import io
import math
import sys
import numpy as np
from PIL import Image

class Squeezer:

    FILE_SIZE = 1500000

    @staticmethod
    def squeeze(im, filename, target):
        """
        Save the image as JPEG with the given name at best quality that makes less than "target" bytes
        URL: https://stackoverflow.com/a/52281257
        """
        # Min and Max quality
        Qmin, Qmax = 25, 96
        # Highest acceptable quality found
        Qacc = -1
        while Qmin <= Qmax:
            m = math.floor((Qmin + Qmax) / 2)

            # Encode into memory and get size
            buffer = io.BytesIO()
            im.save(buffer, format="JPEG", quality=m)
            s = buffer.getbuffer().nbytes

            if s <= target:
                Qacc = m
                Qmin = m + 1
            elif s > target:
                Qmax = m - 1

        # Write to disk at the defined quality
        if Qacc > -1:
            im.save(filename, format="JPEG", quality=Qacc)
        else:
            print("ERROR: No acceptble quality factor found", file=sys.stderr)