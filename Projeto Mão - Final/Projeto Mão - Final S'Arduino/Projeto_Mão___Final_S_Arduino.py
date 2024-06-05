# -*- coding: utf-8 -*-
from pickle import TRUE
import cv2
import mediapipe as mp
import time

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 960)    # Largura da camera
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)   # Altura da camera

mpDraw = mp.solutions.drawing_utils
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
gesto_detectado = None
gesto_final = None
tempo_inicial = None
contador_ok = None
tempo_limite = 5

while True:
    check,img = video.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    resultados = Hand.process(imgRGB)
    handsPoints = resultados.multi_hand_landmarks
    h,w,_ = img.shape
    pontos = []

    ###############################################################

    if handsPoints:
        
        for points in handsPoints:
            
            # Marcação do centro da da imagem para reconhecer a mão esquerda ou direita
            palma_x = points.landmark[mp.solutions.hands.HandLandmark.WRIST].x * img.shape[1]
            centro_img = img.shape[1] // 2            
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            
            for id,cord in enumerate(points.landmark):

                # Marcação dos pontos na mão
                cx,cy = int(cord.x*w), int(cord.y*h)
                cv2.putText(img,str(id),(cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
                pontos.append((cx,cy))
                
        ###############################################################

        contador = 0
        Dedao = 0
        Indicador = 0
        Medio = 0
        Anelar = 0
        Minimo = 0
        

        # Logica para reconhecer a mão direita ou esquerda
        if palma_x > centro_img:
            
            lado_direito = True
            
        else:
            
            lado_direito = False
            
        ###############################################################    
        
        #Logica para reconhecer se a mão está virada
        mao_virada = False

        if pontos[4][0] > pontos[20][0]:
            
            mao_virada = True
            
        ###############################################################
        
        # Logica para reconhecer qual dedo está levantado
        if lado_direito:
            
            if mao_virada:

                if points:
            
                    if pontos[4][0] > pontos[3][0] or pontos[4][0] == pontos[3][0]:
                
                        Dedao += 1
                        contador += 1
                
                    if pontos[8][1] < pontos[6][1] or pontos[8][1] == pontos[6][1]:
                
                        Indicador += 1
                        contador += 1
                    
                    if pontos[12][1] < pontos[10][1] or pontos[12][1] == pontos[10][1]:
                
                        Medio += 1
                        contador += 1
                
                    if pontos[16][1] < pontos[14][1] or pontos[16][1] == pontos[14][1]:
                
                        Anelar += 1
                        contador += 1
                
                    if pontos[20][1] < pontos[18][1] or pontos[20][1] == pontos[18][1]:
                
                        Minimo += 1
                        contador += 1
             
            else:
                
                if points:
            
                    if pontos[4][0] < pontos[3][0] or pontos[4][0] == pontos[3][0]:
                
                        Dedao += 1
                        contador += 1
                
                    if pontos[8][1] < pontos[6][1] or pontos[8][1] == pontos[6][1]:
                
                        Indicador += 1
                        contador += 1
                    
                    if pontos[12][1] < pontos[10][1] or pontos[12][1] == pontos[10][1]:
                
                        Medio += 1
                        contador += 1
                
                    if pontos[16][1] < pontos[14][1] or pontos[16][1] == pontos[14][1]:
                
                        Anelar += 1
                        contador += 1
                
                    if pontos[20][1] < pontos[18][1] or pontos[20][1] == pontos[18][1]:
                
                        Minimo += 1
                        contador += 1

        else:
            
            if mao_virada:

                if points:
            
                    if pontos[4][0] > pontos[3][0] or pontos[4][0] == pontos[3][0]:
                
                        Dedao += 1
                        contador += 1
                
                    if pontos[8][1] < pontos[7][1] or pontos[8][1] == pontos[7][1]:
                
                        Indicador += 1
                        contador += 1
                    
                    if pontos[12][1] < pontos[11][1] or pontos[12][1] == pontos[11][1]:
                
                        Medio += 1
                        contador += 1
                
                    if pontos[16][1] < pontos[15][1] or pontos[16][1] == pontos[15][1]:
                
                        Anelar += 1
                        contador += 1
                
                    if pontos[20][1] < pontos[19][1] or pontos[20][1] == pontos[19][1]:
                
                        Minimo += 1
                        contador += 1
             
            else:
                
                if points:
            
                    if pontos[4][0] < pontos[3][0] or pontos[4][0] == pontos[3][0]:
                
                        Dedao += 1
                        contador += 1
                
                    if pontos[8][1] < pontos[7][1] or pontos[8][1] == pontos[7][1]:
                
                        Indicador += 1
                        contador += 1
                    
                    if pontos[12][1] < pontos[11][1] or pontos[12][1] == pontos[11][1]:
                
                        Medio += 1
                        contador += 1
                
                    if pontos[16][1] < pontos[15][1] or pontos[16][1] == pontos[15][1]:
                
                        Anelar += 1
                        contador += 1
                
                    if pontos[20][1] < pontos[19][1] or pontos[20][1] == pontos[19][1]:
                
                        Minimo += 1
                        contador += 1
                    
        ###############################################################
        
        # Enumerando sinais e reconhecendo gestos
        if contador == 5: 
            
            texto = "Mao Aberta"
            gesto_detectado = 1
             
        elif contador == 4:
            
            if Dedao == 0 and Indicador > 0 and Medio > 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Dedao abaixado"
                cv2.putText(img,str("Dedao abaixado"),(100,100), cv2.FONT_HERSHEY_SIMPLEX,1,(128,0,128),1)
                gesto_detectado = 2
                
            elif Dedao > 0 and Indicador == 0 and Medio > 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Indicador abaixado"
                gesto_detectado = 3
                
            elif Dedao > 0 and Indicador > 0 and Medio == 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Medio abaixado"
                gesto_detectado = 4
                
            elif Dedao > 0 and Indicador > 0 and Medio > 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Anelar Abaixado"
                gesto_detectado = 5
                
            elif Dedao > 0 and Indicador > 0 and Medio > 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Minimo Abaixado"
                gesto_detectado = 6
                
        elif contador == 3:
            
            if Dedao == 0 and Indicador == 0 and Medio > 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Tres - Medio/Anelar/Minimo"
                gesto_detectado = 7
                
            elif Dedao == 0 and Indicador > 0 and Medio > 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Tres - Indicador/Medio/Anelar"
                gesto_detectado = 8

            elif Dedao == 0 and Indicador > 0 and Medio > 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Tres - Indicador/Medio/Minimo"
                gesto_detectado = 9
                
            elif Dedao == 0 and Indicador > 0 and Medio == 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Tres - Indicador/Anelar/Minimo"
                gesto_detectado = 10
                
            elif Dedao > 0 and Indicador == 0 and Medio == 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Tres - Dedao/Anelar/Minimo"
                gesto_detectado = 11
                
            elif Dedao > 0 and Indicador == 0 and Medio > 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Tres - Dedao/Medio/Minimo"
                gesto_detectado = 12
                
            elif Dedao > 0 and Indicador == 0 and Medio > 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Tres - Dedao/Medio/Anelar"
                gesto_detectado = 13

            elif Dedao > 0 and Indicador > 0 and Medio == 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Tres - Dedao/Indicador/Minimo"
                gesto_detectado = 14
                
            elif Dedao > 0 and Indicador > 0 and Medio == 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Tres - Dedao/Indicador/Anelar"
                gesto_detectado = 15
                
            elif Dedao > 0 and Indicador > 0 and Medio > 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Tres - Dedao/Indicador/Medio"
                gesto_detectado = 16
                
        elif contador == 2:
            
            if Dedao == 0 and Indicador == 0 and Medio == 0 and Anelar > 0 and Minimo > 0:
                
                texto = "Dois - Anelar/Minimo"
                gesto_detectado = 17
                
            if Dedao == 0 and Indicador > 0 and Medio > 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Dois - Indicador/Medio"
                gesto_detectado = 18
                
            elif Dedao == 0 and Indicador == 0 and Medio > 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Dois - Medio/Minimo"
                gesto_detectado = 19
                
            elif Dedao == 0 and Indicador == 0 and Medio > 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Dois - Medio/Anelar"
                gesto_detectado = 20
                
            elif Dedao == 0 and Indicador > 0 and Medio == 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Dois - Indicador/Minimo"
                gesto_detectado = 21
                
            elif Dedao > 0 and Indicador == 0 and Medio == 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Dois - Dedao/Minimo"
                gesto_detectado = 22
                
            elif Dedao > 0 and Indicador == 0 and Medio > 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Dois - Dedao/Medio"
                gesto_detectado = 23
                
            elif Dedao > 0 and Indicador == 0 and Medio == 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Dois - Dedao/Anelar"
                gesto_detectado = 24
                
            elif Dedao > 0 and Indicador > 0 and Medio == 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Dois - Dedao/Indicador"
                gesto_detectado = 25
                
        elif contador == 1:
            
            if Dedao > 0 and Indicador == 0 and Medio == 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Dedao Levantado"
                gesto_detectado = 26
                
            elif Dedao == 0 and Indicador > 0 and Medio == 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Indicador Levantado"
                gesto_detectado = 27
                
            elif Dedao == 0 and Indicador == 0 and Medio > 0 and Anelar == 0 and Minimo == 0:
                
                texto = "Medio Levantado"
                gesto_detectado = 28
                
            elif Dedao == 0 and Indicador == 0 and Medio == 0 and Anelar > 0 and Minimo == 0:
                
                texto = "Anelar Levantado"
                gesto_detectado = 29
                
            elif Dedao == 0 and Indicador == 0 and Medio == 0 and Anelar == 0 and Minimo > 0:
                
                texto = "Minimo Levantado"
                gesto_detectado = 30
                
        elif contador == 0:
            
            texto = "Mao fechada"
            gesto_detectado = 31
            
    else:
        
        texto = "Mao nao detectada"
        contador = 0
        gesto_final = None
    
    cv2.putText(img,texto,(100,100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
    
    ###############################################################    

    cv2.imshow("Imagem",img)
    
    fechar = cv2.waitKey(10)
    if fechar == 27:  # ESC
        break
