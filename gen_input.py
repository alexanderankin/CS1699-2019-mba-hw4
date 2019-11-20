#!/usr/bin/env python3
"""
* Your application should process 100 records and generates an output similar
to what is shown on slide #15 in this lecture.
* Each record of your input records should represent a ternary mix of maximum
of 5 different products (A, B, C, D, E).
* Each product of your 5 products should be represented at least 10 times in
your input data set. Your input format looks like the following:

TransactionId, product1 product2 product3

* Example of Input:

1, A B C
2, C D E
3, A B E

"""
import random

products = [chr(a) for a in range(ord('A'), ord('F'))]

def ensure_rows(products, rows, min_count):
  for product in products:
    times = 0
    for row in rows:
      trx_products_str = row.split(', ')[1]
      trx_products = trx_products_str.split(' ')
      if product in trx_products:
        times += 1

    # check that product appears min_count times
    if times < min_count:
      print('product %s only appears %d times' % (product, times))
      return False
  return True

def main():
  rows = []
  for transaction_id in range(1, 101):
    trx_products = [random.choice(products) for i in range(3)]
    rows.append(str(transaction_id) + ', ' + ' '.join(trx_products))

  ensure_rows(products, rows, 10)

  with open('input.txt', 'w') as input_file:
    input_file.write('\n'.join(rows))

if __name__ == '__main__':
  main()
