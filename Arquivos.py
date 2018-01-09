import os
import glob
import shutil

folderXML = os.listdir("/home/davint-1/Desktop/Marc/SUN2012/Annotations")

count = 1

# for folders in folderXML:
#     if(folders != '.DS_Store'):
#         if(folders == "misc"):
#             for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/misc/*.xml'):
#                  for line in open(file):
#                     if line.startswith("door "):
#                         nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                         #shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/doorsSUN")
#                         os.remove(nome)
#                         print(count)
#                         count += 1
#                         break
#         else:
#             folder2 = os.listdir("/home/davint-1/Desktop/Marc/SUN2012/Annotations/" + folders)
#             for folder3 in folder2:
#                 count = 1
#                 path = '/home/davint-1/Desktop/Marc/SUN2012/Annotations/'+ str(folders) + '/' +str(folder3) +'/*.xml'
#                 for file in glob.glob(path):
#                     for line in open(file):
#                         if line.startswith("door "):
#                             nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                             #shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/doorsSUN")
#                             os.remove(nome)
#                             print(count)
#                             count += 1
#                             break



verificador = 0

# for folders in folderXML:
#     if(folders != '.DS_Store'):
#         if(folders == "misc"):
#             for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/misc/*.xml'):
#                 for line in open(file):
#                     verificador = 0
#                     for word in line.split():
#                         if word == 'staircase':
#                             nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                             shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/stairsSUN")
#                             print(count)
#                             count += 1
#                             verificador = 1
#                             break
#                     if(verificador == 1):
#                         break
#         else:
#             folder2 = os.listdir("/home/davint-1/Desktop/Marc/SUN2012/Annotations/" + folders)
#             for folder3 in folder2:
#                 path = '/home/davint-1/Desktop/Marc/SUN2012/Annotations/'+ str(folders) + '/' +str(folder3) +'/*.xml'
#                 for file in glob.glob(path):
#                     verificador = 0
#                     for line in open(file):
#                         for word in line.split():
#                             if word == 'staircase':
#                                 nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                                 shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/stairsSUN")
#                                 print(count)
#                                 count += 1
#                                 verificador = 1
#                                 break
#                         if(verificador == 1):
#                             break

# for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/b/bedroom/*.xml'):
#     verificador = 0
#     for line in open(file):
#         for word in line.split():
#             if (word == 'door'):
#                 verificador = 1
#                 break
#         if(verificador == 1):
#             break
#     if(verificador == 0):
#         nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#         shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/indoorSUN")
#         print(nome)
#         print(count)
#         count += 1

# for file in glob.glob('/home/davint-1/Desktop/Marc/SUN2012/Annotations/b/bedroom/*.xml'):
#         for line in open(file):
#             if line.startswith("door "):
#                 nome = file.replace("Annotations", "Images")[:-3] + "jpg"
#                 print(nome)
#                 print(count)
#                 count += 1
#                 #shutil.copy(nome, "/home/davint-1/Desktop/Marc/SUN2012/doorsSUN")
#                 break


diretorio2 = os.listdir('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Annotation_Doors_Half_Open/')
diretorio1 = os.listdir('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Half_Open/')

count = 0
for arquivo in diretorio1:
    verificador = 0
    file1 = arquivo[:-4]
    for arquivo2 in diretorio2:
        file2 = arquivo2[:-4]
        if (file1 == file2):
            verificador = 1

    if(verificador == 0):
        count += 1
        print(file1)
        print(arquivo)
        # os.remove('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Half_Open/' + arquivo)
        shutil.copy('/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_Half_Open/' + arquivo, "/home/davint-1/Desktop/Marc/gvc_dataset-master/dataset_doors/Doors_temp/")
        print(count)


