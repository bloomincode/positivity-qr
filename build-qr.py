import qrcode

img = qrcode.make("https://media.giphy.com/media/dJGYFScvBjfRabiH7m/giphy.gif")
img.save("./positivity.jpg")