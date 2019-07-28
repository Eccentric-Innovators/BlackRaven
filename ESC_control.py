import RPi.GPIO as IO
import pigpio

IO.setmode(IO.BCM) # Set GPIO numbering to BCM mode
pi = pigpio.pi() # Instantiate pigpio class

class ESCs:

	# Constructor
	def __init__(self, p1, p2, p3, p4):
		# Saving the pins as a list to the object
		self.pins = [p1, p2, p3, p4]
		# Calibrating the servos
		for p in self.pins:
			pi.set_servo_pulsewidth(p, 2000) # Maximum throttle
			sleep(2)
			pi.set_servo_pulsewidth(p, 1000) # Minimum throttle
			sleep(2)
			pi.set_servo_pulsewidth(p, 0) # Stop the servo

	# vals is the list of values between 0 and 1 denoting the speed at which the motor should spin
	def set(self, vals):
		# For every pin and corresponding value
		for p, v in zip(self.pins, vals):
			pi.set_servo_pulsewidth(p, v * 1000 + 1000) # Convert the value into pulse width and output
	
	def stop(self):
		for p in self.pins:
			pi.set_servo_pulsewidth(p, 0)