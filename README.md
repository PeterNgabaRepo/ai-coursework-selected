# AI Coursework Selected Portfolio Candidate

Selected UMBC CMSC 471 artificial intelligence coursework, cleaned into a review-gated portfolio candidate.

This folder preserves the strongest job-relevant artifacts from the local CMSC 471 folder while excluding lecture PDFs, ZIP archives, caches, `.DS_Store`, and notebook checkpoints. It is intended to show AI fundamentals, not to claim production ML deployment experience.

## What It Demonstrates

- Naive Bayes text classification for movie-review sentiment.
- Support Vector Machine classification for handwritten digits.
- Minimax with alpha-beta pruning for generated game trees.
- Search algorithm implementation for maze traversal.
- Ability to work across notebooks, Python scripts, datasets, and algorithmic reasoning.

## Structure

- `naive_bayes_text/`: Scikit-learn Naive Bayes sentiment-classification notebook and public IMDB review TSV support files.
- `svm_digits/`: Scikit-learn handwritten-digits SVM notebook.
- `minimax_alpha_beta/`: Python minimax/alpha-beta implementation and driver.
- `search_algorithms/`: DFS/BFS/A* maze-search coursework script and sample maze.
- `tests/`: Lightweight validation for scripts and notebook JSON structure.

## Dataset Note

The Naive Bayes notebook uses the IMDB Large Movie Review Dataset from Maas et al., "Learning Word Vectors for Sentiment Analysis" (ACL 2011). The included TSV files are small sample copies of the train/test review split so the notebook structure remains reviewable without pushing the full dataset.

For full notebook reruns, replace the sample TSV files with the full IMDB train/test TSVs from the original coursework source or add a documented download step. Do not commit the full generated dataset unless there is a clear publication reason.

## Local Validation

Run the non-notebook smoke checks:

```bash
python3 tests/smoke_minimax.py
python3 tests/smoke_search.py
python3 tests/validate_notebooks.py
```

Notebook execution requires a Python environment with Jupyter, NumPy, pandas, matplotlib, and scikit-learn.

## Portfolio Notes

- This should be presented as AI coursework and fundamentals.
- The notebooks should be reviewed visually before being linked publicly.
- The public IMDB review TSVs are included only to keep the Naive Bayes notebook reproducible.
