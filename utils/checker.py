import cv2

from utils.mark_detector import MarkDetector
from utils.pose_estimator import PoseEstimator


def image_main(image, width, height):
    pose_estimator = PoseEstimator(img_size=(width, height))
    mark_detector = MarkDetector()
    tm = cv2.TickMeter()

    facebox = mark_detector.extract_cnn_facebox(image)

    if facebox is not None:
        x1, y1, x2, y2 = facebox
        face = image[y1:y2, x1:x2]

        tm.start()
        marks = mark_detector.detect_marks(face)
        tm.stop()

        marks *= x2 - x1
        marks[:, 0] += x1
        marks[:, 1] += y1

        pose = pose_estimator.solve_pose_by_68_points(marks)
        print(pose[0][0])
        if -0.2 > pose[0][0] > 0.2:
            color = (0, 0, 255)
            flag = "Head is turned"
        else:
            color = (0, 255, 0)
            flag = "Head is not turned"

        # Do you want to see the pose annotation?
        pose_estimator.draw_annotation_box(image, pose[0], pose[1], color=color)

        # Do you want to see the head axes?
        pose_estimator.draw_axes(image, pose[0], pose[1])

        # Do you want to see the marks?
        # mark_detector.draw_marks(frame, marks, color=(0, 255, 0))

        # Do you want to see the facebox?
        # mark_detector.draw_box(frame, [facebox])

    return image, pose, flag
