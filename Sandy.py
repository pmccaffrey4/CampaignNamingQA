# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:57:59 2019

@author: Sandy Sun
"""

name = 'Sandy'
age = '23'
hobbies = ['Hanging w/ Friends & Family', 'Watching dope tv shows', 'Singing in the mirror']

if __name__ == '__main__':

    print(f'My Name is {name}')
    print(f'I am {age} years old')

    print('My favorite things to do are...')
    for i, h in enumerate(hobbies):

        print(f'Hobby #{i + 1}  {h}')