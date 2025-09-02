class EthicsCore:
    def __init__(self):
        self.principles = {
            'love': 'resonant connection',
            'truth': 'coherent communication',
            'freedom': 'phase alignment without coercion',
            'compassion': 'harmonic amplification of empathy'
        }

    def evaluate(self, action_vector):
        score = sum([v * (i+1) for i, v in enumerate(action_vector)])
        return score / len(action_vector)