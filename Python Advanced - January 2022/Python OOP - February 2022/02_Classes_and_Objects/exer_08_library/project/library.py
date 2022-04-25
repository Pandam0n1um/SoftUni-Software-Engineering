from project.user import User


class Library:
	def __init__(self, ):
		self.user_records = []
		self.books_available = {}
		self.rented_books = {}

	def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
		if book_name in self.books_available[author]:
			user.books.append(book_name)
			self.books_available[author].remove(book_name)
			if user.username not in self.rented_books:
				self.rented_books[user.username] = {}
			self.rented_books[user.username][book_name] = days_to_return

			return f"{book_name} successfully rented for the next {days_to_return} days!"

		for user, books in self.rented_books.items():
			if book_name in books:
				return f"The book \"{book_name}\" is already rented and will be available in {books[book_name]} days!"

	def return_book(self, author: str, book_name: str, user: User):
		if book_name not in user.books:
			return f"{user.username} doesn't have this book in his/her records!"
		user.books.remove(book_name)
		self.rented_books[user.username].pop(book_name)
		self.books_available[author].append(book_name)
#
# def add_user(self, user):
# 	for existing_user in self.user_records:
# 		if existing_user.user_id == user.user_id:
# 			return f"User with id = {user.user_id} already registered in the library!"
# 	self.user_records.append(user)
# 	self.rented_books[user.username] = {}
#
# def remove_user(self, user):
# 	if user in self.user_records:
# 		self.user_records.remove(user)
# 	else:
# 		return f"We could not find such user to remove!"
#
# def change_username(self, user_id: int, new_username: str):
# 	for user in self.user_records:
# 		if user.user_id == user_id:
# 			if user.username == new_username:
# 				return "Please check again the provided username - it should be different than the username used so far!"
# 			#
# 			# user.username = new_username
# 			rented_books = self.rented_books[user.username]
# 			self.rented_books.pop(user.username)
# 			user.username = new_username
# 			self.rented_books[user.username] = rented_books
# 			return f"Username successfully changed to: {new_username} for userid: {user_id}"
#
# 	return f"There is no user with id = {user_id}!"
