'''
A neat handy script which lets you compute the pq_code_length given the raw dimensions of the euclidean embeddings.
'''

import argparse


def get_padded_dim(dim, pq_code_length):
  # Returns padded dim which is next size up from dim such that pq_code_length divides padded dim.
  if dim % pq_code_length == 0:
    return dim
  padded_dim = ((dim // pq_code_length) + 1) * pq_code_length
  return padded_dim

parser = argparse.ArgumentParser(description='Encoder training settings.')
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
required.add_argument('-d','--raw_dim', help='Dimension of raw descriptors (unpadded) output from a model.', type=int, required=True)
required.add_argument('-l','--pq_code_len', help='Desired PQ code length in bytes, often 64 or 128.', type=int, required=True)
args = vars(parser.parse_args())


if __name__ == '__main__':
  dim = args['raw_dim']
  pq_code_length = args['pq_code_len']
  padded_dim = get_padded_dim(dim, pq_code_length)
  print('''Inputs:
    Raw dimension             = {raw_dim}
    PQ code length (in bytes) = {pq_code_length}'''.format(raw_dim=dim, pq_code_length=pq_code_length))
  if padded_dim == dim:
    print('''Use encoder settings:
    Padded dim                = {padded} <- no change because already a multiple of PQ code length\t
    PQ code length (in bytes) = {in_bytes}\t
    PQ code length (in bits)  = {in_bits}'''.format(padded=padded_dim, in_bytes=pq_code_length, in_bits=8 * pq_code_length))
  else:
    print('''Use encoder settings:
    Padded dim                = {padded}\t
    PQ code length (in bytes) = {in_bytes}\t
    PQ code length (in bits)  = {in_bits}'''.format(padded=padded_dim, in_bytes=pq_code_length, in_bits=8 * pq_code_length))
