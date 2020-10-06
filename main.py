print("Welcome, please select input:\n1.Qrcode generater\n2.Qr code reader\n")
n=int(input())
if(n==1):
  def qr_generater():
    import qrcode
    qr=qrcode.QRCode(
      version=2,
      box_size=10,
      border=5

      )

    data="https://www.youtube.com/results?search_query=talkwithrd" #Enter your date here.
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save("yt.png")
  qr_generater()
if(n==2):
   def qr_reader():
     import cv2
      # read the QRCODE image
     img = cv2.imread("yt.png")
     detector = cv2.QRCodeDetector()
     data, bbox, straight_qrcode = detector.detectAndDecode(img)
      # if there is a QR code
     if bbox is not None:
        print(f"QRCode data:\n{data}")
          # display the image with lines
          # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
              # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
          # display the result
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
   qr_reader()

   #This code is contributed by Rishabh Dwivedi.