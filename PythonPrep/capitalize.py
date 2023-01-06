'''

Given a full name, your task is to capitalize the name appropriately.

You are asked to ensure that the first and last names of
people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

'''

'''
STEPS:
    split each word and store it to an array

    iterate each word

'''
def capitalize(s):
    split_word = s.split(" ")

    for i in split_word:
        s = s.replace(i, i.capitalize())
    return s


capitalize("alison heck")