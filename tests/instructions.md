TASK 3C

## Evaluation of Your CoT Problems

### Problem 1

```text
I have my car with me, I want it to get car washed but the car washing business is 50 meters away. should I just walk to go there?
```

**Result: Needs Improvement**

Why:

- too subjective
- no measurable correctness
- model may answer based on opinion/personality
- hard to compare “basic vs CoT” objectively

CoT works best when:

- intermediate reasoning materially improves accuracy.

This problem tests:

- common sense
  more than:
- reasoning decomposition.

---

## Problem 2

```text
A warehouse has 450 units...
```

**Result: Strong Pass**

Excellent CoT problem.

Why it works:

- multi-step arithmetic
- requires state tracking
- easy to verify correctness
- CoT should noticeably improve reliability

This is exactly the kind of problem you want.

---

## Problem 3

```text
[4, 9, 16, 25, 36, 49, _]
```

**Result: Pass**

Good reasoning problem.

Why:

- pattern recognition
- sequence inference
- intermediate reasoning helps explain logic

Though this one may be slightly too easy for Mistral.

Still acceptable.

---

# Important Insight

For CoT experiments, your problems should ideally have:

| Property                  | Why                           |
| ------------------------- | ----------------------------- |
| Verifiable answer         | easier comparison             |
| Multiple reasoning steps  | CoT advantage becomes visible |
| Possibility of failure    | reveals prompt differences    |
| Non-trivial decomposition | demonstrates reasoning        |

---

# Replace Problem 1

You should swap it with something reasoning-heavy.

---

# Better Alternatives

## Option A — Scheduling Logic

```text
John has a meeting at 3:00 PM.
It takes 25 minutes to drive there.
He also needs 15 minutes to prepare before leaving.
If he wants to arrive 10 minutes early, what time should he start preparing?
```

Excellent for CoT.

---

## Option B — Word Problem

```text
A train travels 60 km/h for 2 hours, then 80 km/h for 3 hours.
What is the total distance traveled?
```

Simple but demonstrates decomposition.

---

## Option C — Constraint Reasoning

```text
A pizza is cut into 8 slices.
3 people each eat 2 slices.
How many slices remain?
```

Not amazing, but still better than subjective questions.

---

# My Recommendation

Use:

1. Warehouse inventory problem
2. Sequence prediction
3. Scheduling/time-management problem

That gives:

- arithmetic reasoning
- pattern reasoning
- logical planning

Good diversity.

---

# Your Next Goal

Now implement:

```text
prompts/cot_test.py
```

You will:

- send BASIC prompt
- send CoT prompt
- compare outputs
- save results

---

# Expected Output Structure

Conceptually something like:

```json
[
  {
    "problem": "...",
    "basic_response": "...",
    "cot_response": "..."
  }
]
```

---

# Additional Requirement

You ALSO need:

```text
prompts/cot_analysis.md
```

This is where you explain:

- which performed better
- why
- observed differences

---

# Important Design Advice

For CoT prompt:
avoid only:

```text
Think step-by-step
```

Better:

```text
Solve the problem step-by-step before giving the final answer.
```

More explicit = more reliable.

---

# Your Turn

Replace Problem 1, then implement:

```text
cot_test.py
```

---

## Follow-up prompts

1. **“Review my cot_test.py implementation”**
2. **“Help me write cot_analysis.md”**
3. **“Teach me self-consistency prompting after this”**

---

TASK 3D
Yes. Here’s the full mental model and implementation outline for **Task 3D — Prompt Comparison** so you can work offline productively.

---

# What Task 3D Is ACTUALLY Testing

Not:

> “Can the AI fix code?”

But:

> “Can you demonstrate that engineered prompts outperform naive prompts?”

This is fundamentally:

- an experiment
- a comparison study
- prompt quality evaluation

---

# Core Idea

You will compare:

| Prompt Type       | Example                           |
| ----------------- | --------------------------------- |
| Basic Prompt      | `"Fix this code"`                 |
| Engineered Prompt | structured debugging instructions |

against:

- the SAME buggy code
- using the SAME model

Then compare:

- correctness
- explanation quality
- completeness
- readability

---

# Expected Flow

```text id="bbn1pm"
buggy file
    ↓
basic prompt
    ↓
response

same buggy file
    ↓
engineered prompt
    ↓
response

compare results
    ↓
save JSON
```

