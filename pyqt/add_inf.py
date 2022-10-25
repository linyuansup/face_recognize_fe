import os.path

import cv2
import face_recognition
import numpy as np
import requests

def face_id_encoding(face_id: np.ndarray) -> str:
    return ",".join(map(str, face_id.tolist()))

def add_inf(n, c):
    image_dir = os.path.join(os.path.dirname(__file__) + '\\images\\')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # name = input("请输入姓名：")
    # is_ctrl = input("是否为管理员：")
    name = n
    is_ctrl = c
    image_name_path = os.path.join(image_dir + name)
    image_name_path += '.jpg'
    # 照相
    capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    capture.set(6, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    flag = capture.isOpened()

    while (flag):
        ret, frame = capture.read()
        cv2.imshow("get photo", frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            # cv2.imwrite(image_name_path, frame, )
            cv2.imencode('.jpg', frame)[1].tofile(image_name_path)
            print("照片已成功保存！")
            print('-------------------')
        elif k == ord('q'):
            break
    cv2.destroyAllWindows()

    # 转换信息
    # num_inf_dir = "E:\\ShiJun\\python\\final_work_private\\teamwork\\num_inf"

    # cd = open(num_inf_dir + "\\code_128.txt", 'a+')
    # f = open(num_inf_dir + "\\names.txt", "a+")

    face_image = face_recognition.load_image_file(image_name_path)
    face_encodings = face_recognition.face_encodings(face_image, model='large', num_jitters=5)
    face_encoding = face_encodings[0]
    face_encoding_str = face_id_encoding(face_encoding)
    _response = requests.get(
        url='http://43.142.162.144:5000/addUser',
        params={"name":name, "face_id":face_encoding_str, 'isAdmin':c},
    )

    os.remove(image_name_path)


    # np.savetxt(cd, face_encoding, newline=' ', delimiter=',')
    # cd.write("\n")
    # f.write(name)
    # f.write("\n")
    #
    # cd.close()
    # f.close()

    print("信息录入成功！")
    return capture

if __name__ == '__main__':
    add_inf()