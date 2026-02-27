# Secure-Web-Based-EVM
Prototype secure electronic voting system demonstrating authentication, hash-linked vote storage, and integrity verification.
## Cryptographic Design

This prototype incorporates ElGamal encryption to provide vote confidentiality in addition to integrity protection.

Voting workflow:

1. Voter authenticates
2. Vote choice is encrypted using ElGamal public key
3. Encrypted vote is stored with SHA-256 hash
4. Hash verification detects tampering
5. Duplicate voting prevented per voter

This demonstrates core security properties of electronic voting:

- Confidentiality — ElGamal encryption
- Integrity — cryptographic hashing
- Authentication — voter login
- Duplicate prevention — vote checks

Note: Educational prototype with simplified parameters.

# How to run?
-pip install flask
-python3 app.py

open browser: http://127.0.0.1:5000

## Demonstration

### Server Running
Flask backend hosting the secure voting application.

![Server](screenshots/server.png)

### Voter Authentication Interface
Login page for credential verification.

![Login](screenshots/login.png)

### Vote Submission Interface
Authenticated voter submitting candidate selection.

![Vote](screenshots/vote.png)

### Vote Recorded Confirmation
Successful vote recording after encrypted and integrity-protected storage.

![Success](screenshots/success.png)
