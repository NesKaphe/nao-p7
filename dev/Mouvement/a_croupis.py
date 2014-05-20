# Choregraphe simplified export in Python.

from naoqi import ALProxy
names = list()
times = list()
keys = list()

'''
Mouvement de Nao pour ramasser la balle
'''

def move(motion) :


	names.append("HeadPitch")
	times.append([ 0.04000, 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.34706, [ 3, -0.01333, 0.00000], [ 3, 0.09333, 0.00000]], [ 0.44635, [ 3, -0.09333, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.13955, [ 3, -1.36000, 0.10947], [ 3, 1.20000, -0.09659]], [ -0.17185, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.08748, [ 3, -0.62667, -0.02034], [ 3, 0.58667, 0.01904]], [ -0.05373, [ 3, -0.58667, -0.02750], [ 3, 0.37333, 0.01750]], [ 0.04751, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.04598, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.06132, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.05825, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.05825, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadYaw")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.00464, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.00916, [ 3, -1.36000, 0.00000], [ 3, 1.20000, 0.00000]], [ 0.00357, [ 3, -1.20000, 0.00370], [ 3, 0.62667, -0.00193]], [ -0.00771, [ 3, -0.62667, 0.00564], [ 3, 0.58667, -0.00528]], [ -0.02919, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.33590, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.33284, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.33744, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.32056, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.32056, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.52620, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.04606, [ 3, -1.36000, -0.16217], [ 3, 1.20000, 0.14309]], [ 0.38959, [ 3, -1.20000, -0.19886], [ 3, 0.62667, 0.10385]], [ 0.86207, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 0.66878, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.70867, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.70867, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.70867, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.70867, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.70867, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00004, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.15949, [ 3, -1.36000, 0.00000], [ 3, 1.20000, 0.00000]], [ -0.07052, [ 3, -1.20000, -0.05106], [ 3, 0.62667, 0.02666]], [ 0.07367, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 0.03532, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.05220, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.05220, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.05220, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.05220, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.05220, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.97865, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.99399, [ 3, -1.36000, 0.01331], [ 3, 1.20000, -0.01174]], [ -1.05382, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.03831, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ -0.50771, [ 3, -0.58667, 0.02169], [ 3, 0.37333, -0.01381]], [ -0.52152, [ 3, -0.37333, 0.01381], [ 3, 0.33333, -0.01233]], [ -1.36675, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.48624, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -0.49391, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.49391, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -1.38218, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.98947, [ 3, -1.36000, -0.18119], [ 3, 1.20000, 0.15987]], [ -0.35900, [ 3, -1.20000, -0.28116], [ 3, 0.62667, 0.14683]], [ 0.29449, [ 3, -0.62667, -0.33118], [ 3, 0.58667, 0.31004]], [ 1.56464, [ 3, -0.58667, -0.02411], [ 3, 0.37333, 0.01534]], [ 1.57998, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.34051, [ 3, -0.33333, 0.07073], [ 3, 0.60000, -0.12732]], [ 0.21318, [ 3, -0.60000, 0.06123], [ 3, 0.18667, -0.01905]], [ 0.09967, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.09967, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00528, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.00244, [ 3, -1.36000, 0.00094], [ 3, 1.20000, -0.00083]], [ 0.00000, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.00000, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 0.00000, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.00000, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.00, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 1.00000, [ 3, -0.60000, 0.00020], [ 3, 0.18667, -0.00006]], [ 1.00000, [ 3, -0.18667, 0.00037], [ 3, 0.13333, -0.00026]], [ 1.00000, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.32517, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.03524, [ 3, -1.36000, -0.09399], [ 3, 1.20000, 0.08293]], [ 0.20560, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.98172, [ 3, -0.62667, 0.29982], [ 3, 0.58667, -0.28068]], [ -1.53589, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.53589, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.53589, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -1.53589, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -1.53589, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.53589, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00004, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.06907, [ 3, -1.36000, -0.02200], [ 3, 1.20000, 0.01941]], [ 0.12430, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.04913, [ 3, -0.62667, 0.07517], [ 3, 0.58667, -0.07037]], [ -0.33744, [ 3, -0.58667, 0.01205], [ 3, 0.37333, -0.00767]], [ -0.34511, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.34511, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.34357, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -0.34511, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.34511, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00004, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.27915, [ 3, -1.36000, 0.12849], [ 3, 1.20000, -0.11337]], [ -0.72554, [ 3, -1.20000, 0.18811], [ 3, 0.62667, -0.09824]], [ -1.13819, [ 3, -0.62667, 0.00758], [ 3, 0.58667, -0.00710]], [ -1.14529, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.14529, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.14529, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -1.14432, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -1.14529, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.14529, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.84673, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.33437, [ 3, -1.36000, 0.16629], [ 3, 1.20000, -0.14673]], [ -0.09233, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.55220, [ 3, -0.62667, -0.17487], [ 3, 0.58667, 0.16371]], [ 0.92343, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.85286, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.85286, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.85286, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.85133, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.85286, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 1.43271, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 1.11824, [ 3, -1.36000, 0.15131], [ 3, 1.20000, -0.13351]], [ 0.57828, [ 3, -1.20000, 0.17602], [ 3, 0.62667, -0.09192]], [ 0.31443, [ 3, -0.62667, 0.12333], [ 3, 0.58667, -0.11546]], [ -0.13810, [ 3, -0.58667, 0.01687], [ 3, 0.37333, -0.01074]], [ -0.14884, [ 3, -0.37333, 0.01074], [ 3, 0.33333, -0.00959]], [ -1.16588, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.22861, [ 3, -0.60000, -0.27729], [ 3, 0.18667, 0.08627]], [ -0.07521, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.07521, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.27301, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.31596, [ 3, -1.36000, -0.03314], [ 3, 1.20000, 0.02924]], [ 0.46016, [ 3, -1.20000, -0.04736], [ 3, 0.62667, 0.02473]], [ 0.53226, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 0.18864, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.24847, [ 3, -0.37333, -0.05983], [ 3, 0.33333, 0.05342]], [ 0.72707, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.11356, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -0.07674, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.07828, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.01683, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.51086, [ 3, -1.36000, 0.16978], [ 3, 1.20000, -0.14980]], [ -0.94192, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.34519, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ -1.21037, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.11066, [ 3, -0.37333, -0.09971], [ 3, 0.33333, 0.08903]], [ -0.33752, [ 3, -0.33333, -0.23065], [ 3, 0.60000, 0.41517]], [ 0.82678, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.54760, [ 3, -0.18667, 0.00215], [ 3, 0.13333, -0.00153]], [ 0.54606, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.52919, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.42488, [ 3, -1.36000, -0.03640], [ 3, 1.20000, 0.03212]], [ -0.32363, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -1.18630, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ -0.72094, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.72094, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.72861, [ 3, -0.33333, 0.00164], [ 3, 0.60000, -0.00296]], [ -0.73474, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -0.73168, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.73168, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00004, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.02919, [ 3, -1.36000, -0.00924], [ 3, 1.20000, 0.00815]], [ 0.05220, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.05211, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 0.21020, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.21020, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.21020, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.21020, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.21020, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.21020, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.98640, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.44337, [ 3, -1.36000, 0.16849], [ 3, 1.20000, -0.14867]], [ 0.03491, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.05527, [ 3, -0.62667, -0.01909], [ 3, 0.58667, 0.01787]], [ 0.14577, [ 3, -0.58667, -0.00964], [ 3, 0.37333, 0.00614]], [ 0.15191, [ 3, -0.37333, -0.00378], [ 3, 0.33333, 0.00338]], [ 0.16725, [ 3, -0.33333, -0.00402], [ 3, 0.60000, 0.00723]], [ 0.18566, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.16111, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.16265, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 1.38056, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 1.25017, [ 3, -1.36000, 0.03993], [ 3, 1.20000, -0.03523]], [ 1.15506, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 1.16273, [ 3, -0.62667, -0.00185], [ 3, 0.58667, 0.00173]], [ 1.16580, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 1.15966, [ 3, -0.37333, 0.00135], [ 3, 0.33333, -0.00121]], [ 1.15813, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 1.15966, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 1.15966, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.15966, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00529, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.00537, [ 3, -1.36000, -0.00002], [ 3, 1.20000, 0.00001]], [ 0.00538, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.00535, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 0.00535, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.00535, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00535, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.00535, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.00535, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00535, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.32372, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.12890, [ 3, -1.36000, -0.06411], [ 3, 1.20000, 0.05657]], [ 0.03831, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.37127, [ 3, -0.62667, 0.21339], [ 3, 0.58667, -0.19977]], [ -1.20116, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.20116, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.20116, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -1.20270, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -1.20270, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.20423, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00004, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.09813, [ 3, -1.36000, 0.03178], [ 3, 1.20000, -0.02804]], [ -0.17944, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.08288, [ 3, -0.62667, -0.09296], [ 3, 0.58667, 0.08703]], [ 0.36053, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.36053, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.36053, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.36053, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.36053, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.36053, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipYawPitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.00004, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.27915, [ 3, -1.36000, 0.12849], [ 3, 1.20000, -0.11337]], [ -0.72554, [ 3, -1.20000, 0.18811], [ 3, 0.62667, -0.09824]], [ -1.13819, [ 3, -0.62667, 0.00758], [ 3, 0.58667, -0.00710]], [ -1.14529, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.14529, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.14529, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ -1.14432, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -1.14529, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -1.14529, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.84681, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.76397, [ 3, -1.36000, 0.02553], [ 3, 1.20000, -0.02253]], [ 0.70261, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 2.11255, [ 3, -0.62667, 0.00000], [ 3, 0.58667, 0.00000]], [ 2.11235, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 2.11235, [ 3, -0.37333, 0.00000], [ 3, 0.33333, 0.00000]], [ 2.11255, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 2.11235, [ 3, -0.60000, 0.00019], [ 3, 0.18667, -0.00006]], [ 2.11082, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 2.11082, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 1.43433, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 1.54631, [ 3, -1.36000, -0.03531], [ 3, 1.20000, 0.03116]], [ 1.63375, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.88823, [ 3, -0.62667, 0.17061], [ 3, 0.58667, -0.15972]], [ 0.64279, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.65353, [ 3, -0.37333, -0.00405], [ 3, 0.33333, 0.00362]], [ 0.66580, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.66580, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.66887, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.66733, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ -0.27003, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ -0.39275, [ 3, -1.36000, 0.05188], [ 3, 1.20000, -0.04578]], [ -0.56302, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.20713, [ 3, -0.62667, -0.12756], [ 3, 0.58667, 0.11942]], [ 0.17790, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.16563, [ 3, -0.37333, 0.00351], [ 3, 0.33333, -0.00314]], [ 0.15796, [ 3, -0.33333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.16103, [ 3, -0.60000, -0.00117], [ 3, 0.18667, 0.00036]], [ 0.16256, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.16256, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.32000, 4.40000, 8.00000, 9.88000, 11.64000, 12.76000, 13.76000, 15.56000, 16.12000, 16.52000])
	keys.append([ [ 0.04138, [ 3, -0.10667, 0.00000], [ 3, 1.36000, 0.00000]], [ 0.39880, [ 3, -1.36000, -0.11599], [ 3, 1.20000, 0.10235]], [ 0.69639, [ 3, -1.20000, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.16571, [ 3, -0.62667, 0.00328], [ 3, 0.58667, -0.00307]], [ -0.16878, [ 3, -0.58667, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.16725, [ 3, -0.37333, -0.00054], [ 3, 0.33333, 0.00048]], [ -0.16571, [ 3, -0.33333, -0.00153], [ 3, 0.60000, 0.00276]], [ -0.14731, [ 3, -0.60000, 0.00000], [ 3, 0.18667, 0.00000]], [ -0.16571, [ 3, -0.18667, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.16571, [ 3, -0.13333, 0.00000], [ 3, 0.00000, 0.00000]]])

	try:

	  motion.angleInterpolationBezier(names, times, keys);
	except BaseException, err:
	  print err