---

# Recommended Folder Structure

```text id="uxecg9"
project/
├── prompts/
│   ├── prompt_comparison.py
│   └── prompt_comparison.json
│
├── code_snippets/
│   ├── buggy1.py
│   ├── buggy2.py
│   └── buggy3.py
```

---

# What The Buggy Files Should Look Like

Keep them:

- small
- obvious
- beginner-intermediate level

---

# Recommended Bug Types

## 1. Logic Error

Example:

```python id="y2usdx"
def divide(a, b):
    return a / 0
```

---

## 2. Syntax Error

Example:

```python id="9xpc6d"
for i in range(5)
    print(i)
```

---

## 3. Type/Runtime Error

Example:

```python id="jlwm1t"
numbers = [1,2,3]
print(numbers + 5)
```

---

# Avoid

Do NOT use:

- giant files
- advanced frameworks
- obscure bugs
- multi-file systems

This task is about PROMPTS.

Not software complexity.

---

# Your Two Prompt Types

---

# BASIC Prompt

Minimal instruction.

Example:

```text id="r77b2h"
Fix the following Python code:

{code}
```

That’s intentionally weak.

---

# ENGINEERED Prompt

This is where prompt engineering happens.

Example structure:

```text id="1nrwbw"
You are a beginner-friendly Python debugging assistant.

Analyze the following code carefully.

Tasks:
1. Identify the bug
2. Explain why it happens
3. Provide corrected code
4. Keep the explanation concise

Code:
{code}
```

This should outperform the basic prompt.

---

# What You Should Compare

For each snippet:

- Was the bug identified?
- Was the fix correct?
- Was explanation understandable?
- Was corrected code included?

---

# Suggested JSON Structure

```json id="5wxz3h"
[
  {
    "file": "buggy1.py",
    "basic_prompt_response": "...",
    "engineered_prompt_response": "..."
  }
]
```

---

# Suggested Program Structure

You already know enough Python for this.

Think in functions:

---

## 1. Read code file

```python id="m5l1dy"
read_code_file(path)
```

---

## 2. Build prompts

```python id="ezmjlwm"
build_basic_prompt(code)

build_engineered_prompt(code)
```

---

## 3. Send request to Ollama

Reusable helper:

```python id="ntzj1p"
query_ollama(prompt)
```

---

## 4. Store comparisons

Append results to list.

---

## 5. Save JSON

```python id="34tz4u"
json.dump(...)
```

---

# VERY IMPORTANT INSIGHT

This task is teaching:

- prompt specificity
- instruction hierarchy
- output guidance
- structured prompting

You are essentially demonstrating:

```text id="4a9dlk"
same model
+
better instructions
=
better results
```

That’s the central lesson.

---

# Common Mistakes To Avoid

---

## 1. Making prompts TOO long

Bad:

```text id="d0ny9x"
You are the greatest AI software engineer...
```

Verbose prompts often dilute focus.

---

## 2. Comparing DIFFERENT models

Do NOT:

- use mistral for one
- code-helper for another

Use SAME model.

Otherwise comparison becomes invalid.

---

## 3. Using impossible bugs

If even YOU cannot easily explain the bug,
the comparison becomes messy.

---

# Suggested Timeline

While offline:

## Phase 1

Create:

- buggy files
- prompt templates

---

## Phase 2

Implement:

- file reader
- Ollama request helper

---

## Phase 3

Run comparisons later when internet/local Ollama available.

---

# Most Important Learning From Task 3D

You will realize:

> Prompt quality often matters more than model size.

That is a major real-world AI engineering lesson.

---

# Recommended Engineered Prompt Template

This is probably strong enough for your assignment:

```text id="51l59x"
You are a beginner-friendly Python debugging assistant.

Analyze the following Python code carefully.

Tasks:
1. Identify the bug
2. Explain why the issue occurs
3. Provide corrected code
4. Keep the explanation concise and beginner-friendly

Code:
{code}
```

Simple.
Focused.
Structured.
Good.

---

## Follow-up prompts

1. **“Review my engineered prompt before I implement it”**
2. **“Teach me what makes a prompt high quality technically”**
3. **“After Task 3D, help me transition into Flask for Task 4”**
