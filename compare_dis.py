from operator import mod
import numpy as np
import face_recognition
import requests
import cv2


def face_id_encoding(face_id: np.ndarray) -> str:
    return ",".join(map(str, face_id.tolist()))


def compare_dis():
    global capture
    capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    face_locations = []
    face_encodings = []
    # process_this_frame = True
    turn_time = 0
    first = True

    while True:
        ret, frame = capture.read()
        if first:
            cv2.imshow('Video', frame)
            first = False
            continue
        # if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        print(face_locations)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=5, model='large')

        if not len(face_encodings) == 0:
            face_encoding_str = face_id_encoding(face_encodings[0])

            _response = requests.get(
                url='http://43.142.162.144:5000/checkFace',
                params={'face_id': face_encoding_str},
            )
        # process_this_frame = False
            if not _response.text == 'Unknown':
                cv2.destroyAllWindows()
                return True, _response.text, capture
            else:
                turn_time += 1

            for (top, right, bot, left) in face_locations:
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

        # 保证一段时间内识别成功的帧数至少有一半才认证为识别成功
        if turn_time == 100:
            break

        # if turn == 4:
        #     break
        # # 有十贞对上了就算识别成功
        # if _time == 7:
        #     break

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    cv2.destroyAllWindows()
    return False, '',capture
