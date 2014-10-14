#!/usr/local/bin/python2.7
def r_fib(n):
  if n<=1:
    return 1
  return r_fib(n-1) + r_fib(n-2)

def m_fib(n, memo = None):
  if memo is None:
    memo = {0:1,1:1}
  if n not in memo:
    memo[n] = m_fib(n-1, memo) + m_fib(n-2, memo)
  return memo[n]
