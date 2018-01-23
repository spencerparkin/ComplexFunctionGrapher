# test.py

from zeta_function import ZetaFunction

if __name__ == '__main__':
    result = ZetaFunction(-1)
    print('result = %f + %fj' % (result.real, result.imag))
    print('expected = %f' % (-1.0 / 12.0))