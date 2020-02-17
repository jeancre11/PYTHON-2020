import numpy as np
import cv2
#crear un objeto
camara=cv2.VideoCapture(0)
while True:
    #leer las imagenes que captura la camara
    ret,img=camara.read()
    #convertir a escala grises
    gris=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    gris2=cv2.equalizeHist(gris)
    #segmentacion
    umbral=120
    segementando=np.where(gris>=umbral, 255,0)
    segementando=np.uint8(segementando)
    #mostrar la imagen mediante la funcion imshow
    #cv2.imshow("mi imagen gris 1", img)
    cv2.imshow("imagen segmentada 1", gris)
    cv2.imshow("imagen segmentada 2", gris2)
    #cuando se presiona la tecla q para cerrar toda la aplicacion
    if cv2.waitKey(1)==ord("q"):
        camara.release()
        cv2.destroyAllWindows()
