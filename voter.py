class Voter:

    def __init__(self, id, leaning):
        self.id = id
        self.leaning = leaning

# Ranking logic
    def rank_candidates(self, candidates):
        return sorted(
            candidates,
            key=lambda c: abs(self.leaning - c.leaning)
        )

    def __repr__(self):
        return (
            f"Voter with ID={self.id}, "
            f"leaning: {self.leaning:.3f}"
        )
