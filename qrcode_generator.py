import qrcode

data = "https://sub.bfgnet.vip/link/mhJqh4WiLbNkICpZ?sub=6&extend=1"

img = qrcode.make(data)
img.show()

