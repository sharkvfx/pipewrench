#!/usr/local/bin/python2.6

import os
import sgtk

#ROOT_DIRECTORY = '/project/deliveries/'
#ROOT_DIRECTORY = './test'
ROOT_DIRECTORY = '/array/X/outsource/michael/to_mvrcks'
SEARCH_TEMPLATE = '/POJECT/EPISODE/SEQUENCE/SHOT/Comp/publish/render/VERSION'
VALID_FILES = ['jpg','jpeg','cin','dpx','tif','tiff','png']
 


def fileSequence(files):
    ''' Check File list for a valid sequence i.e. 
    - frame numbers (padded)
    - no missingn numbers
    - return start frame, end frame and total
    '''
    # get file numbers
    fnumbers = []
    files.sort()
    for file in files:
        fnumbers.append (int(file.split('.')[-2]  ))
    fnumbers.sort()
    start = fnumbers[0]
    length = len(fnumbers)
    end = fnumbers[-1]

    for i in range(len(fnumbers)):
        # dont check for first frame
	# check for a valid sequence of numbers
        if i != 0:
	    #print fnumbers[i]
            if fnumbers[i] == i + start:
                #print "OK: ", fnumbers[i]
		if files[i].split('.')[0] != files[0].split('.')[0]:
			print files[i], files[0]
			print "File names are not consistent"
			return False
            else:
                print "File numbers are not contiguous"
                return False

    # print fnumbers
    #print "This is a valid sequence: ",start, end, length
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
	files.sort()
        for file  in files:
# NEED A BETTER WAY TO CHECK REQUEST TO PUBLISH
            if file.lower() == 'publish.txt':
                print "publish.txt exists"
                publish = True
            else:
                if file.split('.')[-1].lower() in VALID_FILES:
                    #print "Valid File: ", file
                    pfiles.append(file)
        if publish is True:
            if fileSequence(pfiles)  is False:
                print "NOT A SEQUNCE"
            else:
                print "Valid Sequnce - publish"
		# get details of project/episode/sequence/shot/version from file
		data =  self.root.split('/')[-1].split('_')
		#project = self.root.split('/')[3]
		project = 'pipetest2'
		version = data[-1]
		shot = data[0].split('-')[-1]
		sequence = data[0].split('-')[1]
		episode = data[0].split('-')[0]
		print "project %s epsispde %s sequence %s shot %s version %s" % (project, episode, sequence, shot, version)



		tkpath = '/array/X/outsource/michael/to_mvrcks/pipetest2/Ep01/seq01/ep01-seq01-shot030/Comp/publish/renders/Ep01-seq01-shot030_Comp_v001/ep01-FE-020_comp_v001.%04d.dpx'
		ctxpath = "/array/X/" + project + "/episodes/"+episode+"/"+sequence+ "/" + shot + "/Comp/"
		#ctxpath = '/array/X/outsource/michael/to_mvrcks/pipetest2/Ep01/seq01/ep01-seq01-shot030/Comp/publish/renders/Ep01-seq01-shot030_Comp_v001/
		#os.makedirs(ctxpath)
		

		#sgEntity = tk.entity_from_path(ctxpath)
		#print sgEntity

		tk = sgtk.sgtk_from_path(ctxpath)
		ctx = tk.context_from_path(ctxpath)
		publish = sgtk.util.register_publish( tk, ctx , tkpath, "Publish Name", 001 )
		print publish

class scanRoot:
    '''
    Scan the root directory for new directories and spawn a directory watcher 
    when a new directory matching the required structure appears
    '''
    # traverse root directory, and list directories as dirs and files as files
    print "Scanning ", ROOT_DIRECTORY
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

