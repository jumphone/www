# Python Control Flow - Lecture Handout (90 minutes)

**Course:** Programming I  
**Week:** 04  
**Topic:** Control Flow, Conditionals, and Loops  
**Format:** Instructor Teaching Notes

---

## Lecture Overview

**Total Time:** 90 minutes  
**Structure:** 5 main sections, 44 content slides  
**Target:** Beginner programmers with basic Python syntax knowledge

**Learning Objectives:**
- Understand how programs make decisions and repeat tasks
- Master `if-elif-else` conditional structures
- Implement `while` and `for` loops correctly
- Recognize common control flow patterns and pitfalls
- Build simple interactive programs (games, grading systems)

---

## Section 1: Control Flow Fundamentals (15 minutes)

### Slide s1.1: Conditional Statements - Traffic Light
**Time:** 2 minutes  
**Key Concepts:** Sequential vs. decision-based execution, `if-elif-else` chain

**Talking Points:**
- Control flow is about *choice* - programs don't just run top-to-bottom
- The traffic light is a classic finite state machine example
- Emphasize: only ONE branch executes (first True condition)
- Ask students: "What happens if we check 'green' before 'red'?" (Answer: logic error, but no syntax error - dangerous!)

**Common Pitfall:** Students may think all `elif` blocks run. Stress the mutual exclusivity.

---

### Slide s1.2: Flowchart - Decision Making
**Time:** 1 minute  
**Key Concepts:** Visualizing program flow, diamond = decision, rectangle = action

**Talking Points:**
- Flowcharts help plan logic before coding
- Show how the diamond's arrows branch based on conditions
- Mention: real programs have many nested diamonds

**Interactive:** Have students draw a flowchart for "Should I bring an umbrella?" on paper.

---

### Slide s1.3: While Loops - Morning Run
**Time:** 2 minutes  
**Key Concepts:** Repetition, loop variable, termination condition

