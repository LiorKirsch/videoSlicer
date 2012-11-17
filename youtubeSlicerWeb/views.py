from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.conf import settings

import cStringIO
import datetime

#from django.template import RequestContext
from django.utils import simplejson 
from django.views.decorators.csrf import csrf_exempt
from django.core.servers.basehttp import FileWrapper

from cutVideo import VideoCutter
import subprocess
from urlparse import parse_qs, urlparse
import os
import sys
import youtube_dl

VIDEO_FOLDER = settings.VIDEO_ROOT
def getBasic(request):
    my_data_dictionary = {}
    return render_to_response('base.html',
                          my_data_dictionary,
                          context_instance=RequestContext(request))

    
def getVideoDetails(request):
    originalUrl = request.GET.get('videoUrl')
    
    myArgs = []
    myArgs.append('-f')
    myArgs.append('18')
    myArgs.append('--skip-download')
    myArgs.append(originalUrl)
    videoData = youtube_dl._real_main(myArgs, VIDEO_FOLDER)
    
    if videoData is not None:
        videoUrl = videoData['url']
        thumbnail = videoData['thumbnail']
        videoId = videoData['id']
        returnObject = {'status': 'success','originalUrl':originalUrl, 'videoId':videoId, 'thumbnail':thumbnail, 'videoUrl':videoUrl}
    
    response = sendObjectAsJson(returnObject)
    return response
 

def getVideo(request):
    videoUrl = request.GET.get('videoUrl')
    video_id = request.GET.get('videoId')
  
    myArgs = []
    myArgs.append('-f')
    myArgs.append('18')
    myArgs.append(videoUrl)
    videoData = youtube_dl._real_main(myArgs, VIDEO_FOLDER)
    
    returnObject = {'status': 'success', 'videoId':videoData['id']}
    response = sendObjectAsJson(returnObject)
    return response
    
def downloadVideo(request):
    videoID = request.GET.get('videoId')
    fileName = '%s.mp4' % (videoID)
    fileLocation = '%s/%s' % (VIDEO_FOLDER, fileName)
    myFile = open(fileLocation) 
    resp = HttpResponse(FileWrapper(myFile), mimetype='application/octet-stream')
    contentString = 'attachment; filename=%s' % fileName
    resp['Content-Disposition'] = contentString
    return resp

def sliceVideo(request):
    videoId = request.GET.get('videoId')
    startSecond = request.GET.get('startSecond')
    endSecond = request.GET.get('endSecond')
    
    outputVideoId = '%s-%s-%s' % (videoId,startSecond,endSecond)
    fileName = '%s/%s.mp4' % (VIDEO_FOLDER,videoId)
    outputFileName = '%s/%s.mp4' % (VIDEO_FOLDER,outputVideoId)
    VideoCutter.cutVideo(startSecond, endSecond ,infile = fileName,outputFile=outputFileName)
    
    returnObject = {'status': 'success', 'videoId':outputVideoId}
    response = sendObjectAsJson(returnObject)
    return response
    
def sendObjectAsJson(myObjectDict):
    data = simplejson.dumps(myObjectDict, indent=4) 
    print 'returning: %s' % data
    resp = HttpResponse(data, mimetype='application/json')
    resp['Access-Control-Allow-Headers'] = '*'
    return resp

