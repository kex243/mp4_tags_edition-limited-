import xlrd
import mutagen
from mutagen.mp4 import MP4
from mutagen.id3 import ID3, TIT2

from os import listdir
from os.path import isfile, join

#improting video
mypath = "./input"
videomp4 = [f for f in listdir(mypath) if isfile(join(mypath, f))]




#importing excel file
workbook = xlrd.open_workbook('samples.xls')
#to list by index
worksheet = workbook.sheet_by_index(0)
# raw, cell
#show = worksheet.cell(1, 0).value
#print (show)

#file properties
#print (videomp4)

#metadata = MP4(mypath +'/'+ str(videomp4[0]))
#print (metadata)

a = mutagen.File("myfile.mp4").keys()
print (a)
mutagen.id3.PairedTextFrame
#for frame in mutagen.File("myfile.mp4").tags:
 #   print (frame)
print (mutagen.File("myfile.mp4").tags)
#attributes list
metadata = 'myfile.mp4'
mp4_video_tags = MP4(metadata)
mp4_video_tags['\xa9nam'] = '!1'
mp4_video_tags['\xa9gen'] = '!2tags'
mp4_video_tags['\xa9sub'] = '!2subtitles'
mp4_video_tags['subtitles'] = '!f3q2gtg32subtitles'
mp4_video_tags['\xa9alb'] = '!4!My Genre1'
mp4_video_tags['\xa9ART'] = '!5!artists'
mp4_video_tags['\aART'] = '!10!My Comments are very long'
mp4_video_tags['\xa9wrt'] = '!16!My Comments are very long'
mp4_video_tags['\xa9cmt'] = '!4My Com'
mp4_video_tags['\xa9tcm'] = '!etgw4egw'
mp4_video_tags['\xa9day'] = '2122' #7

mp4_video_tags['desc'] = '!8My Comments are very long'
mp4_video_tags['purd'] = '!9My Comments are very long'
mp4_video_tags['\xa9grp'] = '!10My Comments are very long'
mp4_video_tags['\xa9gen'] = '!6!My Comments are very long'
mp4_video_tags['\xa9lyr'] = '!9!My Comments are very long'
mp4_video_tags['purl'] = '!13My Comments are very long'
mp4_video_tags['egid'] = '!14My Comments are very long'
mp4_video_tags['catg'] = '!15My Comments are very long'
mp4_video_tags['keyw'] = '!16My Comments are very long'

mp4_video_tags['cprt'] = '!18My Comments are very long'
mp4_video_tags['soal'] = '!19My Comments are very long'
mp4_video_tags['soaa'] = '!20My Comments are very long'
#mp4_video_tags['tmpo'] = 4 #something taht doesnt work
#mp4_video_tags['\xa9too'] = '8!My Comments are very long'
#mp4_video_tags['soar'] = '21My Comments are very long'
#mp4_video_tags['sonm'] = '22My Comments are very long'
#mp4_video_tags['soco'] = '23My Comments are very long'
#mp4_video_tags['sosn'] = '24My Comments are very long'
#mp4_video_tags['tvsh'] = '25My Comments are very long'
#mp4_video_tags['\xa9wrk'] = '26My Comments are very long'
#mp4_video_tags['\xa9mvn'] = '27My Comments are very long'



mp4_video_tags.save()


#print(mutagen.File(metadata))
