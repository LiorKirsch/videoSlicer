'''
Created on Jul 28, 2012

@author: lior
'''
from subprocess import Popen, PIPE
import subprocess
import pickle
import os
from urlparse import parse_qs, urlparse

class VideoCutter(object):
    '''
    to cut a video using ffmpeg:
        ffmpeg -sameq -ss [start_seconds] /
        -t [duration_seconds] -i [input_file] [outputfile]
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        
        
    @staticmethod
    def cutVideo(startTime, endTime ,infile = None, outputFile = None):
        
        if float(endTime) < float(startTime):
            raise Exception('timeMismatch', 'endTime must be greater then startTime')
        
        duration = float(endTime) - float(startTime)
        duration = str(duration)
        
        if infile is None:
            p=subprocess.call(["ffmpeg", "-i", "XAolCtofOtA.mp4", '-ss','65','-t','32','-y', "out.mp4"]                   )
            print p 
             
        else:
            p=subprocess.call(["ffmpeg", '-y' ,'-ss', startTime, '-t', duration, "-i", infile, "-vcodec" ,"copy" ,"-acodec" ,"copy",  outputFile] )
            print p
        
        if p is not 0:
            raise Exception("bad slicing happened")

        return
#            with open(infile, "rb") as infile:
#                 p=Popen(["ffmpeg", "-i", "-", "-f", "matroska",  '-ss',startTime ,'-t',duration, "-"], stdin=infile, stdout=PIPE)
#                data = p.stdout.read()
#                p.wait()
#                fileOut = p.stdout
            
        
#        f = open(outputFile, 'w')
#        f.write(data)
#        f.close()    
#        return fileOut

    
    def testingVideo(self, infile = None):
        
        if infile is None:
            p=subprocess.call(["ffmpeg", "-i", "XAolCtofOtA.mp4", '-ss','65','-t','32','-y', "out.mp4"]                   )
            print p 
             
        else:
            with open("XAolCtofOtA.mp4", "rb") as infile:
                p=Popen(["ffmpeg", "-i", "-", "-f", "matroska", "-vcodec", "mpeg4",
                    "-acodec", "aac", "-strict", "experimental", "-"],
                       stdin=infile, stdout=PIPE)
                
                
                while True:
                    data = p.stdout.read(1024)
                    if len(data) == 0:
                        break
                    # do something with data...
                    print(data)
            print p.wait() # should have finisted anyway
            
        return data
    
if __name__ == '__main__':
    print os.getcwd()
    
    videoUrl = 'http://www.youtube.com/watch?v=Uhgxr47tAMs'
    video_id = parse_qs(urlparse(videoUrl).query)['v'][0]
    print(video_id)
    p=subprocess.call(["./downloadVideo.py", "-f", "18", videoUrl]                   )
    a = VideoCutter()
    fileName = '%s.mp4' % video_id
    seconds = str(1*60 + 04)
    end = str(1*60 + 44)
    data = a.cutVideo(startTime=seconds, endTime=end, infile=fileName)