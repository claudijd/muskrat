class Grader:
    def __init__(self, result):
        self.result = result
        self.grade_map = {
            range(90, 101): "A",
            range(80, 90): "B",
            range(70, 80): "C",
            range(60, 70): "D",
            range(-500, 60): "F"
        }

    def grade(self):
        score = 100

        for recommendation in self.result["compliance_recommendations"]:
            score -= 10

        for score_range in self.grade_map.keys():
            if score in score_range:
                return self.grade_map[score_range]
