# Import the OpenCV and numpy libraries
import cv2
import numpy as np


def get_color_name(r, g, b):
    # Define color ranges in RGB format
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
    }

    # Calculate the Euclidean distance between the given color and each defined color
    min_distance = float('inf')
    closest_color = "unknown"
    for color_name, color_value in colors.items():
        distance = np.sqrt((r - color_value[0]) ** 2 + (g - color_value[1]) ** 2 + (b - color_value[2]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name

    return closest_color


def capture_rgb():
    # Define a video capture object
    vid = cv2.VideoCapture(0)

    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()

        # Check if the frame is captured correctly
        if not ret:
            print("Failed to capture frame")
            break

        # Get the center pixel of the frame
        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2
        b, g, r = frame[center_y, center_x]

        # Get the color name from the RGB values
        color_name = get_color_name(r, g, b)
        print(r, g, b, color_name)

        # Draw a circle at the center of the frame
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), 2)

        # Display the resulting frame with the circle
        cv2.imshow('frame', frame)

        # The 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return r, g, b, color_name


if __name__ == "__main__":
    capture_rgb()
