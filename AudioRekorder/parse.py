import time
import argparse
import requests
#Parser
parser = argparse.ArgumentParser('Just a test')
parser.add_argument('url')
parser.add_argument('--fileName', '-f', required=True)
parser.add_argument('--duration', '-d', type=int, default=20)
arg = parser.parse_args()
#Überprufung richtig übergebene Eingabe
print(arg.url, arg.duration, arg.fileName)

#Default Name
default_file_name = time.strftime( "%Y%m%d%H%M%S",time.localtime())+".mp3"

#Param: FileName, URL, Duration
def record_audio(path=default_file_name, stream_url="http://stream.electroradio.fm/192k", duration = 20):
    #Zuweisung
    print("Recording audio...")
    filename = path
    m_file = open(filename, 'wb')
    chunk_size = 1024
    start_time_in_seconds = time.time()

    time_limit = duration - 11 if duration > 11 else 1 # time in seconds, for recording
    time_elapsed = 0
    url = stream_url

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


record_audio(arg.fileName, arg.url, arg.duration)