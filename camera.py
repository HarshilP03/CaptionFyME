import cv2 

def gen_frame():
    camera = cv2.VideoCapture(0)
    path = None
    while True:
        success,frame = camera.read()
        if not success:
            break

        else:
            path = "./static/clickImg.jpg"
            cv2.imwrite(path,frame)
            break
            # ret, buffer = cv2.imencode('.jpg',frame)
            # frame = buffer.tobytes()
            # return (b'--frame\r\n'
            #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return path
