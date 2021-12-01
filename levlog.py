import sys
from pprint import pprint
import Levenshtein

lev_treshold = float(sys.argv[1])
input_filenames = sys.argv[2:]
log_dict = {}

for input_filename in input_filenames:
    with open(input_filename) as log_file:
        for log_line in [line.rstrip('\n') for line in log_file]:

            matched = False
            for saved_log_line in log_dict.keys():
                if Levenshtein.ratio(saved_log_line, log_line) >= lev_treshold:
                    log_dict[saved_log_line] += 1
                    matched = True
                    break

            if not matched:
                log_dict[log_line] = 1


for k, v in log_dict.items():
    print('\t'.join([str(v), k]))
