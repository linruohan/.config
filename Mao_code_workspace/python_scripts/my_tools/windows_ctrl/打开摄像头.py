import cv2
from VideoCapture import Device


def screenshots(filename):
    cam = Device()
    cam.saveSnapshot(filename)


def cv2capture():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        c = cv2.waitKey(1)
        if c == 27:  # 按 ESC 键退出
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cv2capture()
    screenshots("001.jpg")
