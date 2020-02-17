import  numpy as np
import cv2
camara=cv2.VideoCapture(0)

kernel1=np.array([[-1,0,1],[0,0,0],[-1,0,1]])
while True:
    #leer las imagenes de la camara
    estado,frame=camara.read()
    #convertir la imagen BGR a grises
    Ig=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #------------ECUALIZACION DEL HISTOGRAMA (RESALTAR EL CONTRASTE)
    Icon=cv2.equalizeHist(Ig)
    #aplicar un filtro para eliminar el ruido
    Isinr=cv2.GaussianBlur(Icon,(3,3),3)
    #-----realizar la convolucion 2D de la imagen y el kernel
    img2=cv2.filter2D(Icon,-1,kernel=kernel1)
                      #convertir la imagen a un binario
    imgb=np.where(img2>=30,255,0)
    imgb=np.uint8(imgb)
    #--------------------------
    cv2.imshow("imagen original grises" , Ig)
    cv2.imshow("imagen equializada grises", Icon)
    cv2.imshow("imagen convolucion y binaria", imgb)
    #--- ESPERAR A PRESIONAR LA TECLA q  PARA CERRAR LA APLICACION
    if cv2.waitKey(1)==ord("q"):
        camara.release()
        cv2.destroyAllWindows()
        break
