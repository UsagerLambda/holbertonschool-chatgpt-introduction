class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Le montant doit être positif.")
            return
        self.balance += amount
        print("Déposé ${:.2f}".format(amount))
        print("Solde actuel: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Le montant doit être positif.")
            return
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retiré ${:.2f}".format(amount))
            print("Solde actuel: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Solde actuel: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (déposer, retirer, solde, quitter) : ").strip().lower()
        if action == 'quitter':
            break
        elif action == 'déposer':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                cb.deposit(amount)
            except ValueError:
                print("Veuillez entrer un montant valide.")
        elif action == 'retirer':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                cb.withdraw(amount)
            except ValueError:
                print("Veuillez entrer un montant valide.")
        elif action == 'solde':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
