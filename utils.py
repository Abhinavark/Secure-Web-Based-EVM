import hashlib
import os
import secrets

def hash_password(password: str) -> dict:
    """
    Creates a secure, salted, and stretched hash for a new voter.
    """
    # 1. The Salt: Generate 32 bytes of cryptographically secure random data
    salt = os.urandom(32) 
    
    # 2. The Work Factor: Run SHA-256 100,000 times
    # This creates a microsecond delay that destroys brute-force attempts
    iterations = 100000 
    
    # 3. The Hash: Combine the password, salt, and iterations using PBKDF2
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        iterations
    )
    
    # You must store the salt AND the iterations alongside the hash in your database
    return {
        'salt': salt.hex(),
        'hash': hashed_password.hex(),
        'iterations': iterations
    }

def verify_password(stored_password_dict: dict, provided_password: str) -> bool:
    """
    Verifies a login attempt against the stored database values.
    """
    # 1. Retrieve the unique salt and iterations used for this specific user
    salt = bytes.fromhex(stored_password_dict['salt'])
    stored_hash = stored_password_dict['hash']
    iterations = stored_password_dict['iterations']
    
    # 2. Hash the new login attempt using the EXACT SAME parameters
    new_login_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        provided_password.encode('utf-8'), 
        salt, 
        iterations
    ).hex()
    
    # 3. Security Check: Use compare_digest to prevent Timing Attacks
    return secrets.compare_digest(stored_hash, new_login_hash)

# --- Demonstration ---
print("--- Secure Voter Registration ---")
voter_password = "secure_voting_password_2026"

# Simulating saving a user to the database
db_record = hash_password(voter_password)
print(f"Stored Salt: {db_record['salt'][:15]}...") 
print(f"Stored Hash: {db_record['hash'][:15]}...")

print("\n--- Secure Voter Login ---")
# Simulating a correct login attempt
is_valid = verify_password(db_record, "secure_voting_password_2026")
print(f"Correct password login successful? {is_valid}")

# Simulating an incorrect login attempt
is_invalid = verify_password(db_record, "wrong_password")
print(f"Wrong password login successful? {is_invalid}")
