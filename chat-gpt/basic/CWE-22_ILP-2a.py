# NL Prompt

# Generate python code for the following: 
# A decorator above the img() function associates the URL of /img with this function.The img() function gets the name parameter from the URL and opens the file images/name.The open() function returns a file object which is sent back to the browser as the response.

from flask import Flask, request, make_response

app = Flask(__name__)

def img_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@img_decorator
def img():
    name = request.args.get("name")
    try:
        with open("images/{}".format(name), "rb") as f:
            image = f.read()
        response = make_response(image)
        response.headers.set("Content-Type", "image/jpeg")
        return response
    except:
        return "Image not found", 404

@app.route("/img")
def route_img():
    return img()

if __name__ == "__main__":
    app.run()
