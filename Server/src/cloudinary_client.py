import os

class CloudinaryClient():
    def __init__(self):
        print("init!")

    def upload_image_url(self, img_url):
        upd_url = "curl https://api.cloudinary.com/v1_1/" + os.environ["cloud_name"] + "/image/upload" +  " -X POST --data" + " '" + img_url + "&timestamp=173719931&api_key=" + os.environ["api_key"] + "&signature="+ os.environ["api_secret"] + "'"
        print(upd_url)
        os.system(upd_url)

if __name__ =="__main__":
    c = CloudinaryClient()
    c.upload_image_url("https://res.cloudinary.com/hwhaxlz5c/image/upload/makers/1.png")