#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input('add 1st num: '))
    b = int(input('add 2nd num: '))
    c = int(input('add 3rd num: '))
    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        print('one or more of three added nums is even')
    else:
        print('no one of three added nums is even')
