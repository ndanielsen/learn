#!/usr/bin/env python 

"""
Python fundaments because well... just because review is good.


"""

fun_dict = {'a':10, 'b':20, 'c':[30, 40]}
fun_dict['b'] = 25
fun_dict['c'][0] = 35

fun_dict['c'].append(45)


if __name__ == '__main__':

	print fun_dict
	# print funlist

	print [(key.upper(), fun_dict[key]) for key in fun_dict.keys()]