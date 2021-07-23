import requests
res = requests.get("http://google.com")
res.raise_for_status()
print("answer_code:", res.status_code) #200정상

if res.status_code == requests.codes.ok:
  print("OKAY")
else:
  print("ALERT [code ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
   f.write(res.text)