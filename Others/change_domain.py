def change_domain(email, old_domain, new_domain):
    index = email.index("@")
    domain = email[index+1:]
    if domain == old_domain:
        new_email = email[:index] + "@" + new_domain
        return new_email

print(change_domain("fabricio@coisa.com", "coisa.com", "lindo.com"))
print(change_domain("jose.carlos@coisa.com", "coisa.com", "lindo.com"))
print(change_domain("francis@coisa.com", "scoisa.com", "lindo.com"))