**Talking Points:**
- `while` loops are for *indefinite* repetition (don't know exact iterations upfront)
- The loop variable `runs_remaining` must change inside the loop
- Without `runs_remaining = runs_remaining - 1`, it's an infinite loop
- The `time.sleep(1)` simulates work; in real code this could be sensor reading, file processing, etc.

**Demonstration Tip:** Run this code live and show how the counter decrements. Then comment out the decrement line to show an infinite loop (but have Ctrl+C ready!).

---

### Slide s1.4: Flowchart - Loop Execution
**Time:** 1 minute  
**Key Concepts:** Loop flowchart pattern, feedback arrow

**Talking Points:**
- The arrow back to the decision diamond is the "loop"
- This visual shows why it's called a "loop" - execution cycles back
- Contrast with `if` flowchart (no feedback arrow)

---

### Slide s1.5: Why Control Flow Matters - Automatic Door
**Time:** 3 minutes  
**Key Concepts:** Real-world application, sensor simulation, continuous monitoring

**Talking Points:**
- This is an *event-driven* system (common in robotics, IoT)
- `while sensor_active:` creates an infinite loop - intentional!
- The `object_detected()` function simulates a sensor; in reality, this would read hardware
- Emphasize: the loop runs "forever" until external shutdown
- Ask: "What if we forget the `else: close_door()`?" (Answer: door stays open - security issue!)

**Career Connection:** This pattern is used in self-driving cars, smart home devices, industrial automation.

---

### Slide s1.6: Vending Machine Example
**Time:** 2 minutes  
**Key Concepts:** Accumulator pattern, input validation, business logic

**Talking Points:**
- `coins` is an accumulator variable (common pattern)
- The loop stops when a *condition* is met (coins >= 5), not a fixed count
- **Question 1:** "How to limit coins per insertion?"  
  → Answer: Add `if insert_coins > 3: print("Too many!"); continue`
- **Question 2:** "How to return extra coins?"  
  → Answer: Calculate `extra = coins - 5` and print it

**Common Mistake:** Students may try to check `coins == 5` exactly, which fails if user inserts 2 then 3 (total 5, but second insertion exceeds). Teach `>=` is safer.

---

### Slide s1.7: Common Patterns
**Time:** 2 minutes  
**Key Concepts:** Flag-controlled vs. counter-controlled loops

**Talking Points:**
- **Flag pattern:** Use when termination depends on user input or complex condition
  - Example: game main menu, server running
- **Counter pattern:** Use when you know maximum iterations
  - Example: password attempts, processing fixed number of files
- Show both ascending (`attempts < 10`) and descending (`attempts > 0`) patterns

**Memory Aid:** "Flags are for events, counters are for numbers."

---

### Slide s1.8: Take-home Message
**Time:** 2 minutes  
**Key Concepts:** Summary, infinite loop danger

**Talking Points:**
- **CRITICAL:** Always update loop condition variable!
- Show the infinite loop example - this is the #1 beginner mistake
- The comment `# Don't forget this!` should be a mental mantra
- Mention: if your program "hangs," check for infinite loops first

**Demonstration:** Show a real infinite loop and how to kill it (Ctrl+C, Task Manager).

---

## Section 2: Conditionals in Python (20 minutes)

### Slide s2.1: `if` Statement Basics
**Time:** 2 minutes  
**Key Concepts:** Syntax, colon, indentation

**Talking Points:**
- The colon `:` is non-negotiable - it tells Python "a block is coming"
- Indentation is not for style; it's *syntax* (part of the language)
- 4 spaces is PEP 8 standard; never use tabs in Python
- Show error: `IndentationError` if missing, `SyntaxError` if missing colon

**Live Demo:** Show the same code with 2 spaces, 4 spaces, and tabs - all work, but mixing fails.

---

### Slide s2.2: Indentation Demo
**Time:** 1 minute  
**Key Concepts:** Visual distinction between correct/incorrect

**Talking Points:**
- Python has no `{}` or `begin/end` - indentation *is* the block structure
- Wrong indentation creates logic errors or syntax errors
- IDE helps: most show spaces vs. tabs

**Rule of Thumb:** "If you see a colon, the next line must be indented."

---

### Slide s2.3: Comparison Operators
**Time:** 2 minutes  
**Key Concepts:** `==`, `!=`, `>`, `<`, `>=`, `<=`

**Talking Points:**
- `==` is *equality* check, `=` is *assignment* (coming up next)
- Comparison results are always `True` or `False` (boolean type)
- Real-world example: luggage height check is common in travel apps
- Chain comparisons work: `0 <= score <= 100` is valid Python

**Exercise:** Have students write 3 comparisons about their age/height.

---

### Slide s2.4: Logical Operators
**Time:** 3 minutes  
**Key Concepts:** `and`, `or`, `not`, truth tables

**Talking Points:**
- `and`: Both True → True (like multiplication)
- `or`: At least one True → True (like addition, but max 1)
- `not`: Flips the boolean
- **Truth Table Drill:** Ask "True and False?" "False or True?" "not True?"
- Weather example: `if is_raining and not has_umbrella:` is a common real-life decision

**Common Mistake:** `if age > 18 and < 65:` is WRONG. Must be `if age > 18 and age < 65:`.

---

### Slide s2.5: Common Mistake Fix (= vs ==)
**Time:** 2 minutes  
**Key Concepts:** Assignment vs. comparison, syntax error prevention

**Talking Points:**
- This is the #2 beginner mistake after indentation
- `if temperature = 30:` tries to *assign* 30 to temperature, then check if 30 is truthy
- Python prevents this: `SyntaxError: invalid syntax`
- Many languages (C, JavaScript) allow this and create subtle bugs

**Memory Aid:** "if variable *equals* value" → `==`. "Assign variable *to* value" → `=`.

---

### Slide s2.6: Multi-Condition Flow
**Time:** 2 minutes  
**Key Concepts:** `elif` ladder, mutually exclusive branches

**Talking Points:**
- Only the *first* True condition runs; others are skipped
- Order matters! If `age < 18` was after `age < 65`, it would never trigger
- This is *not* a switch statement - it's a series of prioritized checks
- Ask: "What if age is exactly 18?" (Answer: goes to `else` branch)

**Best Practice:** Use `elif` when conditions are mutually exclusive; use separate `if`s when they can both be true.

---

### Slide s2.7: Nested Conditions
**Time:** 3 minutes  
**Key Concepts:** Nested blocks, indentation levels, complexity management

**Talking Points:**
- Each `if` creates a new block level; nested `if` is level 2
- **Rule:** Max 3 nesting levels recommended (PEP 8)
- Deeper nesting → code smell, needs refactoring
- Show how to flatten: `if age < 18 or (age >= 18 and is_student):`

**Refactoring Demo:** Convert nested example to flat `elif` chain if possible.

---

### Slide s2.8: Ticket System Flowchart
**Time:** 3 minutes  
**Key Concepts:** Complex decision logic, priority order

**Talking Points:**
- This is a *priority-based* discount system (age first, then status)
- **Question 1:** 19-year-old student without membership → "Student discount" (first match)
- **Question 2:** 19-year-old student with membership → "Student discount" (membership never checked)
- **Question 3:** How to get both discounts? → Cannot with `elif`; need separate `if`s or combine conditions
- Show solution: Use separate discount variables and sum them

**Business Logic:** Explain why companies prioritize certain discounts (e.g., age-based over membership).

---

### Slide s2.9: Truth Value Testing
**Time:** 2 minutes  
**Key Concepts:** "Falsy" values, implicit boolean conversion

**Talking Points:**
- Python treats many non-boolean values as False in `if` statements
- **Falsy values:** `False`, `None`, `0`, `""`, `[]`, `{}`, `set()`
- Everything else is Truthy
- `if not name:` is Pythonic for "if name is empty"
- This is why `while True:` works (True is always truthy)

**Caution:** `if not name:` is clean, but beginners should learn explicit checks first (`if name == ""`).

---

### Slide s2.10: Short-form Conditional Expression
**Time:** 2 minutes  
**Key Concepts:** Ternary operator, readability trade-off

**Talking Points:**
- This is Python's ternary operator: `value_if_true if condition else value_if_false`
- **Not recommended for beginners** - can reduce readability
- Use only for simple assignments, not complex logic
- The "preferred" version is clearer for novices and debuggers

**When to Use:** Simple config values, not control flow. Example: `debug = True if env == "dev" else False`.

---

## Section 3: Loop Structures in Python (25 minutes)

### Slide s3.1: For Loop Basics
**Time:** 3 minutes  
**Key Concepts:** Iteration, iterables, `for...in` syntax

**Talking Points:**
- `for` loops are for *definite* iteration (know the sequence)
- Works on any iterable: lists, strings, tuples, dictionaries, files
- The loop variable (`item`) takes each value in sequence
- Contrast with `while`: `for` is safer (harder to create infinite loops)

**Shopping List Analogy:** You have the list; you just check each item. No condition to manage.

---

### Slide s3.2: The range() Function
**Time:** 4 minutes  
**Key Concepts:** Three signatures, zero-indexing, half-open intervals

**Talking Points:**
- **Single arg:** `range(5)` → 0,1,2,3,4 (5 numbers, starts at 0)
- **Two args:** `range(2,5)` → 2,3,4 (starts at 2, stops *before* 5)
- **Three args:** `range(0,10,2)` → 0,2,4,6,8 (step size 2)
- **Critical:** `range()` is lazy (generates numbers on demand), not a list
- Common use: `range(len(some_list))` for index-based iteration

**Memory Aid:** "Start, Stop, Step" - always stops *before* the stop value.

---

### Slide s3.3: String Traversal with Index
**Time:** 3 minutes  
**Key Concepts:** `enumerate()`, index-value pairs

**Talking Points:**
- `enumerate()` is the Pythonic way to get both index and value
- Returns pairs: (0, 'h'), (1, 'e'), etc.
- Alternative: `for i in range(len(word)):` then `word[i]` (less clean)
- Useful when you need to know position (e.g., find all 'a' at even indices)

**Performance Note:** `enumerate()` is efficient; no need to manually count.

---

### Slide s3.4: While Loop Mechanics
**Time:** 3 minutes  
**Key Concepts:** Condition checking, manual control, alarm clock analogy

**Talking Points:**
- `while` checks condition *before* each iteration
- The loop body must modify the condition variable
- **Alarm clock analogy:** It keeps ringing *while* you haven't pressed snooze
- Contrast `for`: `while` is for "keep doing until something changes"

**Common Error:** Forgetting to decrement/increment → infinite loop.

---

### Slide s3.5: Termination Condition Design
**Time:** 2 minutes  
**Key Concepts:** Infinite loop danger, commented dangerous code

**Talking Points:**
- The commented code is a *real* bug pattern
- Temperature never changes → loop runs forever
- This is why `while True:` with `break` is sometimes safer (explicit exit)
- **Rule:** Every `while` loop must have a clear path to termination

**Design Pattern:** Write the termination condition first, then the loop body.

---

### Slide s3.6: Safe Loop Writing Technique
**Time:** 3 minutes  
**Key Concepts:** Constants, initialization, increment pattern

**Talking Points:**
- **SAFE pattern:** 1) Initialize, 2) Define MAX, 3) Check condition, 4) Increment
- Use UPPER_CASE for constants (`MAX_ATTEMPTS`) - signals "don't change"
- `counter += 1` is shorthand for `counter = counter + 1`
- This pattern prevents off-by-one errors

