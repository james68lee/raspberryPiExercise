import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plotPose3D(lmList):
    face_index_list = [8, 6, 5, 4, 0, 1, 2, 3, 7]
    mouth_index_list = [9, 10]
    right_arm_index_list = [11, 13, 15, 17, 19, 15, 21]
    left_arm_index_list = [12, 14, 16, 18, 20, 16, 22]
    right_body_side_index_list = [11, 23, 25, 27, 29, 31, 27]
    left_body_side_index_list = [12, 24, 26, 28, 30, 32, 28]
    shoulder_index_list = [11, 12]
    waist_index_list = [23, 24]

    # 眼耳鼻 - 臉部
    face_x, face_y, face_z = [], [], []
    for index in face_index_list:
        point = lmList[index]
        face_x.append(point[0])
        face_y.append(point[1])
        face_z.append(point[2])
    
    # 嘴巴   
    mouth_x, mouth_y, mouth_z = [], [], []
    for index in mouth_index_list:
        point = lmList[index]
        mouth_x.append(point[0])
        mouth_y.append(point[1])
        mouth_z.append(point[2])
    
    # 右手
    right_arm_x, right_arm_y, right_arm_z = [], [], []
    for index in right_arm_index_list:
        point = lmList[index]
        right_arm_x.append(point[0])
        right_arm_y.append(point[1])
        right_arm_z.append(point[2])

    # 左手
    left_arm_x, left_arm_y, left_arm_z = [], [], []
    for index in left_arm_index_list:
        point = lmList[index]
        left_arm_x.append(point[0])
        left_arm_y.append(point[1])
        left_arm_z.append(point[2])

    # 右半身
    right_body_side_x, right_body_side_y, right_body_side_z = [], [], []
    for index in right_body_side_index_list:
        point = lmList[index]
        right_body_side_x.append(point[0])
        right_body_side_y.append(point[1])
        right_body_side_z.append(point[2])

    # 左半身
    left_body_side_x, left_body_side_y, left_body_side_z = [], [], []
    for index in left_body_side_index_list:
        point = lmList[index]
        left_body_side_x.append(point[0])
        left_body_side_y.append(point[1])
        left_body_side_z.append(point[2])

    # 肩
    shoulder_x, shoulder_y, shoulder_z = [], [], []
    for index in shoulder_index_list:
        point = lmList[index]
        shoulder_x.append(point[0])
        shoulder_y.append(point[1])
        shoulder_z.append(point[2])

    # 腰
    waist_x, waist_y, waist_z = [], [], []
    for index in waist_index_list:
        point = lmList[index]
        waist_x.append(point[0])
        waist_y.append(point[1])
        waist_z.append(point[2])
            
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter(face_x, face_y, face_z)
    ax.plot(mouth_x, mouth_y, mouth_z)
    ax.plot(right_arm_x, right_arm_y, right_arm_z)
    ax.plot(left_arm_x, left_arm_y, left_arm_z)
    ax.plot(right_body_side_x, right_body_side_y, right_body_side_z)
    ax.plot(left_body_side_x, left_body_side_y, left_body_side_z)
    ax.plot(shoulder_x, shoulder_y, shoulder_z)
    ax.plot(waist_x, waist_y, waist_z)

    ax.view_init(elev=300, azim=330, roll=300)   # 指定視角
    ax.set_box_aspect([1, 1, 1])                 # 指定x, y, z的比例
    # plt.savefig("pose_landmark.png") 
    plt.show()


