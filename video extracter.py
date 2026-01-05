import cv2
import os

def extract_frames(video_path, output_folder="extracted_frames", target_fps=10):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Get the video's frame rate
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video Frame Rate: {fps} fps")

    # Calculate the number of frames to skip to achieve the target FPS
    frame_skip = int(fps / target_fps)

    frame_count = 0

    while True:
        # Read a new frame
        ret, frame = cap.read()

        # Break the loop if the video has ended (ret is False)
        if not ret:
            break

        # Only save the frame at the target FPS
        if frame_count % frame_skip == 0:
            # Save the frame as an image file
            frame_filename = os.path.join(outputfolder, f"frame{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Video processing complete. Total frames saved: {frame_count // frame_skip}")

--- Usage Example ---
video_file_path = "Video Path ie C:\Users\ blah blah blah"
output_folder_path = "path to output folder"  # Set the desired output folder

Set your desired frames per second here
desired_fps = 5  # Example: Change this value to whatever suits your needs
extract_frames(video_file_path, output_folder=output_folder_path, target_fps=desired_fps)
