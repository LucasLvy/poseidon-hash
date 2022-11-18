from parameters import *
import hash


def main():
    poseidon_simple, t = case_simple()

    input_vec = [x for x in range(0, t)]
    print("Input: ", input_vec)
    poseidon_digest = poseidon_simple.run_hash(input_vec)
    print("Output: ", hex(int(poseidon_digest)))


if __name__ == "__main__":
    main()