'''
Created on Apr 30, 2015

@author: jchirag
'''
#from xoze.snapvideo import VideoHost
from xoze.snapvideo import VideoHost, Video, STREAM_QUAL_HD_720
from xoze.utils import http
import logging
import re

VIDEO_HOST_NAME = 'letwatch'

def getVideoHost():
    video_host = VideoHost()
    video_host.set_icon('http://letwatch.us.com/images/logo.png')
    video_host.set_name(VIDEO_HOST_NAME)
    return video_host

def retrieveVideoInfo(video_id):
    # Old Method
    #import urlresolver
    #videoUrl =  'http://letwatch.us/embed-' + str(video_id) + '-595x430.html'
    #media = urlresolver.HostedMediaFile(url=videoUrl, title='')   

    #New method to get 720links
    video = Video()
    video.set_video_host(getVideoHost())
    video.set_id(video_id)

    try:
        video_link = 'http://letwatch.us/embed-' + str(video_id) + '-595x430.html'
        html = http.HttpClient().get_html_content(url=video_link)
        img_link = re.compile('<span id=\'vplayer\'><img src=\"(.+?)\" style=').findall(html)[0]                
        video_link = re.compile('label:\"SD\"},{file:\"(.+?)\",label:\"HD\"').findall(html)[0]
        video.set_stopped(False)
        video.set_thumb_image(img_link)
        video.set_name("PLAYWIRE Video")
        if re.search(r'\Artmp', video_link):
            video.add_stream_link(STREAM_QUAL_HD_720, video_link)
        else:
            video.add_stream_link(STREAM_QUAL_HD_720, video_link)
    except:
        video.set_stopped(True)
    return video
