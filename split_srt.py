import re
subs=[]
start_time=[]
end_time=[]
dialogue=[]

def srt_time_to_seconds(time):
    split_time=time.split(',')
    major, minor = (split_time[0].split(':'), split_time[1])
    return int(major[0])*1440 + int(major[1])*60 + int(major[2]) + float(minor)/1000

def srt_store_to_database(srtText):
    
    for s in re.sub('\r\n', '\n', srtText).split('\n\n'):
        st = s.split('\n')
        if len(st)>=3:
            split = st[1].split(' --> ')
            subs.append({'start': srt_time_to_seconds(split[0].strip()),
                         'end': srt_time_to_seconds(split[1].strip()),
                         'text': '<br />'.join(j for j in st[2:len(st)])
                        })
            start_time.append(float(srt_time_to_seconds(split[0].strip())))
            end_time.append(float(srt_time_to_seconds(split[1].strip())))
            dialogue.append('<br/>'.join(f for f in st[2:len(st)]))
     
          
    return subs

