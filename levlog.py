import sys
from pprint import pprint
import Levenshtein

lev_treshold = float(sys.argv[1])
input_file_names = sys.argv[2:]

log_dict = {}

for input_file_name in input_file_names:
    with open(input_file_name) as log_file:
        for log_line in log_file.readlines():

            log_line = log_line.strip('\n')
            matched = False

            for saved_log_line in log_dict.keys():
                if Levenshtein.ratio(saved_log_line, log_line) >= lev_treshold:
                    log_dict[saved_log_line] += 1
                    matched = True

            if not matched:
                log_dict[log_line] = 1


pprint(log_dict)
