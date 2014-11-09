#!/usr/bin/python

import os

#ROOT_DIRECTORY = '/project/deliveries/'
ROOT_DIRECTORY = './test'
SEARCH_TEMPLATE = '/POJECT/EPISODE/SEQUENCE/SHOT/Comp/publish/render/VERSION'
VALID_FILES = ['jpg','jpeg','cin','dpx','tif','tiff','png']

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
def fileSequence(files):
    ''' Check File list for a valid sequence i.e. 
    - frame numbers (padded)
    - no missingn numbers
    - return start frame, end frame and total
    '''
    # get file numbers
    fnumbers = []
    for file in files:
        fnumbers.append (int(file.split('.')[-2]  ))
    fnumbers.sort()
    start = fnumbers[0]
    length = len(fnumbers)
    end = fnumbers[-1]

    for i in range(len(fnumbers)):
        # check for first frame
        if i != 0:
            if fnumbers[i] == i + start:
                print "OK: ", fnumbers[i]
            else:
                print "this is not a continuous sequence"
                return False

    print fnumbers
    print "This is a valid sequence: ",start, end, length
    return start, end, length




class watchDirectory:
    '''
    Watch a directory for files
    '''
    def __init__(self, root ):
              self.root = root

    def process(self):
        print "Watching %s", self.root

        #set up valid file list to publish
        pfiles = []
        publish = False
        
        # get directory listing
        files = os.listdir(self.root)
        for file  in files:
# NEED A BETTER WAY TO CHECK REQUEST TO PUBLISH
            if file.lower() == 'publish.txt':
                print "publish.txt exists"
                publish = True
            else:
                if file.split('.')[-1].lower() in VALID_FILES:
                    print "Valid File: ", file
                    pfiles.append(file)
        if publish is True:
            if fileSequence(pfiles)  is False:
                print "NOT A SEQUNCE"
            else:
                print "Valid Sequnce - publish"


class scanRoot:
    '''
    Scan the root directory for new directories and spawn a directory watcher 
    when a new directory matching the required structure appears
    '''

    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(ROOT_DIRECTORY):
        path = root.split('/')
        template = (ROOT_DIRECTORY + SEARCH_TEMPLATE).split('/')

        # check search path with template
        # should probably be more definitiive
        # eg. path[7] == 'Comp' 
        if len(template) ==  len(path):
            #print "got one --> ", root
            newdir = watchDirectory(root)
            newdir.process()

#        for file in files:
#            print len(path)*'---', file



if __name__ == "__main__":
    scanRoot()


