# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

def move(motion) :

	names.append("HeadPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.06899, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.08740, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.08740, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.08126, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.09046, [ 3, -0.24000, -0.00153], [ 3, 0.24000, 0.00153]], [ 0.09200, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.09046, [ 3, -0.29333, 0.00153], [ 3, 0.37333, -0.00195]], [ 0.01070, [ 3, -0.37333, 0.00226], [ 3, 0.25333, -0.00153]], [ 0.00916, [ 3, -0.25333, 0.00153], [ 3, 0.62667, -0.00379]], [ -0.02152, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("HeadYaw")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.32210, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.31750, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.31750, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.30216, [ 3, -0.21333, 0.00409], [ 3, 0.24000, -0.00460]], [ 0.29142, [ 3, -0.24000, 0.00384], [ 3, 0.24000, -0.00384]], [ 0.27915, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.28221, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.00311, [ 3, -0.37333, 0.00904], [ 3, 0.25333, -0.00614]], [ -0.00925, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.00303, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnklePitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.70867, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.91882, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.91576, [ 3, -0.26667, 0.00307], [ 3, 0.21333, -0.00245]], [ -0.03686, [ 3, -0.21333, 0.11590], [ 3, 0.24000, -0.13039]], [ -0.16725, [ 3, -0.24000, 0.03554], [ 3, 0.24000, -0.03554]], [ -0.25008, [ 3, -0.24000, 0.08284], [ 3, 0.29333, -0.10124]], [ -0.76858, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.39735, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.73483, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.08595, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LAnkleRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.05220, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.05373, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.05373, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.08288, [ 3, -0.21333, -0.02915], [ 3, 0.24000, 0.03279]], [ 0.25162, [ 3, -0.24000, -0.05343], [ 3, 0.24000, 0.05343]], [ 0.40348, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.19793, [ 3, -0.29333, 0.09494], [ 3, 0.37333, -0.12084]], [ -0.24386, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.11194, [ 3, -0.25333, -0.00806], [ 3, 0.62667, 0.01994]], [ -0.09200, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -0.51692, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.03491, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.03491, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -0.03491, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.28528, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.27608, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ -0.28528, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.05825, [ 3, -0.37333, -0.01808], [ 3, 0.25333, 0.01227]], [ -0.04598, [ 3, -0.25333, -0.00162], [ 3, 0.62667, 0.00401]], [ -0.04138, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LElbowYaw")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.11347, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.29627, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -1.29474, [ 3, -0.26667, -0.00057], [ 3, 0.21333, 0.00045]], [ -1.29320, [ 3, -0.21333, -0.00153], [ 3, 0.24000, 0.00173]], [ -0.51853, [ 3, -0.24000, -0.01074], [ 3, 0.24000, 0.01074]], [ -0.50780, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ -0.52160, [ 3, -0.29333, 0.01381], [ 3, 0.37333, -0.01757]], [ -0.61364, [ 3, -0.37333, 0.04783], [ 3, 0.25333, -0.03245]], [ -0.76244, [ 3, -0.25333, 0.03327], [ 3, 0.62667, -0.08229]], [ -0.96033, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHand")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.00051, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.00303, [ 3, -0.24000, -0.00001], [ 3, 0.26667, 0.00001]], [ 0.00304, [ 3, -0.26667, -0.00001], [ 3, 0.21333, 0.00001]], [ 0.00306, [ 3, -0.21333, -0.00002], [ 3, 0.24000, 0.00002]], [ 0.00323, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.00323, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.00323, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.01666, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.00013, [ 3, -0.25333, 0.00005], [ 3, 0.62667, -0.00013]], [ 0.00000, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -1.53589, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.20261, [ 3, -0.24000, -0.00138], [ 3, 0.26667, 0.00153]], [ -1.20108, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -1.53589, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.53589, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.31920, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ -1.53589, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.52782, [ 3, -0.37333, -0.00807], [ 3, 0.25333, 0.00547]], [ -0.54760, [ 3, -0.25333, -0.14926], [ 3, 0.62667, 0.36923]], [ 0.02765, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -0.34357, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.34511, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.34357, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -0.35891, [ 3, -0.21333, 0.00313], [ 3, 0.24000, -0.00352]], [ -0.36352, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.36352, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ -0.19631, [ 3, -0.29333, -0.09359], [ 3, 0.37333, 0.11912]], [ 0.27463, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.16571, [ 3, -0.25333, 0.01958], [ 3, 0.62667, -0.04843]], [ 0.07061, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LHipYawPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -1.14529, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.14529, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -1.14529, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -1.07683, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.14529, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.06149, [ 3, -0.24000, -0.08380], [ 3, 0.29333, 0.10242]], [ 0.08134, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.52765, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.36045, [ 3, -0.25333, -0.04710], [ 3, 0.62667, 0.11652]], [ -0.03677, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LKneePitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.85133, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.42181, [ 3, -0.24000, 0.00138], [ 3, 0.26667, -0.00153]], [ 0.42027, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 1.72571, [ 3, -0.21333, -0.26545], [ 3, 0.24000, 0.29864]], [ 2.11255, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 2.10768, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 2.11255, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 2.11228, [ 3, -0.37333, 0.00026], [ 3, 0.25333, -0.00018]], [ 1.59225, [ 3, -0.25333, 0.18871], [ 3, 0.62667, -0.46682]], [ 0.14569, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -0.05527, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.59208, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.56294, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.57521, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.33437, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.51998, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.26074, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 2.07085, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 1.02007, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 1.46953, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LShoulderRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -0.06447, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.27463, [ 3, -0.24000, 0.01381], [ 3, 0.26667, -0.01534]], [ -0.28997, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -0.26696, [ 3, -0.21333, -0.02301], [ 3, 0.24000, 0.02588]], [ 0.22852, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.16103, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.59668, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.59668, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.15029, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.21318, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("LWristYaw")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.56907, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.60129, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.60129, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.60896, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.59055, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.59055, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.59055, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 1.78093, [ 3, -0.37333, -0.02487], [ 3, 0.25333, 0.01688]], [ 1.79781, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 1.79013, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnklePitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -0.73628, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.69486, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.70100, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.01998, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.18404, [ 3, -0.24000, 0.04807], [ 3, 0.24000, -0.04807]], [ -0.26841, [ 3, -0.24000, 0.08437], [ 3, 0.29333, -0.10312]], [ -0.77923, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.45095, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.60282, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.11501, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RAnkleRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.21020, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.02450, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.02450, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -0.08279, [ 3, -0.21333, 0.03248], [ 3, 0.24000, -0.03655]], [ -0.23159, [ 3, -0.24000, 0.04167], [ 3, 0.24000, -0.04167]], [ -0.33284, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.07214, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.07052, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.02143, [ 3, -0.25333, -0.01737], [ 3, 0.62667, 0.04297]], [ 0.11049, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.16418, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.18105, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.03491, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.05066, [ 3, -0.21333, -0.01576], [ 3, 0.24000, 0.01773]], [ 0.62591, [ 3, -0.24000, -0.02761], [ 3, 0.24000, 0.02761]], [ 0.65353, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.59830, [ 3, -0.29333, 0.05522], [ 3, 0.37333, -0.07029]], [ 0.06294, [ 3, -0.37333, 0.01356], [ 3, 0.25333, -0.00920]], [ 0.05373, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.11509, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RElbowYaw")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 1.15966, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 1.16426, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.86974, [ 3, -0.26667, 0.00384], [ 3, 0.21333, -0.00307]], [ 0.86667, [ 3, -0.21333, 0.00307], [ 3, 0.24000, -0.00345]], [ 0.06285, [ 3, -0.24000, 0.16388], [ 3, 0.24000, -0.16388]], [ -0.11663, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.16563, [ 3, -0.29333, -0.17999], [ 3, 0.37333, 0.22908]], [ 1.11057, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.97251, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 0.97251, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHand")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.00536, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.00536, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.00536, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.00544, [ 3, -0.21333, -0.00002], [ 3, 0.24000, 0.00002]], [ 0.00549, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.00548, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.00548, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.00552, [ 3, -0.37333, -0.00003], [ 3, 0.25333, 0.00002]], [ 0.01130, [ 3, -0.25333, -0.00105], [ 3, 0.62667, 0.00261]], [ 0.01650, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -1.20423, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.33155, [ 3, -0.24000, 0.01105], [ 3, 0.26667, -0.01227]], [ -1.34383, [ 3, -0.26667, 0.01227], [ 3, 0.21333, -0.00982]], [ -1.53589, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.53589, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.29934, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ -1.53404, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.44354, [ 3, -0.37333, -0.09051], [ 3, 0.25333, 0.06141]], [ -0.62591, [ 3, -0.25333, -0.14426], [ 3, 0.62667, 0.35685]], [ 0.05978, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.36053, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.36053, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.36053, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.33445, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.33599, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.32065, [ 3, -0.24000, 0.01534], [ 3, 0.29333, -0.01875]], [ -0.06592, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.15191, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.02459, [ 3, -0.25333, 0.02488], [ 3, 0.62667, -0.06154]], [ -0.10734, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RHipYawPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -1.14529, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.14529, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -1.14529, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -1.07683, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.14529, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -1.06149, [ 3, -0.24000, -0.08380], [ 3, 0.29333, 0.10242]], [ 0.08134, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.52765, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.36045, [ 3, -0.25333, -0.04710], [ 3, 0.62667, 0.11652]], [ -0.03677, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RKneePitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 2.11235, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 2.11255, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 2.11255, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 1.67057, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ 2.11255, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 2.11255, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 2.11255, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 2.10469, [ 3, -0.37333, 0.00785], [ 3, 0.25333, -0.00533]], [ 1.54478, [ 3, -0.25333, 0.19048], [ 3, 0.62667, -0.47119]], [ 0.11969, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderPitch")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.68114, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.66580, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.68267, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ 0.64279, [ 3, -0.21333, 0.03988], [ 3, 0.24000, -0.04487]], [ 0.30071, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.36053, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ 0.20253, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ 2.05560, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 1.04316, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ 1.56779, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RShoulderRoll")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ 0.14569, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.09660, [ 3, -0.24000, 0.04909], [ 3, 0.26667, -0.05454]], [ -0.23321, [ 3, -0.26667, 0.04410], [ 3, 0.21333, -0.03528]], [ -0.26849, [ 3, -0.21333, 0.03528], [ 3, 0.24000, -0.03969]], [ -0.51700, [ 3, -0.24000, 0.01381], [ 3, 0.24000, -0.01381]], [ -0.53081, [ 3, -0.24000, 0.01381], [ 3, 0.29333, -0.01687]], [ -0.75324, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.29457, [ 3, -0.37333, -0.12764], [ 3, 0.25333, 0.08661]], [ -0.11049, [ 3, -0.25333, 0.00000], [ 3, 0.62667, 0.00000]], [ -0.17645, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	names.append("RWristYaw")
	times.append([ 0.04000, 0.76000, 1.56000, 2.20000, 2.92000, 3.64000, 4.52000, 5.64000, 6.40000, 8.28000])
	keys.append([ [ -0.14270, [ 3, -0.01333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.14884, [ 3, -0.24000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.10742, [ 3, -0.26667, 0.00000], [ 3, 0.21333, 0.00000]], [ -0.11816, [ 3, -0.21333, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.09515, [ 3, -0.24000, 0.00000], [ 3, 0.24000, 0.00000]], [ -0.09515, [ 3, -0.24000, 0.00000], [ 3, 0.29333, 0.00000]], [ -0.09515, [ 3, -0.29333, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.19179, [ 3, -0.37333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.35124, [ 3, -0.25333, -0.07581], [ 3, 0.62667, 0.18753]], [ 0.59822, [ 3, -0.62667, 0.00000], [ 3, 0.00000, 0.00000]]])

	try:

	  motion.angleInterpolationBezier(names, times, keys);
	except BaseException, err:
	  print err

