import math
import os
import random
import sys

# -------------------------------
# Ciphertext you want to solve
# -------------------------------
# Note that the default CIPHERTEXT here is:
#    SOFTWARE DEVELOPERS SHOULD WRITE CODE THAT IS EASY TO READ, TEST, AND MAINTAIN OVER TIME. THIS COURSE IN SOFTWARE CONSTRUCTION FOCUSES ON HOW TO DEVELOP SOFTWARE THAT IS FREE FROM BUGS, UNDERSTANDABLE, AND EASY TO MAINTAIN.
CIPHERTEXT = "CASIQHKU FUBUTAYUKC CJAGTF QKDIU VAFU IJHI DC UHCR IA KUHF, IUCI, HMF NHDMIHDM ABUK IDNU. IJDC VAGKCU DM CASIQHKU VAMCIKGBIDAM SAVGCUC AM JAQ IA FUBUTAY CASIQHKU IJHI DC SKUU SKAN ZGPC, GMFUKCIHMFHZTU, HMF UHCR IA NHDMIHDM."

# -------------------------------
# Path to your local quadgram file
# -------------------------------
QUADGRAM_FILENAME = "english_quadgrams.txt"
QUADGRAM_PATH = os.path.join(os.getcwd(), QUADGRAM_FILENAME)

# -------------------------------
# Load quadgrams
# -------------------------------
def load_quadgrams(filepath):
    """Load quadgram frequency data from a local file."""
    quadgrams = {}
    total = 0
    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) != 2:
                continue
            key, count = parts
            try:
                c = int(count)
            except ValueError:
                continue
            quadgrams[key] = c
            total += c

    log_total = math.log10(total)
    return {q: math.log10(c) - log_total for q, c in quadgrams.items()}

quadgram_log_probs = load_quadgrams(QUADGRAM_PATH)
FLOOR = min(quadgram_log_probs.values()) - 5.0

def score_text(text):
    """Score a candidate plaintext using quadgram frequencies."""
    text = text.upper()
    score = 0
    for i in range(len(text) - 3):
        quad = text[i:i+4]
        score += quadgram_log_probs.get(quad, FLOOR)
    return score

# -------------------------------
# Substitution cipher utilities
# -------------------------------
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def random_key():
    return ''.join(random.sample(ALPHABET, len(ALPHABET)))

def decrypt(ciphertext, key):
    table = str.maketrans(ALPHABET, key)
    return ciphertext.translate(table)

def tweak_key(key):
    i, j = random.sample(range(len(key)), 2)
    key_list = list(key)
    key_list[i], key_list[j] = key_list[j], key_list[i]
    return ''.join(key_list)

# -------------------------------
# Simulated annealing solver
# -------------------------------
def solve(ciphertext, max_iterations=20000, restarts=5):
    best_overall = None
    best_score = float("-inf")

    for restart in range(restarts):
        key = random_key()
        plaintext = decrypt(ciphertext, key)
        best_local_score = score_text(plaintext)
        best_local_key = key

        temperature = 10.0
        cooling = 0.0005

        for _ in range(max_iterations):
            candidate_key = tweak_key(key)
            candidate_plain = decrypt(ciphertext, candidate_key)
            candidate_score = score_text(candidate_plain)

            delta = candidate_score - best_local_score
            if delta > 0 or math.exp(delta / temperature) > random.random():
                key = candidate_key
                best_local_score = candidate_score
                best_local_key = candidate_key

            temperature -= cooling
            if temperature <= 0:
                break

        # Print best result for this restart
        print(f"\n--- Restart {restart+1}/{restarts} ---")
        print("Best plaintext:", decrypt(ciphertext, best_local_key))
        print("Best key:", best_local_key)
        print("Score:", best_local_score)

        if best_local_score > best_score:
            best_score = best_local_score
            best_overall = (decrypt(ciphertext, best_local_key), best_local_key, best_local_score)

    return best_overall

# -------------------------------
# Run solver
# -------------------------------
if __name__ == "__main__":
    # If the user inputs a cipher text, then get the entire ciphertext and solve it.
    # Otherwise, use the default cipher text.
    if len(sys.argv) > 1:
        input_ciphertext = ""
        for i in range(1, len(sys.argv), 1):
            input_ciphertext += (sys.argv[i] + " ")
        plaintext, key, score = solve(input_ciphertext, max_iterations=20000, restarts=10)
    else:
        plaintext, key, score = solve(CIPHERTEXT, max_iterations=20000, restarts=10)
    
    print("\n=== Final Best Decryption ===")
    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Score:", score)