**Off-by-One Demo:** Show `while counter <= MAX_ATTEMPTS` vs `<` - difference in iterations.

---

### Slide s3.7: Break Statement
**Time:** 3 minutes  
**Key Concepts:** Emergency exit, loop termination from inside

**Talking Points:**
- `break` immediately exits the *nearest* enclosing loop
- Use case: found what you're looking for, no need to continue
- Security example: stop checking passwords after finding "admin"
- **Caution:** Overuse makes logic hard to follow (multiple exit points)

**Alternative:** Sometimes better to refactor condition: `while not found and i < max:`.

---

### Slide s3.8: Continue Statement
**Time:** 2 minutes  
**Key Concepts:** Skip iteration, loop short-circuit

**Talking Points:**
- `continue` jumps to *next* iteration, skipping remaining code
- Use case: filter out unwanted values (odd numbers)
- Contrast `break`: `continue` keeps looping; `break` stops completely
- **Performance:** Can be faster than nested `if` (flattens logic)

**Example:** Process only valid files in a directory, skip `.tmp` files.

---

### Slide s3.9: Else Clause in Loops
**Time:** 3 minutes  
**Key Concepts:** Loop-else, completion detection, unusual syntax

**Talking Points:**
- The `else` block runs *only* if loop completes *without* `break`
- **Use case:** Search loops - "found it" vs. "not found"
- Confusing name: it's not "if condition else" - it's "if not break"
- Many Python developers avoid this due to low readability

