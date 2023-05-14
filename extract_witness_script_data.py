from bitcoinlib.transactions import Transaction, Input, Signature, Key

# Create a transaction input
input_obj = Input(prevout_hash='previous_txid', prevout_n=0, script=b'input_script')

# Create a transaction
tx = Transaction(version=1, locktime=0)

# Set the inputs for the transaction
tx.inputs = [input_obj]

# Get the input script
input_script = tx.inputs[0].script

# Extract the signature values
signature = input_script.signature.decode()
signature_obj = Signature.from_der(signature)
r = signature_obj.r
s = signature_obj.s
z = tx.signature_hash(0, input_script, hash_type=Transaction.SIGHASH_ALL)

# Recover the public key
public_key = Key.recover_public_key_from_signature(z, signature)
