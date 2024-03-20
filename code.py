import numpy as np
import cv2
import random

# Parameters
N = 20  # number of samples
R = 20  # radius
min_cardinality = 2  # minimum cardinality
φ = 16  # update factor

def add_noise(pixel_value):
    # Add random noise to each RGB channel independently
    noise = np.random.randint(-10, 10, size=3)
    return np.clip(pixel_value + noise, 0, 255)

def compute_distance(pixel_value, sample):
    # Euclidean distance between pixel value and sample
    return np.linalg.norm(pixel_value - sample)

def update_model(background_pixels, buffer_M):
    for pixel in background_pixels:
        if random.randint(1, φ) == 1:
            # Replace a random sample value from buffer M with the pixel value
            index = random.randint(0, N - 1)
            buffer_M[index] = pixel
            if random.randint(1, φ) == 1:
                # Replace a random sample value from the 8-neighborhood with a sample value from buffer M
                neighbor_index = random.randint(0, 7)
                neighbor_sample = buffer_M[(index + neighbor_index) % N]
                buffer_M[index] = neighbor_sample

# Example usage
# Assume you have a series of frames stored in a list called frames
import time
# Initialization


buffer_M = np.random.randint(0, 256, size=(N, 3))  # Initialize buffer M with random values
for i in range(N):
    buffer_M[i] = add_noise(buffer_M[i])


# Capture video
cap = cv2.VideoCapture(0)


while True:
    start_time = time.time()
    ret, frame = cap.read()
    frame=cv2.resize(frame,(300,300))
    print("d")
    if not ret:
        break
    
    # Convert frame to numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Compute distances between pixels and samples
    distances = np.zeros(frame.shape[:2], dtype=np.float32)
    
    
    
    
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            pixel_value = frame[i, j]
            for sample in buffer_M:
                distance = compute_distance(pixel_value, sample)
                if distance <= R:
                    distances[i, j] += 1
    # Threshold distances to classify background
    _, classified_frame = cv2.threshold(distances.astype(np.uint8), min_cardinality, 255, cv2.THRESH_BINARY_INV)

    # Update the model
    background_pixels = frame[classified_frame == 255]
    update_model(background_pixels, buffer_M)

    # Display the frame after background subtraction
    cv2.imshow("Background Subtraction", classified_frame)
    execution_time =  time.time() - start_time
    print("Czas wykonania:", execution_time*1000, "milisekund", )

    # Check for key press and exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
