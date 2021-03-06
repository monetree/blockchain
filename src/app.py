genesis_block = {
    'previous_hash' : '',
    'index'         : 0,
    'transaction'   : []
}
blockchain = [genesis_block]
open_transactions=[]
owner = 'Sobhagya'
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
def get_transaction_value():
    recipient = input("Enter recipient of transaction: : ")
    amount    = float(input("Your transaction amount please: "))
    return recipient,amount

def add_transaction(recipient,amount=1.0,sender=owner):
    transaction = {
        'sender'    : sender,
        'recipient' : recipient,
        'amount'    : amount
    }
    open_transactions.append(transaction)
def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    block = {
        'previous_hash' : hashed_block,
        'index'         : len(blockchain),
        'transaction'   : open_transactions
    }
    blockchain.append(block)

def get_user_choice():
    return input("Your choice: ")
def print_blockchain_elements():
    for block in blockchain:
        print('outputting block')
        print(block)
        print('-' * 20)
def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index -1]:
            is_valid = True
        else:
            is_valid = False
    return is_valid
waiting_for_input = True
while waiting_for_input:
    print('please choice')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        recipient,amount = get_transaction_value()
        add_transaction(recipient,amount=amount)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'q':
        waiting_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print('input is invalid *************Try again!!!')
    # if not verify_chain():
    #     print('hh')
    #     print_blockchain_elements()
    #     print('Well try to break breakchain !!')
    #     break
else:
    print('user left!')
print('Done !!')
