import cv2
import keyboard

video_path = 'your_video.mp4'  # замените на путь к вашему видео

playing = False
cap = None

def start_video():
    global cap, playing
    if not playing:
        cap = cv2.VideoCapture(video_path)
        playing = True
        print("Видео запущено!")

def stop_video():
    global cap, playing
    if cap is not None:
        cap.release()
    playing = False
    cv2.destroyAllWindows()
    print("Видео остановлено!")

# Задайте кнопку для запуска/остановки
button_key = 'space'  # например, пробел

while True:
    if keyboard.is_pressed(button_key):
        if not playing:
            start_video()
        else:
            stop_video()
        # Задержка, чтобы избежать повторных срабатываний при удержании клавиши
        while keyboard.is_pressed(button_key):
            pass

    if playing and cap is not None:
        ret, frame = cap.read()
        if not ret:
            # видео закончилось
            stop_video()
            continue
        cv2.imshow('Видео', frame)

        # Нажатие 'q' завершает просмотр
        if cv2.waitKey(25) & 0xFF == ord('q'):
            stop_video()
            break