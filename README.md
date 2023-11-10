# Text Eval

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/d1pankarmedhi/StrapDown.js/graphs/commit-activity) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/d1pankarmedhi/texteval/blob/main/LICENSE.md)
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)




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

