def convert_to_gray(frame):
# Oblicz wartość jasności pikseli przy użyciu odpowiednich wag dla każdego kanału
    gray = frame[:, :, 0] * 0.114 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.299
    return gray.astype('uint8')
