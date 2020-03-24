import time
import requests


print('Recording audio...')
#Std Name des Files
filename = time.strftime("%Y%m%d%H%M%S",time.localtime())+".mp3"
#Aufruf in Binär
m_file = open(filename, 'wb')
#Größe
chunk_size = 1024

start_time_in_seconds = time.time()

time_limit = 1 # time in seconds, for recording
time_elapsed = 0
url = "http://stream.electroradio.fm/192k"
with requests.Session() as session:
    response = session.get(url, stream=True)
    for chunk in response.iter_content(chunk_size=chunk_size):
        if time_elapsed > time_limit:
            break
        # to print time elapsed
        if int(time.time() - start_time_in_seconds)- time_elapsed > 0 :
            time_elapsed = int(time.time() - start_time_in_seconds)
            print(time_elapsed, end='\r', flush=True)
        if chunk:
            m_file.write(chunk)

    m_file.close()