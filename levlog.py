import sys
from pprint import pprint
import Levenshtein

lev_treshold = float(sys.argv[2])
log_dict = {}
with open(sys.argv[1]) as log_file:
    for log_line in log_file.readlines():

        if len(log_dict.keys()) == 0:
            log_dict[log_line] = 1

        else:
            matched = False
            for saved_log_line in log_dict.keys():
                if Levenshtein.ratio(saved_log_line, log_line) >= lev_treshold:
                    log_dict[saved_log_line] += 1
                    matched = True

            if not matched:
                log_dict[log_line] = 1

pprint(log_dict)
