import qrcode

def main():

    song = "https://www.youtube.com/watch?v=7A35Lda3e5E&list=RD7A35Lda3e5E&start_radio=1"
    qr = qrcode.QRCode(version = 1,box_size = 5,border = 5)
    qr.add_data(song)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("youtube-qr.png")




if __name__=="__main__":
    main()
