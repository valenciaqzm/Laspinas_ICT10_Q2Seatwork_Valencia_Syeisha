from pyscript import document

club_members = ["Josua Ortiz", "Sasha Valenci", "Maria Santos", "Juan Dela Cruz"]

def check_name(event):
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()
    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    document.querySelector("#result").innerText = messages[is_member]
