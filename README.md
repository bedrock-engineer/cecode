# `cecode`

**Civil Engineering Codes in Readable, Usable, Executable Python**

`cecode` is a Python library that implements civil engineering standards and codes of practice as structured, interactive [marimo](https://marimo.io) notebooks.

It enables engineers to:

- Perform calculations as described in codes like the Eurocode using real code-compliant formulas.
- Understand how results are derived via clear, documented, step-by-step notebooks.
- Automate engineering workflows while retaining traceability to the source standards.

> Designed for engineers who need transparency and repeatability—not just black-box results.

## 📦 What’s Inside

- 💻 Python-first code that reflects the logic of engineering standards
- 📓 Marimo notebooks that combine inputs, explanations, formulas, and results
- ⚙️ Executable modules usable in automation pipelines or standalone analysis
- 📖 Mapping of inputs and variables to code clauses, descriptions, units, and LaTeX symbols

## 🧱 Why `cecode`?

Civil engineering standards often describe calculations in written prose, diagrams, or formulae that must be manually translated into code. `cecode` bridges this gap by:

- **Replicating the logic of the code** in precise Python
- **Making inputs explicit**, with documented symbols, units, and meaning
- **Rendering results transparently** in a visual notebook interface
- **Allowing batch or automated use**, via the same functions used in notebooks

This makes it possible to write automated engineering tools while still complying with the original design intent of the code of practice that underpins the design.

## 🚀 Getting Started

1. Clone the repo or download one of the marimo notebooks you're interested in.
2. Run the notebook with:  
   ```bash
   uvx marimo edit --sandbox path/to/cecode_marimo_notebook.py
   ```

## 📁 Proposed Project Structure

```text
cecode/                       # Project root
│
├── src/                      # Source directory (standard for modern Python packaging)
│   └── cecode/               # `cecode` Python package
│       │
│       ├── eurocode_1_1/     # Actions on structures (EN 1991-1)
│       │   ├── defs.py       # Variable definitions for Eurocode 1-1
│       │   ├── clause_2_3_imposed_loads.py
│       │   └── ...
│       │
│       ├── eurocode_2_1/     # Structural concrete (EN 1992-1)
│       │   ├── defs.py       # Variable definitions for Eurocode 2-1
│       │   ├── clause_3_1_design_strength.py
│       │   └── ...
│       │
│       ├── eurocode_3_1/     # Steel design (EN 1993-1)
│       │   ├── defs.py       # Variable definitions for Eurocode 3-1
│       │   ├── clause_6_2_buckling_resistance.py
│       │   └── ...
│       │
│       ├── eurocode_7_1/     # Geotechnical design (EN 1997-1)
│       │   ├── defs.py       # Variable definitions for Eurocode 7-1
│       │   ├── clause_6_5_bearing_resistance.py 
│       │   ├── clause_7_8_pile_design.py
│       │   └── ...
│       │
│       ├── bs_8004/          # British Standard: Foundations
│       │   ├── defs.py
│       │   ├── section_7_shallow_foundations.py
│       │   └── ...
│       │
│       ├── ciria_c580/       # CIRIA C580: Embedded retaining walls
│       │   ├── defs.py
│       │   ├── section_4_wall_design.py
│       │   └── ...
│       │
│       ├── aashto_lrfd/      # AASHTO LRFD Bridge Design (USA)
│       │   ├── defs.py
│       │   └── ...
│       │
│       └── ...
│
├── tests/                    # Unit tests and verification against worked examples
│   ├── test_clause_6_5_bearing_resistance.py
│   └── ...
│
├── pyproject.toml            # Project metadata and build config
└── README.md                 # Project overview
```

## ✍️ Contributing

If you'd like to add more clauses, improve notebook clarity, or expand coverage to other codes:

- Fork the repo
- Write clean, readable Python and nicely formatted marimo notebooks
- Document inputs, intermediate variables and results clearly (symbol, units, description, bounds)
- Match the logic of the source standard, clause by clause
- Open a PR and reference the standard clauses you implemented

## 📄 License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.

> Note: The actual texts of (most or all?) civil engineering codes (like the Eurocode) are copyrighted and not included in this repository.

## 👷 Maintainers

- [@bedrock-engineer](https://github.com/bedrock-engineer)
- You?
