#!/usr/bin/python

import os

#ROOT_DIRECTORY = '/project/deliveries/'
ROOT_DIRECTORY = './test'
SEARCH_TEMPLATE = '/POJECT/EPISODE/SEQUENCE/SHOT/Comp/publish/render/VERSION'

# scan for a new directory with the following structure
# ROOTDIR/<user>/<shot>/<episode>/<sequence>/<step>/publish>/renders/<version>
## PSEUDxIOCODE
# if dir is found then
#     spawn anothe thread as we don't want to hold up the scanning
#     class watchdir
#         get shot name, length, task, artist from shotgun
#         if no shotname exit and email someone
#         if shot doesnt exist exit and email someone
#         if version already exists as published then exit
#         scan dir for files
#         while no_of_files == length && count == 1 
#         if no of files == length then
#             publih files into shotgun (which should also copy to project)
#             exit
#         if after a certain period ( eg 1/2 hour) files don't equal length then
#             email someone
#         if after 3hours files don't equal length then
#             email someone and exit
# 
class watchDirectory:
    '''
    Watch a directory for files
    '''

class scanRoot:
    '''
    Scan the root directory for new directories and spawn a directory watcher 
    when a new directory matching the required structure appears
    '''

    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(ROOT_DIRECTORY):
        path = root.split('/')

        template = (ROOT_DIRECTORY + SEARCH_TEMPLATE).split('/')
        print "path: %s, template: %s ", (path),  (template)
        if len(template) ==  len(path):
            print "got one"

        print (len(path) - 1) *'---' , os.path.basename(root)       
#        for file in files:
#            print len(path)*'---', file





if __name__ == "__main__":
    scanRoot()


