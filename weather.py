import json, requests
from PIL import Image, ImageDraw, ImageFont
from datetime  import date 
import sender 

api = "YOUR API KEY HERE"

positions = [600, 825, 1060, 1300, 1535]

uk_list = ["London", "Edinburgh", "Manchester", "Liverpool", "Glasgow", "UK"] 
tr_list = ["İstanbul", "Bursa", "Ankara", "İzmir", "Antalya", "TR"]
wrld_list = ["Seoul", "Tokyo", "Hokkaido", "Melbourne", "Sydney", "WORLD"]
city_list = [uk_list, tr_list, wrld_list]

#pdf files to store
pdf_files = []

for country in city_list:
    
    #PRINTING A IMAGE
    img = Image.open("story.png")
    draw = ImageDraw.Draw(img)

        #Fixed variable
    color = "rgb(255, 255, 255)"

        #1-Variables
    font = ImageFont.truetype("ClarityCity-Light.ttf", size=90)
    header = "Today's Weather Forecast"
    (x, y) = 38, 87

        #1-Printing
    draw.text((x, y), header, color, font=font)


        #2-Variables
    today = date.today()
    header = today.strftime("%A - %B %d, %Y ")
    font = ImageFont.truetype("ClarityCity-Light.ttf", size=60)
    (x, y) = 45, 272

        #2-Printing
    draw.text((x, y), header, color, font=font)

    i = 0
    for city in country:
        if i < 5:
            url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api)
            response = requests.get(url)
            data = json.loads(response.text)
            color = 0,0,0
            
            
            #city name
            font = ImageFont.truetype("ClarityCity-Light.ttf", size=100)
            (x, y) = 43, positions[i]
            draw.text((x, y), city, color, font=font)
            
            #temperature
            font = ImageFont.truetype("ClarityCity-Light.ttf", size=100)
            header = str(int(data['main']['temp'])) + "\u00b0"
            (x,y) = 655, positions[i]
            draw.text((x, y), header, color, font=font)

            #humidity
            font = ImageFont.truetype("ClarityCity-Light.ttf", size=100)
            header = str(data["main"]["humidity"])
            (x,y) = 940, positions[i]+1
            draw.text((x, y), header, color, font=font)
            
            i+=1
        else:
            pass
      
    img.save(str(date.today()) + " " + country[5] + " .png")
    img_pdf = img.convert("RGB")
    filePDF = str(date.today()) + " " + country[5] + " .pdf"
    img_pdf.save(filePDF)
    pdf_files.append(filePDF)  #add pdfs names to list

#send all pdfs
sender.send(filenames=pdf_files)
    