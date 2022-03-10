class NameTooShortError(Exception):
	pass


class MustContainAtSymbolError(Exception):
	pass


class InvalidDomainError(Exception):
	pass


VALID_DOMAINS = (
	'.com',
	'.bg',
	'.org',
	'.net',
)


def is_domain_invalid(domain: str, VALID_DOMAINS):
	result = True
	for valid_domain in VALID_DOMAINS:
		if domain.endswith(valid_domain):
			result = False
			return result
	return result


while True:
	is_valid = False
	email = input()
	if email == "End":
		break

	if "@" not in email:
		raise MustContainAtSymbolError("Email must contain @")

	username, domain = email.split("@")

	if len(username) < 5:
		raise NameTooShortError("Name must be more than 4 characters")

	if is_domain_invalid(domain, VALID_DOMAINS):
		raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

	print("Email is valid")