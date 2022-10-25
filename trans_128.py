import face_recognition
import os

import numpy as np

image_dir = "E:\\ShiJun\\python\\final_work_private\\teamwork\\images"
num_inf_dir = "E:\\ShiJun\\python\\final_work_private\\teamwork\\num_inf"

person_num = 4
img_path = os.listdir(image_dir)
cd = open(num_inf_dir + "\\code_128.txt", 'w+')
f = open(num_inf_dir + "\\names.txt", "w+")
#之后别忘了将指针移到最后，连续写入

# for idx in range(len(image_dir)):
for idx in range(person_num):
    img_name = img_path[idx]
    img_item_path = os.path.join(image_dir, img_name)
    # print(img_item_path)
    img = face_recognition.load_image_file(img_item_path)
    code_128 = face_recognition.face_encodings(img, num_jitters=5, model='large')
    # print(code_128[0])
    np.savetxt(cd, code_128, newline=' ', delimiter=',')
    cd.write("\n")
    f.write(img_name.split('.')[0])
    f.write("\n")
cd.close()
f.close()