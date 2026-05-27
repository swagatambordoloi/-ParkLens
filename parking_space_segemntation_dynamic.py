import cv2
import numpy as np

# 1. Path to your parking lot video file
video_path = "parking_lot_simulation2.mp4" 
cap = cv2.VideoCapture(video_path)
success, frame = cap.read()
cap.release()

if not success:
    print("Error: Could not read frame from video. Make sure the path is correct!")
    exit()

# Global state trackers
current_points = []
all_spots = {}
spot_counter = 1

def mouse_callback(event, x, y, flags, param):
    global current_points, spot_counter
    
    # Capture left mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        current_points.append([x, y])
        print(f"Point registered: [{x}, {y}]")
        
        # When 4 points are captured, finalize the spot outline
        if len(current_points) == 4:
            spot_name = f"spot_{spot_counter}"
            all_spots[spot_name] = list(current_points)
            
            # Print the ready-to-use Python dictionary code snippet to the console
            print(f'\n    "{spot_name}": np.array({current_points}, np.int32),')
            
            spot_counter += 1
            current_points = []  # Reset for the next parking spot

# Create a window and attach the mouse event listener
cv2.namedWindow("Define Parking Spots")
cv2.setMouseCallback("Define Parking Spots", mouse_callback)

print("INSTRUCTIONS:")
print("1. Click 4 points clockwise or counter-clockwise for a spot.")
print("2. The script outputs formatted Python code immediately.")
print("3. Press 'c' to clear your current active clicks if you make a mistake.")
print("4. Press 'q' to finish and exit.")

while True:
    img_copy = frame.copy()
    
    # Draw existing saved spots in GREEN
    for spot_name, points in all_spots.items():
        pts = np.array(points, np.int32)
        cv2.polylines(img_copy, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.putText(img_copy, spot_name, tuple(points[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
    # Draw active selection points in RED
    for pt in current_points:
        cv2.circle(img_copy, tuple(pt), 5, (0, 0, 255), -1)
    if len(current_points) > 1:
        cv2.polylines(img_copy, [np.array(current_points, np.int32)], isClosed=False, color=(0, 0, 255), thickness=1)

    cv2.imshow("Define Parking Spots", img_copy)
    key = cv2.waitKey(1) & 0xFF
    
    # Press 'c' to clear current incomplete clicks
    if key == ord('c'):
        current_points = []
        print("Active points cleared.")
        
    # Press 'q' to close the program
    if key == ord('q'):
        break

cv2.destroyAllWindows()