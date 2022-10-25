def txt_names_read(filepath):
    data_list = []
    with open(filepath) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        data_list.append(line)
    return data_list

def jud_ctrl(name):
    src_path = "E:\\ShiJun\\python\\final_work_private\\teamwork\\num_inf"
    names_path = src_path + "\\names.txt"
    know_face_names = txt_names_read(names_path)
    flag = False
    _index = know_face_names.index(name)

    return know_face_names