# replacing a old damain with new domain in a company who just updated their domainname

def replace(email, old_domain, new_domain):
    username = ""
    if '@' + old_domain in email:
        index = email.index("@")

        return str(email[:index] + "@" + new_domain)
    return email


email = input("enter our email")
old_domain = input("enter your old domain")
new_domain = input("enter your new updated domain")

print(replace(email, old_domain, new_domain))

print("alpha".strip())
