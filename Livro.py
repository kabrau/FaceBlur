import os, cv2, shutil
#Faz a varredura do diretório imagens buscando arquivos JPG, JPEG e PNG.

diretorio = '/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Stairs'
arquivos = os.listdir(diretorio)
diretorio2 = '/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_stairs/Stairs'
arquivos2 = os.listdir(diretorio2)
diretorio3 = '../pedestrian_signal/uploaded'
arquivos3 = os.listdir(diretorio3)

count = 0

# for a in arquivos:
#     if a.lower().endswith('.jpg') or a.lower().endswith('.png') or a.lower().endswith('.jpeg'):
#         for b in arquivos2:
#             if b.lower().endswith('.jpg') or b.lower().endswith('.png') or b.lower().endswith('.jpeg'):
#                 if (a == b):
#                     os.remove('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_stairs/Stairs/' + a)
#                     count += 1
#                     print(count)
    #     for c in arquivos3:
    #         if c.lower().endswith('.jpg') or c.lower().endswith('.png') or c.lower().endswith('.jpeg'):
    #             if (a == c):
    #                 os.remove('../Blur/Pedestrian_Signal/images/' + a)
    #                 count += 1
    #                 print(count)
    # else:
    #     shutil.copy('../Blur/Pedestrian_Signal/images/' + a, '../pedestrian_signal/txt/' + a )
    #     os.remove('../Blur/Pedestrian_Signal/images/'  + a)


# for a in arquivos:
#     count += 1
#     print(count)
# count2 = 0
# for a in arquivos:
#     if a.lower().endswith('.jpg') or a.lower().endswith('.png') or a.lower().endswith('.jpeg'):
#         count += 1
#         print(count)
#     else:
#          count2 += 1
#          print(".txt = {}".format(count2))

        # imgC = cv2.imread(diretorio + '/' + a)
        # imgPB = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)
        # df = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        # faces = df.detectMultiScale(imgPB, scaleFactor = 1.2, minNeighbors = 7, minSize = (30,30), flags =
        #                     cv2.CASCADE_SCALE_IMAGE)
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(imgC, (x, y), (x + w, y + h), (0, 255, 255), 7)
        #     alt = int(imgC.shape[0]/imgC.shape[1]*640)
        #     imgC = cv2.resize(imgC, (640, alt), interpolation = cv2.INTER_CUBIC)
        #     cv2.imshow(str(len(faces))+' face(s) encontrada(s).', imgC)
        #     cv2.waitKey(0)


####### DELETA ARQUIVOS REPETIDOS ########

dir = '/home/davint-1/Desktop/Marc/pedestrian_ANN/testImages'
arq = os.listdir(dir)
dir2 = '/home/davint-1/Desktop/Marc/pedestrian_ultimo/no_blur_01'
arq2 = os.listdir(dir2)


for file in arq2:
    for file2 in arq:
        if(file == file2):
            print(file)
            count += 1
            print(count)
            #os.remove(dir + '/' + file2)

####### DELETA ARQUIVOS .TXT #######

# for file in arq:
#     if(file.endswith('.txt')):
#         print(file)
#         count += 1
#         print(count)
#         os.remove(dir + '/' + file)
