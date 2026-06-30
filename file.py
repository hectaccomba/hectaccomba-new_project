import cv2
import moondream as md
from PIL import Image


model = md.vl(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlfaWQiOiJlMDdlODk4Ny03ZDc3LTRkMjAtYTQ1Ny0yNDEzOGNlOTM0NGEiLCJvcmdfaWQiOiJHcElNVW43NWFHNkE0NWliWlVFa1Y4Z2FRaU5NVnczbSIsImlhdCI6MTc4MjczNTU0MCwidmVyIjoxfQ.203BPtn-qsnnLP_e2c0QDG3NsZNSE6OjdGF3Tles3h8")

rtsp_url = "rtsp://192.168.1.108:554/s0"
cap = cv2.VideoCapture(rtsp_url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_frame)

    ans = model.query(pil_image, "Describe the picture in one sentence.")
    print(ans["answer"])

    if cv2.waitKey(5000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
