import face_recognition
import numpy as np
import cv2


def txt_128_read(filepath, deti):
    data_list = []
    with open(filepath) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        data_split = line.split(deti)
        temp = list(map(float, data_split))
        data_list.append(np.array(temp))
    return data_list


def txt_names_read(filepath):
    data_list = []
    with open(filepath) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        data_list.append(line)
    return data_list


def compare():
    flag = False
    know_face_encodings = []
    know_face_names = []
    src_path = "E:\\ShiJun\\python\\final_work_private\\teamwork\\num_inf"
    names_path = src_path + "\\names.txt"
    encodings_path = src_path + "\\code_128.txt"

    know_face_encodings = txt_128_read(encodings_path, ',')
    know_face_names = txt_names_read(names_path)

    # print(know_face_encodings[0])
    # print(know_face_names)

    capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    face_names = []
    face_suc_names = []
    # process_this_frame = True
    _time = 0
    turn_time = 0
    turn = 0

    while True:
        ret, frame = capture.read()

        # if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # print(face_locations)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=5, model='large')

        face_names = []

        for face_encoding in face_encodings:
            turn_time += 1
            matches = face_recognition.compare_faces(know_face_encodings, face_encoding, tolerance=0.4)
            name = "Unknown"

            face_distances = face_recognition.face_distance(know_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = know_face_names[best_match_index]
                if name not in face_suc_names:
                    face_suc_names.append(name)
                else:
                    _time += 1

            face_names.append(name)

        # process_this_frame = False

        for (top, right, bot, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bot *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bot), (0, 0, 255), 2)
            # if name != 'Unknown':
            #     cv2.rectangle(frame, (left, bot - 35), (right, bot), (0, 0, 255), cv2.FILLED)
            #     font = cv2.FONT_HERSHEY_DUPLEX
            #     cv2.putText(frame, name, (left + 6, bot - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        #保证一段时间内识别成功的帧数至少有一半才认证为识别成功
        if turn_time == 10:
            turn_time = 0
            _time = 0
            turn += 1

        if turn == 4:
            break
        #有十贞对上了就算识别成功
        if _time == 7:
            flag = True
            break

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    capture.release()
    cv2.destroyAllWindows()
    return flag, face_suc_names


if __name__ == '__main__':
    compare()
