import sys
import os
import cv2
import rospy
import rosbag
from cv_bridge import CvBridge

def convert(video_path, bag_path, topic_name="/cam0/image_raw"):
    if not os.path.exists(video_path):
        print(f"Error: {video_path} not found")
        return

    print(f"Processing: {video_path} -> {bag_path}")
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_duration = 1.0 / fps
    
    # Use a solid base timestamp Kalibr can parse smoothly
    start_time = rospy.Time(1000000000) 
    bridge = CvBridge()
    
    with rosbag.Bag(bag_path, 'w') as bag:
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_time = start_time + rospy.Duration(count * frame_duration)
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_msg.header.stamp = frame_time
            image_msg.header.frame_id = "cam_frame"
            
            bag.write(topic_name, image_msg, frame_time)
            count += 1
            if count % 100 == 0:
                print(f"Frames mapped: {count}")
                
    cap.release()
    print(f"Successfully wrote {count} frames to bag file!")

if __name__ == "__main__":
    # Expects arguments: python3 convert.py input.mp4 output.bag
    video_in = sys.argv[1]
    bag_out = sys.argv[2]
    convert(video_in, bag_out)
