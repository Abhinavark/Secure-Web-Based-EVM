import random

# Educational parameters
p = 30803
g = 2
x = 12345  # Private Key (Keep safe, only used for final tally)
y = pow(g, x, p)  # Public Key (Distributed to the web frontend)

def encrypt_vote(candidate_id: int):
    """
    Frontend operation: Encrypts the vote integer in the browser/client.
    candidate_id must be < p.
    """
    if candidate_id >= p:
        raise ValueError("Candidate ID must be smaller than the prime p")
        
    k = random.randint(2, p-2)
    c1 = pow(g, k, p)
    
    # Encrypt the integer directly
    c2 = (candidate_id * pow(y, k, p)) % p
    
    return (c1, c2)

def decrypt_vote(cipher: tuple):
    """
    Backend operation: Decrypts to recover the candidate integer.
    """
    c1, c2 = cipher
    
    # Calculate shared secret 's'
    s = pow(c1, x, p)
    
    # Find modular multiplicative inverse of s
    # In Python 3.8+, pow(base, -1, mod) handles this cleanly
    s_inv = pow(s, -1, p)
    
    # Recover original candidate integer
    m = (c2 * s_inv) % p
    return m

# --- Demonstration ---
print("--- Secure Voting Demo ---")
# 1. Voter selects Candidate 42
original_vote = 42 
print(f"Original Vote: Candidate {original_vote}")

# 2. Frontend encrypts the vote before sending to database
encrypted_ballot = encrypt_vote(original_vote)
print(f"Encrypted Ballot (Stored in DB): {encrypted_ballot}")

# 3. Backend (or Election Authority) decrypts the ballot
recovered_vote = decrypt_vote(encrypted_ballot)
print(f"Recovered Vote: Candidate {recovered_vote}")