**Example:** Check if a number is prime (break if divisible, else it's prime).

---

### Slide s3.10: Nested Loops: Multiplication Table
**Time:** 4 minutes  
**Key Concepts:** Nested iteration, Cartesian product, `end="\t"`

**Talking Points:**
- Outer loop runs once per row; inner loop runs *completely* for each outer iteration
- Total iterations = outer_count × inner_count (here 3×3=9)
- `end="\t"` prevents newline (tab-separated)
- The `print()` after inner loop creates row separation

**Visualization:** Draw a 3x3 grid, show how `i` and `j` move.

---

### Slide s3.11: Understanding Indentation Levels
**Time:** 3 minutes  
**Key Concepts:** Indentation hierarchy, block scope

**Talking Points:**
- **Level 1:** Outer loop (runs twice)
- **Level 2:** Inner loop (runs 2×2=4 times total)
- **Level 3:** `if` inside inner loop (checked 4 times)
- The final `print("----")` is level 1 (runs twice, after each inner loop)
- **Rule:** Each level must be exactly 4 spaces more than previous

**Debugging Tip:** Use vertical lines in IDE to visualize levels.

---

## Section 4: Control Flow - Practical Examples (20 minutes)

### Slide s4.1: Smart Grade Rating System
**Time:** 3 minutes  
**Key Concepts:** Multi-tier logic, boundary values, float input

**Talking Points:**
- **Boundary testing:** What if score is exactly 90? (Goes to A, because `>=`)
- What if score is 89.9? (Goes to B)
- **Data validation:** No check for <0 or >100 - can add later
- This is a *priority ladder*: checks from highest down

**Ask Students:** "How would you add an 'F' grade for <60?" (Add `elif score >= 60` before else, change else to F).

---

### Slide s4.2: Adding Loop for Multiple Inputs
**Time:** 3 minutes  
**Key Concepts:** Infinite menu loop, break on sentinel value

**Talking Points:**
- `while True:` creates an "infinite" menu - common pattern
- Sentinel value `'q'` quits the loop
- `.lower()` handles 'Q' or 'q' (user-friendly)
- **Placement:** Check quit *before* processing to avoid errors

**Enhancement:** Add `try-except` for non-numeric input (preview error handling).

---

### Slide s4.3: Number Guessing Game
**Time:** 4 minutes  
**Key Concepts:** Random module, game loop, user feedback

**Talking Points:**
- `random.randint(1,100)` includes both endpoints (1 and 100)
- The loop is the "game round" - continues until correct guess
- Feedback ("Too high/low") is essential for user experience
- This is a *binary search* problem - smart players win in ~7 guesses

**Interactive:** Play one round with the class. Have them shout guesses.

---

### Slide s4.4: Tracking Attempts
**Time:** 3 minutes  
**Key Concepts:** Game difficulty, attempt limiting, counter pattern

**Talking Points:**
- Adding `attempts` makes it a *challenge* (5 tries max)
- The `attempts < 5` condition prevents infinite play
- **Game Over check:** Must be *outside* loop (after exit)
- Show how to combine with previous slide's `while True` pattern

**Design Decision:** Why 5 attempts? Balance between difficulty and frustration.

---

### Slide s4.5: Victory/Failure Branches
**Time:** 2 minutes  
**Key Concepts:** Post-loop condition check, final message

**Talking Points:**
- Need to check *why* loop ended: success or failure?
- `if guess == target:` determines victory
- `else` (implicitly `attempts == 5`) means failure
- Provide the answer on failure (good UX, prevents rage-quitting)

**Code Smell:** Repeating `str(target)` - could store in variable.

---

### Slide s4.6: Key Concepts Summary
**Time:** 2 minutes  
**Key Concepts:** Review, error handling preview

**Talking Points:**
- `try-except` is mentioned but not detailed - next week's topic
- Counters track state across loop iterations
- Random module is essential for games, simulations, testing
- This slide bridges theory to practice

**Transition:** "Now let's see the complete, runnable versions."

---

### Slide s4.7: Final Complete Code Demo
**Time:** 3 minutes  
**Key Concepts:** Integrated examples, ready-to-run code

**Talking Points:**
- **Grade System:** Show how it combines loop + conditionals
- **Guessing Game:** Full implementation with attempt tracking
- **Bug Alert:** The grade system has a logic error - it asks for input twice! (score = input... then score = float(input...))
- **Fix:** Remove first input, keep only the float conversion

**Live Coding:** Fix the bug in real-time to show debugging process.

---

## Section 5: Special Considerations (10 minutes)

### Slide s5.1: Multi-line Conditional Statements
**Time:** 1 minute  
**Key Concepts:** Line continuation, readability

**Talking Points:**
- Parentheses `()` allow multi-line conditions without `\`
- Improves readability for complex logic
- All lines must be indented equally (PEP 8)

**Alternative:** Use a helper variable (next slide).

---

### Slide s5.2: Splitting Long Logical Expressions
**Time:** 2 minutes  
**Key Concepts:** Refactoring, descriptive variable names

**Talking Points:**
- Long conditions are hard to read and debug
- **Descriptive variables** act as self-documenting code
- Each part can be tested independently
- **Performance:** Minimal overhead, worth it for clarity

**Rule of Thumb:** If condition doesn't fit on one line (80 chars), split it.

---

### Slide s5.3: Debugging with Print Statements
**Time:** 2 minutes  
**Key Concepts:** Debug output, tracing execution

**Talking Points:**
- `print()` debugging is the #1 technique for beginners
- Shows variable values at each iteration
- **Label your debug prints:** `"DEBUG: counter = "` not just `counter`
- Remove debug prints before final submission (or comment out)

**Advanced:** Introduce `logging` module as professional alternative.

---

### Slide s5.4: Using TODO Comments
**Time:** 1 minute  
**Key Concepts:** Code planning, future work

**Talking Points:**
- `TODO` is a convention recognized by IDEs (PyCharm, VS Code)
- Marks incomplete code without breaking functionality
- **Temporary solution:** Return a placeholder value (10% discount)
- **Warning:** Don't leave TODOs in production code!

---

### Slide s5.5: Missing Colon Error
**Time:** 1 minute  
**Key Concepts:** SyntaxError, common typo

**Talking Points:**
- Forgetting `:` is a `SyntaxError` - easy to fix
- Error message points to the line *after* the missing colon
- **Habit:** After typing `if`/`while`/`for`, type `:` immediately

---

### Slide s5.6: Indentation Error Examples
**Time:** 1 minute  
**Key Concepts:** IndentationError, mixing spaces/tabs

**Talking Points:**
- **Never mix tabs and spaces** - Python 3 forbids it
- Configure IDE to insert 4 spaces when Tab key pressed
- `IndentationError: unexpected indent` means inconsistent levels

**Fix:** Most IDEs have "convert tabs to spaces" command.

---

### Slide s5.7: Floating Point Comparison
**Time:** 2 minutes  
**Key Concepts:** Floating-point imprecision, epsilon tolerance

**Talking Points:**
- **Why?** Computers represent decimals in binary; some fractions are infinite
- `0.1 + 0.2 == 0.3` is `False` (result is 0.30000000000000004)
- **Solution:** Check if difference is *very small* (`< 1e-9`)
- **Epsilon:** Greek letter ε, represents tiny tolerance
- **Alternative:** Use `decimal` module for financial calculations

**Demonstration:** Print `0.1 + 0.2` to show the weird result.

---

### Slide s5.8: While Loop Flow Control
**Time:** 1 minute  
**Key Concepts:** Safe pattern recap

**Talking Points:**
- This is the **canonical safe while loop** pattern
- Initialize, check, execute, increment - all visible
- Use this template for all beginner `while` loops
- **Mermaid diagram** shows the flow clearly

---

## Summary and Practice (5 minutes)

### Key Takeaways
1. **Conditionals:** Use `if-elif-else` for decisions; watch indentation and colons
2. **Loops:** `for` for sequences, `while` for conditions; always update loop variable
3. **Control:** `break` to exit, `continue` to skip; `else` on loops is tricky
4. **Safety:** Initialize counters, use constants, avoid infinite loops
5. **Debugging:** Print statements, TODO comments, watch `==` vs `=`

### Practice Exercises (Assign for Homework)
1. **Calculator Menu:** Create a loop that shows options (add/subtract/quit) and performs operations until user quits
2. **Password Validator:** Ask for password up to 3 attempts; must contain number and symbol
3. **Number Pyramid:** Use nested loops to print:
   ```
   1
   12
   123
   1234
   ```

### Common Pitfalls to Emphasize
- Infinite loops (forgot increment)
- `=` instead of `==`
- Mixed tabs and spaces
- Off-by-one errors in `range()`
- Forgetting to convert input to `int`/`float`

---

## End of Lecture Notes

