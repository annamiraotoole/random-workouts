
import move
import generate




arms = BodyArea("arms")
legs = BodyArea("legs")
core = BodyArea("core")


# NEEDS: name, area, base_reps, delta


# LEGS

jump_squat = Move("Jump Squat", legs, 10, 3)

lunge = Move("Lunges (left and right)", legs, 20, 10)

donkey_kick = Move("Donkey Kick (with 15 lbs weight, left and right)", legs, 20, 10)

pistol_squat = Move("Pistol Squat", legs, 5, 2)

# ARMS

pushup = Move("Pushup", arms, 3, 1)

tricep_dips = Move("Tricep Chair Dips", arms, 10, 3)

chin_up = Move("Chin Up", arms, 1, 1)

pull_up = Move("Pull Up", arms, 1, 1)

arm_raise = Move("Side Arm Raise (with 8 lbs weight, left and right)", arms, 10, 3)


