from candidate import Candidate
from voter import Voter

import random


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = []

    def generate_candidates(self, count):
        names = [
            'Aang', 'Katara', 'Sokka', 'Zuko', 'Iroh',
            'Appa', 'Momo', 'Toph', 'Azula', 'Suki',
            'Ozai', 'Mai', 'Ty'
        ]

        self.candidates = [
            Candidate(
                name=names[i],
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def generate_voters(self, count):
        self.voters = [
            Voter(
                id=i + 1,
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def run_election(self):
        eliminated = set()
        round_num = 1

        while True:
            print(f"\nROUND {round_num}")

            # initialize vote counts
            vote_count = {
                c: 0 for c in self.candidates if c not in eliminated
            }

            # each voter votes for their highest-ranked non-eliminated candidate
            for voter in self.voters:
                ranking = voter.rank_candidates(self.candidates)

                for candidate in ranking:
                    if candidate not in eliminated:
                        vote_count[candidate] += 1
                        break

            # show results for this round (temporary debugging output)
            print("\nResults:")

            total_votes = len(self.voters)

            for candidate, votes in vote_count.items():
                percent = (votes / total_votes) * 100
                print(f"{candidate.name}: {percent:.2f}% ({votes})")


            # Winner check
            for candidate, votes in vote_count.items():
                if votes > total_votes / 2:
                    print(f"\nWINNER: {candidate.name}")
                    return
                
            
            # Eliminate lowest
            loser = min(vote_count, key = vote_count.get)
            eliminated.add(loser)

            print(f"\nEliminated: {loser.name}")

            round_num += 1


if __name__ == "__main__":
    voting_system = VotingSystem()

    voting_system.generate_candidates(5)
    voting_system.generate_voters(100)

    print("Candidates:")
    for candidate in voting_system.candidates:
        print(candidate)

    print("\nVoters:")
    for voter in voting_system.voters:
        print(voter)

    voting_system.run_election()
