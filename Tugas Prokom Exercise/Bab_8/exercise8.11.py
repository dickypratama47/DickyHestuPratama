def show_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

messages = ["Halo!", "Apa kabar?", "Semoga sukses selalu."]
sent_messages = []

show_messages(messages[:], sent_messages)
print("\nList awal:", messages)
print("List terkirim:", sent_messages)