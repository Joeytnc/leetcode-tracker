import requests

username = "jf11kcode"

url = f"https://alfa-leetcode-api.onrender.com/{username}/solved"

response = requests.get(url)

print("Status:", response.status_code)
print(response.text)

