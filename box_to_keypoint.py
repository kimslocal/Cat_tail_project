from ast import Str
import json
import os
import cv2 as cv
import matplotlib.pyplot as plt



def converter(file_labels:str, file_image:str):
    keypoints = []
    img = cv.imread(file_image)
    img_w, img_h = img.shape[1], img.shape[0]

    with open(file_labels) as f:
        lines_txt = f.readlines()
        lines = []
        for line in lines_txt:
            lines.append([int(line.split()[0])] + [round(float(coord), 5) for coord in line.split()[1:]])

    for line in lines:
        if line[0] == 0:
            x_c = round(line[1] * img_w)
            y_c = round(line[2] * img_h)
            w = round(line[3] * img_w)
            h = round(line[4] * img_h)
            
            bboxes = ([round(x_c - w/2), round(y_c - h/2), round(x_c + w/2), round(y_c + h/2)])
        
        else:
            kp_id = line[0]
            x_c = round(line[1] * img_w)
            y_c = round(line[2] * img_h)
            keypoints.append([x_c, y_c, kp_id, 1]) # 기본으로 visibility는 1로 체크

    keypoints = sorted(keypoints, key=lambda x: x[2]) # keypoint id기준으로 상향정렬

    return bboxes, keypoints


def visualize(image, keypoints, bboxes):
        top_left_corner, bottom_right_corner = tuple([bboxes[0], bboxes[1]]), tuple([bboxes[2], bboxes[3]])
        img = cv.imread(image)
        img = cv.rectangle(image, top_left_corner, bottom_right_corner, (0, 255, 0), 3)
    
        for kp_idx, kp in enumerate(keypoints):
            center = tuple([kp[0], kp[1]])
            img = cv.circle(img, center, 5, (255,0,0), 5)
            img = cv.putText(img, " " + label_dict[kp[2]], center, cv.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 4)
        
        cv.imshow(img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        # plt.figure(figsize=(15, 15))
        # plt.imshow(img)


def check_missing(file_image, bboxes, keypoints):
    global label_dict
    top_left_corner, bottom_right_corner = tuple([bboxes[0], bboxes[1]]), tuple([bboxes[2], bboxes[3]])
    img = cv.imread(file_image)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.rectangle(img, top_left_corner, bottom_right_corner, (0, 255, 0), 3)
    
    for kp_idx, kp in enumerate(keypoints):
        center = tuple([kp[0], kp[1]])
        img = cv.circle(img, center, 5, (255,0,0), 5)
        img = cv.putText(img, " " + label_dict[kp[2]], center, cv.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 4)
    
    current = 1
    while current <= len(keypoints):
        cv.imshow(img)
        cv.waitKey(0)
        visibility = input(f"{label_dict[current]}이 사진에서 보이지 않으면 0 입력, 아니면 아무 글자나 입력")
        if visibility == 0:
            keypoints[1][-1] = 0

        else:
            continue

    else:
        cv.destroyAllWindows()



def dump_to_json():
    pass 


def main(IMAGES, LABELS, ANNOTATIONS):
    label_names = ['cat', 'left_ear', 'left_front_leg_bottom', 'left_front_leg_upper', 'left_hind_leg_bottom', 'left_hind_leg_upper', 'neck', 'nose', 'right_ear', 'right_front_leg_bottom', 'right_front_leg_upper', 'right_hind_leg_bottom', 'right_hind_leg_upper', 'spine', 'spine_middle', 'stomach', 'tail_0', 'tail_1', 'tail_2', 'tail_3', 'tail_4', 'tail_5']
    label_dict = {i: label_names[i] for i in range(1, len(label_names))}
    # IMAGES = './data/train/images/'
    # LABELS = './data/train/labels/'
    # ANNOTATIONS = './path/to/dataset/train/annotations/'

    files_names = [file.split('.jpg')[0] for file in os.listdir(IMAGES)]
    
    
    for file in files_names:
        print(file)
        file_labels = os.path.join(LABELS, file + ".txt")
        file_image = os.path.join(IMAGES, file + ".jpg")
        bboxes, keypoints = converter(file_labels, file_image)
        keypoints =  check_missing(file_image, bboxes, keypoints)
        dump_to_json(bboxes, keypoints, os.path.join(ANNOTATIONS, file + '.json')) 
        

# if __name__ == 'box_to_keypoint.py':
main('./data/train/images/', './data/train/labels/', './path/to/dataset/train/annotations/')