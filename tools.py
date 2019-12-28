import pandas as pd
import numpy as np
from bosonnlp import BosonNLP
api_key = "mxCvWCsB.33448.yezpaq5is6oK"
import json
import re
import time
def wirte_result(content, filename):
    fout = open("./processed_data/"+filename, "a")
    fout.write(content)
    fout.close()


