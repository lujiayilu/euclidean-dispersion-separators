import Mathlib

namespace Separator

/-- Abstract finite-set interface: e is the induced-edge count, D is the degree sum,
and f, g are modular reward sums. X is removed and Y is inserted. -/
noncomputable def gain {I : Type*} (δ : ℝ) (e D f g : I → ℝ) (X Y : I) : ℝ :=
  δ * (e X + e Y - D X) + g Y - f X

def price {I : Type*} (δ : ℝ) (D f g : I → ℝ) (X : I) : ℝ :=
  (δ * D X + f X - g X) / 2

theorem diagonal {I : Type*} (δ η : ℝ) (e D f g : I → ℝ) (X : I) :
    gain δ e D f g X X ≤ η ↔ δ*e X - η/2 ≤ price δ D f g X := by
  unfold gain price
  constructor <;> intro h <;> linarith

theorem realizing {I : Type*} (δ : ℝ) (e D t : I → ℝ) (X Y : I) :
    gain δ e D (fun U => t U-δ*D U) (fun U => -t U) X Y =
    (δ*e X-t X)+(δ*e Y-t Y) := by
  unfold gain
  ring

theorem local_gain {a b η : ℝ} (ha : a ≤ η/2) (hb : b ≤ η/2) : a+b ≤ η := by linarith

/-- The estimate on a tight block after deleting any subset of its vertices.
The empty remainder has zero cost and also satisfies the required inequality. -/
theorem tight_restriction (tU tR eU eR δ η : ℝ)
    (ht : tU = δ*eU-η/2) (hr : δ*eR-η/2 ≤ tR) :
    tU-tR ≤ δ*(eU-eR) := by nlinarith only [ht,hr]

theorem global {a b v : ℝ} (ha : a ≤ v) (hb : b ≤ v) : a+b ≤ 2*v := by linarith

/-- Sum the cost of a fractional partition, using weighted degree incidence
as an explicit hypothesis. -/
theorem partition_cost {I : Type*} (S : Finset I) (w deg edges : I → ℝ)
    (δ η m : ℝ) (degree_count : ∑ i ∈ S, w i * deg i = 2*m) :
    (∑ i ∈ S, w i * (δ*(deg i-2*edges i)+η)) =
      2*δ*m - 2*(∑ i ∈ S, w i*(δ*edges i-η/2)) := by
  calc
    _ = ∑ i ∈ S, (δ*(w i*deg i) - 2*(w i*(δ*edges i-η/2))) := by
      apply Finset.sum_congr rfl
      intro i hi
      ring
    _ = _ := by rw [Finset.sum_sub_distrib, ← Finset.mul_sum, ← Finset.mul_sum, degree_count]; ring
end Separator

