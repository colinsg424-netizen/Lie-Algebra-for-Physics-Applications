# Lie Algebra for Physics Applications

A Python framework for the construction and numerical analysis of finite-dimensional Lie algebras using matrix representations.

The project implements computational tools for exploring Lie algebra structure, including commutators, structure constants, Jacobi identity verification, Killing forms, Casimir operators, and Lie group exponential maps.

A key application demonstrates quantum spin-½ dynamics using the $\mathfrak{su}(2)$ Lie algebra, including time evolution under a magnetic field Hamiltonian.

---

# Mathematical Framework

This framework represents Lie algebras as matrix subalgebras of $\mathfrak{gl}(n, \mathbb{C})$.

The Lie bracket is defined by:

$$
[X, Y] = XY - YX
$$

where $X, Y$ are matrices in a chosen representation.

---

## Matrix Basis Construction

The elementary matrix units are defined as:

$$
(E_{ij})_{kl} = \delta_{ik}\delta_{jl}
$$

These are used to construct Lie algebra generators.

---

## Construction of $\mathfrak{su}(n)$

Generators are constructed as:

Generators are constructed as:

**Symmetric part:**

$$
S_{ij} = \frac{1}{2}(E_{ij} + E_{ji})
$$

**Antisymmetric part:**

$$
A_{ij} = -\frac{i}{2}(E_{ij} - E_{ji})
$$

Diagonal traceless generators complete the basis.

---

## Construction of $\mathfrak{u}(n)$

The unitary algebra is:

$$
\mathfrak{u}(n) = \mathfrak{su}(n) \oplus \mathfrak{u}(1)
$$

with identity generator:

$$
T_0 = \frac{1}{\sqrt{2n}} I_n
$$

---

## Jacobi Identity

The Lie bracket satisfies:

$$
[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0
$$

This implementation verifies the Jacobi identity numerically across all generator triples.

---

## Structure Constants

In a basis $\{T_a\}$:

$$
[T_a, T_b] = \sum_c f_{abc} T_c
$$

The structure constants are computed using projection onto the generator basis.

---

## Adjoint Representation

Defined by:

$$
\mathrm{ad}_X(Y) = [X, Y]
$$

with components:

$$
(\mathrm{ad}_{T_a})_{bc} = f_{abc}
$$

---

## Killing Form

Computed as:

$$
K(X, Y) = \mathrm{Tr}(\mathrm{ad}_X \, \mathrm{ad}_Y)
$$

---

## Casimir Operator

The quadratic Casimir is:

$$
C_2 = \sum_{a,b} (K^{-1})_{ab} T_a T_b
$$

and commutes with all generators.

---

## Lie Group Exponential Map

Lie group elements are obtained via:

$$
U = e^{iX}
$$

and implemented numerically using matrix exponentiation.

---

## Physical Application: Quantum Spin-½ Dynamics

The framework is applied to $\mathfrak{su}(2)$.

Spin operators satisfy:

$$
[S_i, S_j] = i \epsilon_{ijk} S_k
$$

The Hamiltonian for a spin in a magnetic field is:

$$
H = \mathbf{B} \cdot \mathbf{S}
$$

Time evolution is computed as:

$$
\psi(t) = e^{-iHt} \psi(0)
$$

This models quantum spin precession under Larmor dynamics.

---

# Examples

## 1. Constructing a Lie Algebra

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")

print("Number of generators:", alg.n)
```

## 2. Checking Lie Algebra Closure

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")

print("Closed under commutator:", alg.check_closure())
```

## 3. Computing Structure Constants

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")
```
