# web scraping 

import requests
import re


url = input("Enter the URL of the webpage: ")


response = requests.get(url)

if response.status_code == 200:
    html = response.text
    
   
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    title = match.group(1).strip() if match else "No title found"
    
    
    with open("title.txt", "w", encoding="utf-8") as file:
        file.write(title)
    
    print("Page title:", title)
    print("Saved to title.txt")
else:
    print("Failed to fetch page:", response.status_code)