# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.17645, -0.13197, -0.13657, -0.16111, -0.16111])

names.append("HeadYaw")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.01078, -0.01385, -0.05373, -0.09668, -0.08288])

names.append("LAnklePitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.09660, -0.58756, 0.04905, -0.08595, -0.13043])

names.append("LAnkleRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.11654, -0.09813, 0.25008, -0.04444, -0.04444])

names.append("LElbowRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.37732, -0.33590, -0.07052, -1.02314, -0.66265])

names.append("LElbowYaw")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -1.19503, -1.16128, -0.75937, -0.21480, -0.03993])

names.append("LHand")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.00526, 0.00694, 0.01611, 0.01618, 0.01633])

names.append("LHipPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.13503, -0.11501, -1.53589, -1.53589, -1.54163])

names.append("LHipRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.11509, 0.17799, -0.35585, -0.35278, -0.35431])

names.append("LHipYawPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.17330, -0.67338, -1.14529, -1.14529, -1.14529])

names.append("LKneePitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.09208, 0.97558, 2.11255, 2.11228, 2.10921])

names.append("LShoulderPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 1.52015, 1.37289, 0.72401, -0.03379, 0.27301])

names.append("LShoulderRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.09967, 0.14569, 0.12575, 0.23006, -0.07214])

names.append("LWristYaw")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.06132, 0.02910, 0.19938, 0.38959, 0.47857])

names.append("RAnklePitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.10129, 0.42189, 0.93201, 0.92198, 0.92044])

names.append("RAnkleRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.07367, 0.20713, 0.08288, -0.01223, -0.01223])

names.append("RElbowRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.39121, 0.34059, 0.03839, 0.07214, 0.06754])

names.append("RElbowYaw")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 1.16426, 0.99706, 0.00303, 0.32210, 0.32517])

names.append("RHand")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.00537, 0.00716, 0.01696, 0.01696, 0.01696])

names.append("RHipPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.13188, 0.03064, -1.10912, -1.53589, -1.53864])

names.append("RHipRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.06439, -0.14109, -0.73827, -0.73781, -0.73781])

names.append("RHipYawPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.17330, -0.67338, -1.14529, -1.14529, -1.14529])

names.append("RKneePitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.09200, -0.09233, 0.33445, 0.55995, 0.55995])

names.append("RShoulderPitch")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 1.51103, 1.37911, 0.71949, 0.20100, 0.10435])

names.append("RShoulderRoll")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ -0.10129, -0.10589, 0.03524, -0.07367, -0.01385])

names.append("RWristYaw")
times.append([ 0.04000, 0.80000, 3.12000, 5.44000, 6.08000])
keys.append([ 0.12575, 0.10887, -0.23628, -0.21634, -0.21634])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "192.168.1.3", 9559)
  motion.angleInterpolation(names, keys, times, True);
except BaseException, err:
  print err

