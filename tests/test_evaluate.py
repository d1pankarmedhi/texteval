import sys
sys.path.append("texteval")
from evaluate import Evaluator
import nltk

class TestEvaluator:
    system_summary = "John really loves data science very much and studies it a lot."

    input_text = "John very much loves data science and enjoys it a lot."

    evaluator = Evaluator()

    def test_rouge_evaluation(self):
        res = self.evaluator.rouge_evaluation(self.input_text, self.system_summary)
        assert type(res) == dict

    
    def test_bleu_evaluation(self):
        bleu_score = self.evaluator.bleu_evaluation(self.system_summary, self.input_text) 
        assert type(bleu_score) == float

    def cosine_similarity_evaluation(self):
        cosine_sim = self.evaluator.cosine_similarity_evaluation(self.system_summary, self.input_text)
        assert type(cosine_sim) == float