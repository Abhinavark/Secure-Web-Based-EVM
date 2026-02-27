import hashlib

def hash_vote(vote_data: str) -> str:
    return hashlib.sha256(vote_data.encode()).hexdigest()

def verify_hash(vote_data: str, stored_hash: str) -> bool:
    return hash_vote(vote_data) == stored_hash
