from BlockChain import BlockChain


def main():
    blockchain = BlockChain()

    print("***Mining kyleCoin about to start***")
    print(blockchain.chain)

    data = [{"sender": "0",  # it implies that this node has created a new block
             "receiver": "Kyle Galloway",
             # creating a new block (or identifying the proof number) is awarded with 1
             "quantity": 1
             },
            {"sender": "Jack Daniels", "receiver": "Kyle Galloway", "quantity": 3},
            {"sender": "Kyle Galloway", "receiver": "Jack Daniels", "quantity": 2}]

    for datum in data:
        last_block = blockchain.latest_block
        last_proof_no = last_block.proof_no
        proof_no = blockchain.proof_of_work(last_proof_no)

        blockchain.new_data(
            sender=datum["sender"],
            receiver=datum["receiver"],
            quantity=datum["quantity"],
        )

        last_hash = last_block.calculate_hash
        # block = blockchain.construct_block(proof_no, last_hash)
        blockchain.construct_block(proof_no, last_hash)

        print("***Mining kyleCoin has been successful***")
        print(blockchain.chain)


if __name__ == "__main__":
    main()
