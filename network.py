import requests

url = "https://www.youtube.com/"
#r = requests.get(url)
# if r.status_code == 200:
#     print("it's work")
# #print(r.status_code)
# if r.ok:
#     print("ok")
# print(r.json())
# with open("index.html", "wb") as f:
#     f.write(r.content)


# download file from internet
# cat = "https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg"
# downloadCat = requests.get(cat)
# with open("cat.jpg", "wb") as F:
#     F.write(downloadCat.content)
# downLoad file  small piaces 
# cat = "https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg"
# downloadCat = requests.get(cat)
# with open("cat.jpg", "wb") as F:
#     for chunk in downloadCat.iter_content(chunk_size=10000):
#         F.write(downloadCat.content)

# requests - in server
# response - from server
# page = requests.get(url)
# if page.status_code == 200:
#     print("Nice it's ", page.encoding)
# else:
#     print("Error:",  page.encoding)

## one from the best practice  get info about site
# page = requests.get(url)
# if page.status_code == 200:
#     print("Nice it's ", page.text)
# else:
#     print("Error:",  page.status_code)


# How to ask google somethings with params
# google = "https://www.google.com"
# page = requests.get(google, params={
#             "q":"dogs",
# })
# if page.status_code == 200:
#     print("nice")
# else:
#     print("somethings wrong")
# print(page.url)

# get info from server with geaders 
# google = "https://www.google.com"
# page = requests.get(google, params={
#             "q":"dogs",
# })
# if page.status_code == 200:
#     print("nice")
# else:
#     print("somethings wrong")
# print(page.headers)


# google = "https://www.google.com"
# page = requests.get(google, params={
#             "q":"dogs",
# })
# if page.status_code == 200:
#     print("nice")
# else:
#     print("somethings wrong")
# print(page.headers ["Server"]) # take key from site with from dict


# jsonSite = "https://jsonplaceholder.typicode.com/posts"
# pageJsone = requests.get(jsonSite)

# if pageJsone.status_code == 200:
#     print("nice this work status is = ", pageJsone.status_code)
# else:
#     print("Error: ", pageJsone.status_code)


# print(pageJsone.text)




# jsonSite = "https://jsonplaceholder.typicode.com/posts"
# pageJsone = requests.post(jsonSite, data={

#                 "userID":"209",
#                 "title":"some info",
#                 "body":"put some thing there"

# })

# if pageJsone.status_code == 200:
#     print("nice this work status is = ", pageJsone.status_code)
# else:
#     print("Error: ", pageJsone.status_code)


# print(pageJsone.text)


# jsonSite = "https://jsonplaceholder.typicode.com/posts"
# pageJsone = requests.post(jsonSite, json={

#                 "userID":"209",
#                 "title":"some info",
#                 "body":"put some thing there"

# })

# if pageJsone.status_code == 200:
#     print("nice this work status is = ", pageJsone.status_code)
# else:
#     print("Error: ", pageJsone.status_code)


# print(pageJsone.text)

# test with reason
# jsonSite = "https://jsonplaceholder.typicode.com/posts"
# pageJsone = requests.get(jsonSite, json={

#                 "userID":"209",
#                 "title":"some info",
#                 "body":"put some thing there"

# })

# if pageJsone.status_code == 200:
#     print("nice this work status is = ", pageJsone.status_code)
# else:
#     print("Error: ", pageJsone.reason)


# print(pageJsone.reason)
# 
# Update info about user with id 1 with method put
# jsonSite = "https://jsonplaceholder.typicode.com/posts/1"
# pageJsone = requests.put(jsonSite, json={

#                 "userID":"209",
#                 "title":"some info",
#                 "body":"put some thing there"

# })

# if pageJsone.status_code == 200:
#     print("nice this work status is = ", pageJsone.status_code)
# else:
#     print("Error: ", pageJsone.reason)


# print(pageJsone.text)

# proxy = {"http": "localhost:8080"}
# x = requests.get("http://www.google.com",proxies=proxy)
# if response.status_code == 200:
#     print("Nice", response.status_code)
# else:
#     print("error")
# print(response.status_code)
# print(x.status_code)
