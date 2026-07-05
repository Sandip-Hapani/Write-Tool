# with open("server/prompts/keywords.prompt") as f:
#   prompt = f.read()


str = """
    What is Bitcoin? Bitcoin is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries. Transactions are verified by network nodes through cryptography and recorded in a public distributed ledger called a blockchain. Bitcoin was invented by an unknown person or group of people under the name Satoshi Nakamoto and released as open-source software in 2009.\n\nWhat is cryptocurrency? A cryptocurrency is a digital or virtual currency that is secured by cryptography, making it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers. A defining feature of cryptocurrencies is that they  are generally not issued by any central authority, rendering them immune to government interference or manipulation.\n\nWhat is blockchain? A blockchain is a digital ledger of all  cryptocurrency transactions. It is constantly growing as "completed" blocks are added to it with a new set of recordings. Each block contains a cryptographic hash of the previous block, a  timestamp, and transaction data. Bitcoin nodes use the block chain to differentiate legitimate Bitcoin transactions from attempts to re-spend coins that have already been spent elsewhere.
  """

print(str.split(".")[-4:])