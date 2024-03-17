# -*- coding:utf-8 -*-
import datetime
import os
import uuid

import cv2
import dlib
import face_recognition
from PIL import Image, ImageDraw


class Face:
    def __init__(self, directory_path, picture_name, save_path):
        self.dir_path = directory_path  # 图片目录
        self.pic_name = picture_name  # 图片名称
        self.save_path = save_path  # 图片路径

    # 图片加载和初始化
    def image_init(self):
        image = face_recognition.load_image_file(
            os.path.join(
                self.dir_path,
                self.pic_name
            )
        )
        return image

    def get_face_locations(self):
        # 初始化
        image = self.image_init()

        # 查找人类位置 ,位置算法基于轮廓
        face_locations = face_recognition.face_locations(image)
        return image, face_locations

    # 获取图像人脸特征
    def get_face_landmarks(self):
        # 初始化
        image = self.image_init()
        # 通过特征算法获得特征点
        face_landmarks_list = face_recognition.face_landmarks(image)
        return face_landmarks_list, image

    @property
    def dt(self):
        return datetime.datetime.now().strftime("%Y%m%d%H%M")

    # 保存名称定义
    @property
    def image_name(self):
        prefix1 = self.dt
        prefix2 = uuid.uuid4().hex
        return prefix1 + prefix2

    # 保存识别结果
    def save_pil_face(self, pil_image):
        if not os.path.exists(self.save_path):  # 如果路径不存在
            os.makedirs(self.save_path)
        # 定义图片完整名称
        filename = "{}.png".format(
            self.image_name
        )
        # 保存图片至指定位置
        pil_image.save(os.path.join(self.save_path, filename), 'png')
        return filename

    # 1.框选人脸的功能
    def face_box(self):
        # 获取人脸的位置
        image, face_locations = self.get_face_locations()
        # 将图片转化为图像数组
        pil_image = Image.fromarray(image)
        # 图像数组转化为可绘制的对象
        draw = ImageDraw.Draw(pil_image)
        # 循环遍历人脸
        for (top, right, bottom, left) in face_locations:
            draw.rectangle(
                (
                    (left, top),
                    (right, bottom)
                ),
                outline=(0, 255, 0),
                width=5
            )

        # pil_image.show()
        # 保存图像
        filename = self.save_pil_face(pil_image)
        return [filename]

    # 2.人脸勾勒
    def face_sence(self):
        # 获取图像和人脸特征
        fece_landmarks_list, image = self.get_face_landmarks()
        # 定义获取脸部特征列表
        facial_features = [
            "chin",
            "left_eyebrow",
            "right_eyebrow",
            "nose_bridge",
            "left_eye",
            "right_eye",
            "top_lip",
            "bottom_lip"

        ]
        # 将图像转化为数组
        pil_image = Image.fromarray(image)
        # 将图像转化为可绘制对象
        draw = ImageDraw.Draw(pil_image)
        # 遍历所有特征点
        for face_landmark in fece_landmarks_list:
            # 遍历特征列表
            for facial_feature in facial_features:
                # 绘制描线
                draw.line(face_landmark[facial_feature], width=5, fill=(255, 255, 255))
        # 显示图像

        # pil_image.show()
        # 保存图像
        filename = self.save_pil_face(pil_image)
        return [filename]

    # 3.人脸截取
    def face_find(self):
        # 获取图像和人脸位置
        image, face_locations = self.get_face_locations()
        result = []
        for face_location in face_locations:
            top, right, bottom, left = face_location
            # 框选图片中所有人
            face_image = image[top:bottom, left:right]
            # 框选结果化数组
            pil_image = Image.fromarray(face_image)
            filename = self.save_pil_face(pil_image)
            result.append(
                filename
            )
        return result

    # 4.人脸化妆
    def face_makeup(self):
        # 获取图像和人脸位置
        face_landmarks_list, image = self.get_face_landmarks()
        # 将图像转化为图像数组
        pil_image = Image.fromarray(image)
        # 将图像数组转化为可绘制的对象
        draw = ImageDraw.Draw(pil_image, 'RGBA')  # A是透明度
        # 循环遍历人脸
        for face_landmark in face_landmarks_list:
            # 绘制左右眉毛
            draw.polygon(face_landmark['left_eyebrow'], fill=(68, 0, 0, 128))
            draw.polygon(face_landmark['right_eyebrow'], fill=(68, 0, 0, 128))
            draw.line(face_landmark['left_eyebrow'], fill=(68, 0, 0, 150), width=3)
            draw.line(face_landmark['right_eyebrow'], fill=(68, 0, 0, 150), width=3)
            # 绘制上下嘴唇
            draw.polygon(face_landmark['top_lip'], fill=(150, 0, 0, 128))
            draw.polygon(face_landmark['bottom_lip'], fill=(150, 0, 0, 128))
            # 绘制左右眼睛
            draw.polygon(face_landmark['left_eye'], fill=(255, 255, 255, 30))
            draw.polygon(face_landmark['right_eye'], fill=(255, 255, 255, 30))
            draw.line(face_landmark['left_eye'] + [face_landmark['right_eye'][0]], fill=(0, 0, 0, 110), width=2)
            draw.line(face_landmark['right_eye'] + [face_landmark['right_eye'][0]], fill=(0, 0, 0, 110), width=2)
        # 保存图片
        filename = self.save_pil_face(pil_image)
        return [filename]
        # pil_image.show()

    # 5.人脸68个特征点获取
    def face_68_point(self):
        image = cv2.imread(os.path.join(self.dir_path, self.pic_name))
        # 使用特征提取器
        detector = dlib.get_frontal_face_detector()
        model_path = os.path.join(
            os.path.dirname
            (os.path.dirname(__file__)
             ),
            'static/models/shape_predictor_68_face_landmarks.dat'
        )
        # 定义预测器
        predictor = dlib.shape_predictor(model_path)
        dets = detector(image, 1)
        for k, d in enumerate(dets):
            # 利用预测器预测
            shape = predictor(image, d)
            # 标出68个点
            for i in range(68):
                cv2.circle(image,
                           (shape.part(i).x, shape.part(i).y), 3, (255, 0, 0),-1  # 这里是BGR
                           )  # 获取圆心
                cv2.putText(image,
                            str(i),
                            (shape.part(i).x,shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0),
                            )
        # cv2.imshow('68.png',image)
        # cv2.waitKey(0)
        #保存图片到指定位置
        filename = self.save_cv2_face(image)
        return [filename]

    # 使用opencv保存图片
    def save_cv2_face(self, image):
        if not os.path.exists(self.save_path):  # 如果路径不存在
            os.makedirs(self.save_path)
        # 定义图片完整名称
        filename = "{}.png".format(
            self.image_name
        )
        # 保存图片至指定位置
        cv2.imwrite(os.path.join(self.save_path, filename), image)
        return filename


if __name__ == "__main__":
    root_path = os.path.dirname(
        os.path.dirname(__file__)
    )
    face = Face(
        directory_path=os.path.join(root_path, 'static\images\exp'),
        picture_name="g.png",
        save_path=os.path.join(root_path, 'static/uploads')
    )
    # print(face.get_face_locations())
    # print(face.get_face_landmarks())
    print(face.face_68_point())
