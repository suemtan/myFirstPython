#exercise-tracking app : a user can log an exercise session by naming exercise, intensity and the duration

class ExerciseSession:

    def __init__(self, exname = " ", exintensity = " ", duration = 0):
        self.exname = exname
        self.exintensity = exintensity
        self.duration = duration

    def get_exercise(self):
        return self.exname

    def get_intensity(self):
        return self.exintensity

    def get_duration(self):
        return self.duration

    def set_exercise(self, exercisename):
        self.exname = exercisename

    def set_intensity(self, intensity):
        self.exintensity = intensity

    def set_duration(self, duration):
        self.duration = duration

    def calories_burned(self):
        if self.exintensity == "Low":
            burnedCal = 4 * self.duration

        elif self.exintensity == "Moderate":
            burnedCal = 8 * self.duration

        elif self.exintensity == "High":
            burnedCal = 12 * self.duration

        return burnedCal


new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())

