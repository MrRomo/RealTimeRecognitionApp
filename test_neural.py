from neural import Neural
import cv2

if __name__ == "__main__":
    neural = Neural()
    while (True):
        frame = neural.neural_detector()
        cv2.imshow('Video', frame[0])
        if cv2.waitKey(1) & 0xFF == ord('t'):
            neural.neural_recognition('Dilan')
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    neural.videoCapture.release()
    cv2.destroyAllWindows()
