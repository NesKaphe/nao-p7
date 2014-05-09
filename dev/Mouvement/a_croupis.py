# Choregraphe simplified export in Python.
from naoqi import ALProxy

from naoqi import ALProxy
names = list()
times = list()
keys = list()


def move(motion) :

	names.append("HeadPitch")
	times.append([ 0.04000, 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.34706, 0.44635, -0.17185, -0.08748, -0.05373, 0.04751, 0.04598, 0.06132, 0.05825, 0.05825])

	names.append("HeadYaw")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.00464, 0.00357, -0.00771, -0.02919, 0.33590, 0.33284, 0.33744, 0.32056, 0.32056])

	names.append("LAnklePitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.52620, 0.38959, 0.86207, 0.66878, 0.70867, 0.70867, 0.70867, 0.70867, 0.70867])

	names.append("LAnkleRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00004, -0.07052, 0.07367, 0.03532, 0.05220, 0.05220, 0.05220, 0.05220, 0.05220])

	names.append("LElbowRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.97865, -1.05382, -0.03831, -0.50771, -0.52152, -1.36675, -0.48624, -0.49391, -0.49391])

	names.append("LElbowYaw")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -1.38218, -0.35900, 0.29449, 1.56464, 1.57998, 0.34051, 0.21318, 0.09967, 0.09967])

	names.append("LHand")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.0000, 0.00000, 0.00000, 0.00000, 0.00000, 1.00000, 1.00000, 1.00000, 0.00000])

	names.append("LHipPitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.32517, 0.20560, -0.98172, -1.53589, -1.53589, -1.53589, -1.53589, -1.53589, -1.53589])

	names.append("LHipRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00004, 0.12430, 0.04913, -0.33744, -0.34511, -0.34511, -0.34357, -0.34511, -0.34511])

	names.append("LHipYawPitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00004, -0.72554, -1.13819, -1.14529, -1.14529, -1.14529, -1.14432, -1.14529, -1.14529])

	names.append("LKneePitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.84673, -0.09233, 0.55220, 0.92343, 0.85286, 0.85286, 0.85286, 0.85133, 0.85286])

	names.append("LShoulderPitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 1.43271, 0.57828, 0.31443, -0.13810, -0.14884, -1.16588, -0.22861, -0.07521, -0.07521])

	names.append("LShoulderRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.27301, 0.46016, 0.53226, 0.18864, 0.24847, 0.72707, -0.11356, -0.07674, -0.07828])

	names.append("LWristYaw")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.01683, -0.94192, -0.34519, -1.21037, -1.11066, -0.33752, 0.82678, 0.54760, 0.54606])

	names.append("RAnklePitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.52919, -0.32363, -1.18630, -0.72094, -0.72094, -0.72861, -0.73474, -0.73168, -0.73168])

	names.append("RAnkleRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00004, 0.05220, -0.05211, 0.21020, 0.21020, 0.21020, 0.21020, 0.21020, 0.21020])

	names.append("RElbowRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.98640, 0.03491, 0.05527, 0.14577, 0.15191, 0.16725, 0.18566, 0.16111, 0.16265])

	names.append("RElbowYaw")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 1.38056, 1.15506, 1.16273, 1.16580, 1.15966, 1.15813, 1.15966, 1.15966, 1.15966])

	names.append("RHand")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00529, 0.00538, 0.00535, 0.00535, 0.00535, 0.00535, 0.00535, 0.00535, 0.00535])

	names.append("RHipPitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.32372, 0.03831, -0.37127, -1.20116, -1.20116, -1.20116, -1.20270, -1.20270, -1.20423])

	names.append("RHipRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00004, -0.17944, 0.08288, 0.36053, 0.36053, 0.36053, 0.36053, 0.36053, 0.36053])

	names.append("RHipYawPitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.00004, -0.72554, -1.13819, -1.14529, -1.14529, -1.14529, -1.14432, -1.14529, -1.14529])

	names.append("RKneePitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.84681, 0.70261, 2.11255, 2.11235, 2.11235, 2.11255, 2.11235, 2.11082, 2.11082])

	names.append("RShoulderPitch")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 1.43433, 1.63375, 0.88823, 0.64279, 0.65353, 0.66580, 0.66580, 0.66887, 0.66733])

	names.append("RShoulderRoll")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ -0.27003, -0.56302, -0.20713, 0.17790, 0.16563, 0.15796, 0.16103, 0.16256, 0.16256])

	names.append("RWristYaw")
	times.append([ 0.32000, 3.16000, 5.04000, 6.80000, 7.92000, 8.92000, 10.72000, 11.28000, 11.68000])
	keys.append([ 0.04138, 0.69639, -0.16571, -0.16878, -0.16725, -0.16571, -0.14731, -0.16571, -0.16571])

	try:
	  motion.angleInterpolation(names, keys, times, True);
	except BaseException, err:
	  print err

"""
	names.append("HeadPitch")
	times.append([ 0.04000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.34706, -0.17185, -0.08748, -0.05373, 0.04751, 0.04598, 0.06132, 0.05825, 0.05825])

	names.append("HeadYaw")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.00008, 0.00357, -0.00771, -0.02919, 0.33590, 0.33284, 0.33744, 0.32056, 0.32056])

	names.append("LAnklePitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.09660, 0.38959, 0.86207, 0.66878, 0.70867, 0.70867, 0.70867, 0.70867, 0.70867])

	names.append("LAnkleRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.11654, -0.07052, 0.07367, 0.03532, 0.05220, 0.05220, 0.05220, 0.05220, 0.05220])

	names.append("LElbowRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.43101, -1.05382, -0.03831, -0.50771, -0.52152, -1.36675, -0.48624, -0.49391, -0.49391])

	names.append("LElbowYaw")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -1.20883, -0.35900, 0.29449, 1.56464, 1.57998, 0.34051, 0.21318, 0.09967, 0.09967])

	names.append("LHand")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.00528, 0.00000, 0.00000, 0.00000, 0.00000, 1.00000, 1.00000, 1.00000, 0.00000])

	names.append("LHipPitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.13657, 0.20560, -0.98172, -1.53589, -1.53589, -1.53589, -1.53589, -1.53589, -1.53589])

	names.append("LHipRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.11509, 0.12430, 0.04913, -0.33744, -0.34511, -0.34511, -0.34357, -0.34511, -0.34511])

	names.append("LHipYawPitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.17330, -0.72554, -1.13819, -1.14529, -1.14529, -1.14529, -1.14432, -1.14529, -1.14529])

	names.append("LKneePitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.09208, -0.09233, 0.55220, 0.92343, 0.85286, 0.85286, 0.85286, 0.85133, 0.85286])

	names.append("LShoulderPitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 1.47567, 0.57828, 0.31443, -0.13810, -0.14884, -1.16588, -0.22861, -0.07521, -0.07521])

	names.append("LShoulderRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.12268, 0.46016, 0.53226, 0.18864, 0.24847, 0.72707, -0.11356, -0.07674, -0.07828])

	names.append("LWristYaw")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.08586, -0.94192, -0.34519, -1.21037, -1.11066, -0.33752, 0.82678, 0.54760, 0.54606])

	names.append("RAnklePitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.09975, -0.32363, -1.18630, -0.72094, -0.72094, -0.72861, -0.73474, -0.73168, -0.73168])

	names.append("RAnkleRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.07367, 0.05220, -0.05211, 0.21020, 0.21020, 0.21020, 0.21020, 0.21020, 0.21020])

	names.append("RElbowRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.36053, 0.03491, 0.05527, 0.14577, 0.15191, 0.16725, 0.18566, 0.16111, 0.16265])

	names.append("RElbowYaw")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 1.16273, 1.15506, 1.16273, 1.16580, 1.15966, 1.15813, 1.15966, 1.15966, 1.15966])

	names.append("RHand")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.00538, 0.00538, 0.00535, 0.00535, 0.00535, 0.00535, 0.00535, 0.00535, 0.00535])

	names.append("RHipPitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.13035, 0.03831, -0.37127, -1.20116, -1.20116, -1.20116, -1.20270, -1.20270, -1.20423])

	names.append("RHipRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.06439, -0.17944, 0.08288, 0.36053, 0.36053, 0.36053, 0.36053, 0.36053, 0.36053])

	names.append("RHipYawPitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.17330, -0.72554, -1.13819, -1.14529, -1.14529, -1.14529, -1.14432, -1.14529, -1.14529])

	names.append("RKneePitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.09233, 0.70261, 2.11255, 2.11235, 2.11235, 2.11255, 2.11235, 2.11082, 2.11082])

	names.append("RShoulderPitch")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 1.54171, 1.63375, 0.88823, 0.64279, 0.65353, 0.66580, 0.66580, 0.66887, 0.66733])

	names.append("RShoulderRoll")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ -0.15191, -0.56302, -0.20713, 0.17790, 0.16563, 0.15796, 0.16103, 0.16256, 0.16256])

	names.append("RWristYaw")
	times.append([ 0.32000, 1.20000, 3.08000, 4.84000, 5.96000, 6.96000, 8.76000, 9.32000, 9.72000])
	keys.append([ 0.11654, 0.69639, -0.16571, -0.16878, -0.16725, -0.16571, -0.14731, -0.16571, -0.16571])

	try:
	  motion.angleInterpolation(names, keys, times, True);
	except BaseException, err:
	  print err
"""
