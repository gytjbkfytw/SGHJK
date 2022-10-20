import cv2
img = cv2.imread("sun-planets.jpg")
cv2.imshow("output",img)

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)

)
cv2.putText(img,"Mercury",(30,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(355,355,255)

)
cv2.putText(img,"Venus",(40,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(555,255,655)

)
cv2.putText(img,"Earth",(50,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)

)
cv2.putText(img,"Mars",(60,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(555,345,655)

)
cv2.putText(img,"Jupitar",(70,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,985,555)

)
cv2.putText(img,"satern",(80,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)

)
cv2.putText(img,"Urenus",(90,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)

)
cv2.putText(img,"Naptune",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)

)
cv2.waitkey(0)