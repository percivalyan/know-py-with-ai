import cv2
import os


def video_to_pictures(video_path, output_path):
    video_cap = cv2.VideoCapture(video_path)
    success, image = video_cap.read()
    count = 0

    while success:
        picture_path = os.path.join(output_path, f"image_{count}.jpg")
        cv2.imwrite(picture_path, image)

        # Mengambil frame berikutnya di waktu detik yang berbeda
        video_cap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        success, image = video_cap.read()
        count += 1

    print(f"{count} pictures successfully stored in {output_path}")


# Path video input - example: C:/your_folder/video name in mp4 format"
input_video_path = "C:/video/forest.mp4"

# Path folder output - example: "C:/your_output_folder"
output_folder_path = "C:/output/forest_forest_videotojpgpersecond"

# Create an output folder if it doesn't already exist
os.makedirs(output_folder_path, exist_ok=True)

# Call the conversion function
video_to_pictures(input_video_path, output_folder_path)
