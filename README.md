# Text Eval




A tiny python package to find the sentence similarity metrics.

## Getting started

### Installing
```bash
$ pip install texteval
```

### Usage
```python
from texteval.evaluate import Evaluator

system_summary = "John really loves data science very much and studies it a lot."
input_text = "John very much loves data science and enjoys it a lot."

evaluator = Evaluator()
res = evaluator.rouge_evaluation(input_text,system_summary)
print(res)
```
Output consists of Recall, Precision and F1 scores.

```
// Rouge metrics
{
    'rouge-1': {
        'r': 0.8333333333333334, 
        'p': 0.9090909090909091, 
        'f': 0.8695652124007562,
    }, 
    'rouge-2': {
        'r': 0.45454545454545453, 
        'p': 0.5, 
        'f': 0.47619047120181407,
    }, 
    'rouge-l': {
        'r': 0.6666666666666666, 
        'p': 0.7272727272727273, 
        'f': 0.6956521689224953,
    },
}

```

