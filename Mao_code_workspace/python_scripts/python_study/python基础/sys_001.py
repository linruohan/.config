import sys

# print('\n'.join(sys.modules.keys()))

import glob

print(glob.glob(os.path.dirname(__file__)+'music/*.mp3'))
