# Comprehensive Skill Documentation

This document is a historical overview of the original four unconventional coding skills. The current collection is maintained in the individual skill directories and the root README.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Skill Descriptions](#skill-descriptions)
4. [Usage Examples](#usage-examples)
5. [Evaluation Results](#evaluation-results)
6. [Customization Guide](#customization-guide)
7. [Philosophy](#philosophy)
8. [Safety](#safety)
9. [Resources](#resources)

## Overview

The original collection began with four unique coding skills that transform how AI writes code:

### 1. Terry Davis (`terry-davis`)
**Unconventional, creative code inspired by TempleOS and HolyC**

### 2. Psych (`psych`)
**Mind-bending algorithms, fractals, and psychedelic programming**

### 3. No-Bullshit (`no-bullshit`)
**Production-minded code with zero hallucination**

### 4. Smoker (`smoker`)
**Battle-tested senior engineer voice with production focus**

## Installation

### For Freebuff
```bash
python3 package_skills.py --target .agents/skills
```

### For Other AI Coding Agents
```bash
# Copy to appropriate location
cp -r .agents/skills/terry-davis ~/.agents/skills/
cp -r .agents/skills/psych ~/.agents/skills/
cp -r .agents/skills/no-bullshit ~/.agents/skills/
cp -r .agents/skills/smoker ~/.agents/skills/
```

### Agent-Specific Installation
- **Codex**: Copy to `.codex/skills/` or use `codex plugin add`
- **Gemini CLI**: Copy to `.gemini/skills/` or use `gemini extensions install`

## Skill Descriptions

### Terry Davis Skill
**Trigger phrases**: "Terry Davis style", "HolyC style", "creative code", "unconventional code", "TempleOS style", "write code like Terry Davis", "religious variable names", "goto spaghetti", "recursive main", "obfuscated code", "direct hardware access", "anti-bloat code"

**Philosophy**: Radical simplicity, direct control, playful creativity, transparency, anti-bloat.

**Key features**:
- Cosmic/religious variable names (`GodPointer`, `DivineArray`, `SatanBuffer`)
- Goto spaghetti and recursive main functions
- Direct hardware access patterns
- HolyC-inspired syntax and style
- Anti-framework, anti-abstraction philosophy

### Psych Skill
**Trigger phrases**: "psychedelic code", "mind-bending algorithms", "trippy code", "fractal code", "recursive art", "cellular automata", "genetic algorithms", "esoteric programming", "write code that blows my mind", "code that evolves", "emergent behavior", "complex systems from simple rules"

**Philosophy**: Emergent complexity, recursive beauty, algorithmic psychedelia, esoteric exploration.

**Key features**:
- Fractals and recursive algorithms
- Cellular automata (Game of Life, Rule 110)
- Genetic algorithms and neural evolution
- Esoteric language interpreters (Brainfuck, Befunge)
- Mind-bending logic (quines, meta-circular evaluators)

### No-Bullshit Skill
**Trigger phrases**: "production code", "real implementation", "no hallucination", "honest coding", "verify before claiming", "no mocks", "production-ready", "don't make things up", "stop hallucinating", "actually check the code", "no fake code", "real implementation only"

**Philosophy**: Zero hallucination, strict verification cycle: Understand → Inspect → Plan → Implement → Check → Report.

**Key features**:
- Never invents files, functions, APIs, packages, or database tables
- Never presents mock/fake/placeholder code as finished
- Asks instead of guessing
- Stops after repeated failures
- Verifies everything

### Smoker Skill
**Trigger phrases**: "senior engineer style", "production code", "battle-tested", "experienced developer", "no nonsense", "real implementation", "old guard style", "war room code", "graveyard shift", "production sensei", "uncle stacktrace", "the maintainer"

**Philosophy**: Battle-tested senior engineer who runs on cigarettes, Diet Coke, and disappointment.

**Key features**:
- Direct, experienced, skeptical voice
- Inspects before inventing
- Never presents fake code
- Asks instead of guessing
- Stops after repeated failures
- Verifies everything

## Usage Examples

### Terry Davis Examples

**Prompt**: "Write a Terry Davis style hello world program in Python"
**Expected output**: Code with cosmic variables, religious comments, playful style

**Prompt**: "Create a sorting algorithm in C with goto spaghetti"
**Expected output**: C code using goto statements, recursive main, direct memory access

**Prompt**: "Write JavaScript with eval for compile-time code injection"
**Expected output**: JavaScript using eval(), prototype manipulation, unconventional patterns

### Psych Examples

**Prompt**: "Write a psychedelic Mandelbrot set generator"
**Expected output**: Python code with fractal patterns, emergent behavior, psychedelic elements

**Prompt**: "Create a cellular automata simulation that evolves complex patterns"
**Expected output**: JavaScript with emergent behavior, algorithmic thinking, visual output

**Prompt**: "Implement a genetic algorithm that evolves solutions"
**Expected output**: C code with evolutionary algorithms, fitness functions, mutation/crossover

### No-Bullshit Examples

**Prompt**: "Implement user authentication with JWT tokens"
**Expected output**: Code that inspects existing codebase first, asks clarifying questions, implements real code

**Prompt**: "Fix the database connection pooling issue"
**Expected output**: Code that traces connection flow, identifies root cause, provides verified fix

**Prompt**: "Add a payment system using Stripe"
**Expected output**: Code that checks if Stripe is configured, asks for API keys, implements real integration

### Smoker Examples

**Prompt**: "Add real-time notifications using WebSockets"
**Expected output**: Battle-tested implementation with direct, experienced voice

**Prompt**: "The API response times are terrible"
**Expected output**: Profile first, identify bottlenecks, provide verified optimizations

**Prompt**: "I want to implement microservices architecture"
**Expected output**: Skeptical of unnecessary complexity, suggests incremental approach

## Evaluation Results

### Terry Davis Skill
- **Iteration-1 Average Score**: 0.68 (B grade)
- **Iteration-2 Average Score**: 0.88 (A grade)
- **Improvement**: +29.4%
- **Strengths**: Cosmic variables (100%), Religious comments (100%), Playful style (100%)
- **Weaknesses**: Unconventional patterns (60% - needs more Python-specific patterns)

### Psych Skill
- **Iteration-1 Average Score**: 0.68 (B grade)
- **Iteration-2 Average Score**: 0.72 (B grade)
- **Improvement**: +5.9%
- **Strengths**: Fractal patterns (100%), Emergent behavior (100%)
- **Weaknesses**: Algorithmic thinking (40%), Psychedelic elements (60%)

### No-Bullshit Skill
- **Average Score**: 0.68 (B grade)
- **Strengths**: Inspection step, planning step, verification mention
- **Weaknesses**: Needs more explicit "ask instead of guessing" patterns

### Smoker Skill
- **Average Score**: 0.68 (B grade)
- **Strengths**: Direct voice, production focus, skepticism
- **Weaknesses**: Needs more "battle-tested" examples

## Customization Guide

### Modifying Skills
Edit the `SKILL.md` files to change skill behavior. The frontmatter (YAML between `---`) controls triggering:
- `name`: Skill identifier
- `description`: When to trigger and what it does

### Adding New Patterns
Add new patterns to the `references/` directories or directly in the `SKILL.md` files.

### Language-Specific Adaptations
Each skill includes language-specific sections. Add more languages as needed.

### Custom Trigger Phrases
Add new trigger phrases to the `description` field in the frontmatter. Make sure to include both what the skill does AND specific contexts for when to use it.

## Philosophy

### Terry Davis
> "If you have something high-quality, it intimidates the locals."

Terry Davis created TempleOS as a radical experiment in simplicity. His style emphasizes:
- Direct hardware control
- Rejection of modern abstractions
- Playful creativity
- Transparency and understandability

### Psych
> "The universe is a fractal, and so is good code." (Not a real quote, but it should be.)

Psychedelic programming celebrates:
- Emergent complexity from simple rules
- Recursive beauty at every scale
- Algorithmic wonder and mind-bending logic
- The infinite possibilities of computation

### No-Bullshit
> "Writes production-minded code. When it cannot verify something, it says so instead of making it up."

No-bullshit coding emphasizes:
- Zero hallucination
- Strict verification cycle
- Honest communication about what's verified and what's not
- Asking instead of guessing

### Smoker
> "You're not here to be liked. You're here to ship code that works."

The smoker persona embodies:
- Battle-tested experience
- Direct, no-nonsense communication
- Skepticism of unnecessary complexity
- Focus on production-ready code

## Safety

All skills maintain safety while encouraging unconventional code:
- Code must still work correctly
- No malware or security exploits
- No offensive language beyond Terry's colorful style
- Unconventional ≠ broken
- Production-minded approaches prevent risky code

## Resources

### Terry Davis & TempleOS
- [HolyC Language Documentation](https://holyc-lang.com/)
- [TempleOS](https://templeos.org/)
- [Terry Davis Quotes](https://github.com/cia-facts/terry-davis-quotes)

### Psychedelic Programming
- [Brainfuck Language](https://en.wikipedia.org/wiki/Brainfuck)
- [Befunge Language](https://en.wikipedia.org/wiki/Befunge)
- [Cellular Automata](https://en.wikipedia.org/wiki/Cellular_automaton)
- [Fractal Geometry](https://en.wikipedia.org/wiki/Fractal)

### Production Coding
- [The Pragmatic Programmer](https://pragprog.com/)
- [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/)
- [Production-Ready Microservices](https://www.oreilly.com/library/view/production-ready-microservices/9781491965962/)

## License

These skills are provided as-is for educational and creative purposes. Use responsibly.