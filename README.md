# ⚛️ Einstein’s Energy–Mass Equivalence (`E = mc²`)

## 📖 Description

This Python program calculates the amount of energy contained in a given mass, based on **Albert Einstein’s equation**:

[
E = m \times c^2
]

Where:

* **E** → Energy (in Joules)
* **m** → Mass (in kilograms)
* **c** → Speed of light (~300,000,000 m/s)

Even if you haven’t studied physics, this simple formula shows that **mass and energy are equivalent** — meaning even a small amount of mass corresponds to a huge amount of energy.

---

## 💡 How It Works

1. The program prompts the user to input a **mass value** (integer, in kilograms).
2. It then applies Einstein’s formula to compute the **equivalent energy** in Joules.
3. Finally, it outputs the result as an integer.

---

## 🧩 Code Example

```python
def main():
    mass = int(input("Mass: "))
    print(energy(mass))

def energy(mass):
    c = 300000000
    return mass * (c ** 2)

if __name__ == "__main__":
    main()
```

---

## 💻 Example Usage

```
Mass: 1
90000000000000000
```

```
Mass: 5
450000000000000000
```

---

## 🧠 Concepts Demonstrated

* User input handling in Python
* Basic arithmetic and variable manipulation
* Implementing real-world physics equations computationally
* Use of functions and `if __name__ == "__main__":` structure

---

## 🧪 Testing 
```python
from einstein import energy

def test_energy():
    assert energy(1) == 90000000000000000
    assert energy(0) == 0
    assert energy(-1) == -90000000000000000
```

Run tests:

```bash
pytest test_einstein.py
```

---


