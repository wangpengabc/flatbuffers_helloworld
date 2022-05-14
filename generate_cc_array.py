from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import struct
import wave


def generate_array(input_fname):
  with open(input_fname, 'rb') as input_file:
    out_string = ''
    byte = input_file.read(1)
    size = 0
    while byte:
      out_string += '0x' + byte.hex() + ','
      byte = input_file.read(1)
      size += 1
    return [size, out_string]

def generate_filei_cc(output_cc_fname, array_name, array_type, array_contents, size):
  out_cc_file = open(output_cc_fname, 'w')
  out_cc_file.write('#include <cstdint>\n\n')
  out_cc_file.write('#include "monster_data.h"\n\n')
  out_cc_file.write('const unsigned int {}_size = {};'.format(array_name, str(size)))
  out_cc_file.write('alignas(16) const {} {}[] = {{'.format(array_type, array_name))
  out_cc_file.write(array_contents)
  out_cc_file.write('};\n')
  out_cc_file.close()


def generate_filei_hdr(output_hdr_fname, array_name, array_type, array_contents, size):
  out_hdr_file = open(output_hdr_fname, 'w')
  out_hdr_file.write('#include <cstdint>\n\n')
  out_hdr_file.write('extern const unsigned int {}_size;'.format(array_name))
  out_hdr_file.write('extern const {} {}[];\n'.format(array_type, array_name))
  out_hdr_file.close()

output_cc_fname = "monster_data.cc"
output_hdr_fname = "monster_data.h"

input_file = "monsterdata.bin"
size, cc_array = generate_array(input_file)

generate_filei_cc(output_cc_fname, "g_monster_data", "unsigned char", cc_array, size)
generate_filei_hdr(output_hdr_fname, "g_monster_data", "unsigned char", cc_array, size)






