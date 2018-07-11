# Copyright(c) 2018 PaddlePaddle.  All rights reserved.
# Created on 2018
#
# Author:Lin_Bo
# Version 1.0
# filename: reader.py

import os

filename="infer.py"

f =open(filename,"rb")

tmp = []
for line in f:
    line_ = str = line.replace('\t', '    ').rstrip()
    tmp.append(line_)
f.close()

fw =open(filename,"wb")

for line_ in tmp:
    fw.write(line_+"\n")

fw.close()
