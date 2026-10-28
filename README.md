# Python Exam · Ekom

Five original exam files practicing input validation, lists, functions and strings.

**Status:** exam snapshot; question 5 is unfinished. Answers are preserved, not a graded reference implementation.

| Question | Concept | Notes |
| --- | --- | --- |
| [Q1](q_1_grade_input_program.py) | Input loops, validation and grade statistics | Interactive; requires at least ten valid grades before the exit sentinel. |
| [Q2](q_2_median_of_an_unsorted_list.py) | Sorting and median | Sorts the input list in place; assumes nonempty input. |
| [Q3](q_3_snake_case_to_camelCase.py) | String transformations | Assumes nonempty underscore-separated segments. |
| [Q4](q_4_duplicte_string_detector.py) | Collection membership and duplicate detection | Interactive; ends on quit. |
| [Q5](q_5_most_common_word.py) | Word-frequency task | Placeholder only; no solution implemented. |

## Run an example

Python 3, standard library only. From the repository root:

```bash
python3 q_2_median_of_an_unsorted_list.py
python3 q_3_snake_case_to_camelCase.py
```

The checked-in examples print `8.0` and `aBCD`. Questions 1 and 4 prompt for input. There is no automated test suite; edge cases and answer correctness are not comprehensively tested.

[Classwork topic index](https://github.com/LOVA-malamud/LOVA_M) · [Homework](https://github.com/LOVA-malamud/ekom_home_work)

On 2026-10-28, both commands above ran successfully under Python 3.12.10 and produced the stated outputs.
