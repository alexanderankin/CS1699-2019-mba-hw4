#!/usr/bin/env python3
def map(trxs):
  emitted = []

  def sf(pair):
    """Small First"""
    if pair[0] > pair[1]:
      return (pair[1], pair[0])
    return (pair[0], pair[1])
  for trx in trxs:
    emitted.append(((trx['items'][0], trx['items'][1]), 1))
    emitted.append(((trx['items'][0], trx['items'][2]), 1))
    emitted.append(((trx['items'][1], trx['items'][2]), 1))

  return emitted

def reduce(mapped):
  reduced = []

  def have_pair_in_reduced(pair):
    for r in reduced:
      if r[0][0] == pair[0] and r[0][1] == pair[1]:
        return True
    return False

  for pi, pair in enumerate(mapped):
    if have_pair_in_reduced(pair):
      continue

    counter = 0
    for oi, other in enumerate(mapped):
      if (pi == oi):
        continue
      if other[0][0] == pair[0][0] and other[0][1] == pair[0][1]:
        counter += 1

    reduced.append((pair, counter))

  return [(r[0][0], r[1]) for r in reduced]

def main():
  trxs = []
  with open('input.txt', 'r') as input_file:
    for line in input_file:
      parts = line.split(', ')
      items = [i.strip() for i in parts[1].split(' ')]
      trx = { 'id': parts[0], 'items': items }
      trxs.append(trx)


  mapped = map(trxs)

  # for mapp in mapped:
  #   print(mapp)
  # return

  reduced = reduce(mapped)

  for r in reduced:
    print(r)

if __name__ == '__main__':
  main()