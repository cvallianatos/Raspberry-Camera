import io
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.rotation = 270    
    camera.start_recording('my_video.h264')
    
    val = input("Hit Enter to stop")
    camera.wait_recording(5)
    camera.stop_recording()