from vidstab import VidStab

stabilizer = VidStab()
stabilizer.stabilize(input_path=0,
                     output_path='stable_webcam.avi',
                     max_frames=1000,
                     playback=True)