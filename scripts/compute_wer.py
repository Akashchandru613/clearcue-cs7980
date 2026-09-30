"""
compute_wer.py - Word Error Rate (WER) for ASR transcripts.

WER = (substitutions + deletions + insertions) / number of words in the reference

Usage:
    # Compare one pair of sentences
    python scripts/compute_wer.py "it starts with b like boy" "it starts with p like boy"

    # Compare many pairs from a CSV with columns: id, reference, hypothesis
    python scripts/compute_wer.py --csv results/raw/transcripts.csv

Note: WER counts HOW MANY words are wrong, not WHETHER the error changes clinical
meaning. That second question is what this project adds (see README).
"""

import argparse
import csv
import re
import sys


def normalize(text):
    """Lowercase and remove punctuation so 'Boy.' and 'boy' count as the same word."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9' ]+", " ", text)
    return text.split()


def word_errors(reference, hypothesis):
    """Return (substitutions, deletions, insertions, reference_length) using edit distance."""
    ref, hyp = normalize(reference), normalize(hypothesis)
    # dp[i][j] = (total_errors, subs, dels, ins) for ref[:i] vs hyp[:j]
    dp = [[None] * (len(hyp) + 1) for _ in range(len(ref) + 1)]
    dp[0][0] = (0, 0, 0, 0)
    for i in range(1, len(ref) + 1):
        dp[i][0] = (i, 0, i, 0)
    for j in range(1, len(hyp) + 1):
        dp[0][j] = (j, 0, 0, j)
    for i in range(1, len(ref) + 1):
        for j in range(1, len(hyp) + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                continue
            t, s, d, n = dp[i - 1][j - 1]
            options = [(t + 1, s + 1, d, n)]           # substitution
            t, s, d, n = dp[i - 1][j]
            options.append((t + 1, s, d + 1, n))       # deletion
            t, s, d, n = dp[i][j - 1]
            options.append((t + 1, s, d, n + 1))       # insertion
            dp[i][j] = min(options)
    _, subs, dels, ins = dp[len(ref)][len(hyp)]
    return subs, dels, ins, len(ref)


def wer(reference, hypothesis):
    subs, dels, ins, n = word_errors(reference, hypothesis)
    return (subs + dels + ins) / n if n else 0.0


def main():
    parser = argparse.ArgumentParser(description="Compute word error rate (WER).")
    parser.add_argument("reference", nargs="?", help="What was actually said")
    parser.add_argument("hypothesis", nargs="?", help="What the ASR system wrote")
    parser.add_argument("--csv", help="CSV file with columns: id, reference, hypothesis")
    args = parser.parse_args()

    if args.csv:
        total_errors, total_words = 0, 0
        with open(args.csv, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                s, d, i, n = word_errors(row["reference"], row["hypothesis"])
                total_errors += s + d + i
                total_words += n
                print(f"{row['id']}: WER={((s + d + i) / n if n else 0):.2%} (sub={s}, del={d}, ins={i})")
        print(f"\nOverall WER: {total_errors / total_words:.2%}" if total_words else "No rows found.")
    elif args.reference is not None and args.hypothesis is not None:
        s, d, i, n = word_errors(args.reference, args.hypothesis)
        print(f"WER: {(s + d + i) / n if n else 0:.2%}  (substitutions={s}, deletions={d}, insertions={i}, words={n})")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
