from speedtest import Speedtest

# Test Commit and git and github

st = Speedtest()

download = st.download() # bit
upload = st.upload() # bit

download_kilobyte = download / 8000
upload_kilobyte = upload / 8000

dowload_megabit = download_kilobyte / 125
upload_megabit = upload_kilobyte / 125

dowload_megabyte = download_kilobyte / 1000
upload_megabyte = upload_kilobyte / 1000

speed_key = {
    "1": [download, upload],
    "2": [download_kilobyte, upload_kilobyte],
    "3": [dowload_megabit, upload_megabit],
    "4": [dowload_megabyte, upload_megabyte]
}

ping = st.results.ping

selection = input("""Please enter the number to get the speed in your value
1 - Bit
2 - Kilobyte
3 - Megabit
4 - Megabyte 

Selection: """)

print("""
Download: {}
Upload: {}
Ping: {} """.format(round(speed_key[selection][0], 2), round(speed_key[selection][1], 2), round(ping)))

input()
