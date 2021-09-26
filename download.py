import sys
import requests
from utils import get_img_from_pattern, post_process_urls, download_images_from_url


# get the url from cli argument
if not sys.argv or len(sys.argv) < 2:
    print("Please enter the url")
    sys.exit(1)


urls = sys.argv[1:]

headers = {
  'cookie': '; over18=1; csv=1; edgebucket=n5rJ5bFE4Uny6le0yO; loid=0000000000eu5829xc.2.1632644018000.Z0FBQUFBQmhVQ3V5QTk2QUx0amEwVmNlY3N6MG1tdG1CR1VuUktXYWk2V2oxOHlYTlJYMjF3QWlMMEJKblBvUWhKcmFYRlo2Tm1QRW02dHd3V24wZ19PVzcwdTV0eFlWazBBdG5RRzhfRmkxb1EydXBKY1g1M3hHQTVqYjFhLWxmazdkMlJNRGxhVGc; session_tracker=rrofdoorceqrpkrbcb.0.1632644018846.Z0FBQUFBQmhVQ3V5ckJPbEFDRUlhcmJOa3Q3N0MzN2VjejRnQnJ2a0pYeWs4N2dyQkpSdmw5ZHBmUEt2am9IbXlDMEM2NlFHc2xkUzJuNWFLUEtRamFnWDFzblZsV3pnVENLOGhvV0dxajdia3hNcVVvWGNFUFRsbVZLMHg3MWZJbldrUkZ2Ykx4b0E; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzI2NDc0OTgsInN1YiI6Ii1rblZzdHp3STYtY01mLUNjQ2xXcFdBZ1BjdG8iLCJsb2dnZWRJbiI6ZmFsc2UsInNjb3BlcyI6WyIqIiwiZW1haWwiLCJwaWkiXX0.pKsmyLw8yShhuTtWwHENHjGBf_MwG0_yG1iwuI0ORA4'
}

all_images = []

for _ in range(10):
    for url in urls:
        # make a get request to the url
        response = requests.get(url, headers=headers)
        images = get_img_from_pattern(response.text)
        all_images += images

all_images = post_process_urls(all_images)
download_images_from_url(all_images)
