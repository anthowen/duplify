#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:53:34 2018

@author: jachi
"""
from dedupper.models import Simple, RepContact, SFContact
import string
from time import clock
from random import *
from range_key_dict import RangeKeyDict
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process #could be used to generate suggestions for unknown records
import numpy as np
from copy import deepcopy

#find more on fuzzywuzzy at https://github.com/seatgeek/fuzzywuzzy

df = None
dups = list()
new_records = list()
unsure = list()

rkd = RangeKeyDict({
    (100, 101): 'Duplicate',
    (70, 100): 'Undecided',
    (0, 70): 'New Record'
})

"""
TODO clean up comments
TODO create special case for phones and emails
"""

def key_generator(partslist):
    print(partslist)
    for key_parts in partslist:
        if 'phone' in key_parts:
            index = partslist.index(key_parts)
            del partslist[index]
            for i in ['homePhone', 'mobilePhone', 'workPhone']:
                new_key_parts = [i if x == 'phone' else x for x in key_parts]
                partslist.insert(index, new_key_parts)
        if 'email' in key_parts:
            index = partslist.index(key_parts)
            del partslist[index]
            for i in ['personalEmail', 'workEmail', 'otherEmail']:
                new_key_parts = [i if x == 'email' else x for x in key_parts]
                partslist.insert(index, new_key_parts)
    print(partslist)


    # for key_parts in partslist:

    rep_list = list(RepContact.objects.filter(type__in=['Unsure', 'New Record']))
    rep_keys = [i.key(partslist[0]) for i in rep_list]
    start = clock()
    rep_map = dict(zip(rep_keys,rep_list))

    sf_list = list(SFContact.object.all())
    sf_keys = [i.key(partslist[0]) for i in sf_list]
    sf_map = dict(zip(sf_keys, sf_list))

    for rep_key in rep_keys:
        key_matches = match_keys(rep_key,sf_keys)
        match_map = list(zip(key_matches,sf_keys))
        match_map = sorted(match_map, reverse=True)
        top1, top2, top3 = [(match_map[i][0],sf_map[match_map[i][1]]) for i in range(3)]
        person = rep_map[rep_key]

        if top1[0] <= top3[0]+25:
            person.average = np.mean([top1[0],top2[0],top3[0]])
            person.closest1 = top1[1]
            person.closest2 = top2[1]
            person.closest3 = top3[1]
        elif top1[0] <= top2[0]+25:
            person.average = np.mean([top1[0],top2[0]])
            person.closest1 = top1[1]
            person.closest2 = top2[1]
        else:
            person.average = top1[0]
            person.closest1 = top1[1]
        #seperate by activity
        person.type  = sort(person.average)
        #try-catch for the save, error will raise if match_contactID is not unique
        person.save()


    end = clock()
    time = str(end - start)
    print('...dedupping and sorting complete \t time = ' + time)
    print('\a')


def match_keys(key,key_list):
    for i in key_list:
        yield match_percentage(key,i)

def sort(avg):
    return rkd[avg]

def match_percentage(key1,key2):
    return fuzz.ratio(key1, key2)

def setSortingAlgorithm(min_dup,min_uns):
    #TODO finish this function and connect it to a slider
    global rkd
    rkd = RangeKeyDict({
    (min_dup, 101): 'Duplicate',
    (min_uns, min_dup): 'Unsure',
    (0, min_uns): 'New Record'
})

def classify_records(key1, key2):
    percent = match_percentage(key1,key2)
    return(rkd[percent],str(percent)+'%')

def mutate(keys):
    mutant = keys.copy()
    num_mutating = randint(int(len(keys)/5),int(len(keys)*0.8))

    for i in range(num_mutating):
        j = randint(0,len(keys)-1)
        for i in range(randint(3,len(mutant[j])+3)):
            mutant[j]=mutant[j].replace(mutant[j][int(sample(range(len(mutant[j])-1), 1)[0])], choice(string.printable))
    return mutant


def dedup(key):
    print('...entering dedup process')
    start = clock()
    sorted_bin = []
    #only dedup unsure list, aka start off with the keys
    #in the unsure list, pop them into new list or leave them
    #then iterate thru key set
    sf_list=mutate(key)

    for i in range(len(key)):
        classify,percent = classify_records(key[i],sf_list[i])
        sorter(classify, i, percent)
        if(classify != 'Unsure'):
            sorted_bin.append(i)
    df.drop(df.index[sorted_bin], inplace = True)
    end = clock()
    time = str(end-start)
    print('...dedupping and sorting complete \t time = '+time)

def get_lists():
    return(dups, new_records, list(df.values))

