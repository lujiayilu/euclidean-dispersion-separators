# Fractional graph separation as a Euclidean dispersion gap

[English manuscript (PDF)](manuscript.pdf) · [LaTeX](manuscript.tex) · [Theorem-by-theorem prior-art review (Chinese)](PRIOR-ART.md)

Two copies of a graph determine a Euclidean point set with at most two nonzero distances. Across site rewards that make the first copy locally stable, the largest objective difference to the second copy is a fractional partition cost. One attaining reward system also makes the second copy globally optimal. Disconnected blocks are permitted. The result concerns a prescribed pair of configurations.

Run `python verify.py` (Python 3.10 or newer, standard library). It tests every labelled graph on two through four vertices, all exchange radii, and two tolerances, using rational arithmetic.

With elan installed, run `lake update`, `lake exe cache get`, and `lake build`. Lean and mathlib are pinned to v4.24.0. The Lean file checks algebraic parts of the proof. The spectral embedding, linear-programming duality, and combinatorial counting argument for global optimality are in the written proof.

This research draft was developed with OpenAI Codex, including its problem formulation, proofs and verification code. Independent priority review and peer review remain outstanding.
