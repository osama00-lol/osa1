class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.status = "Available"

    def check_out(self):
        if self.status == "Available":
            self.status = "Checked Out"
            return True
        return False

    def check_in(self):
        if self.status == "Checked Out":
            self.status = "Available"
            return True
        return False

    def summary(self):
        return f"[{self.item_id}] {self.title} by {self.author} - {self.status}"
class LibraryCatalog:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print("❌ Item with this ID already exists.")
        else:
            self.items[item.item_id] = item
            print("✅ Item added successfully.")

    def check_out_item(self, item_id):
        if item_id in self.items:
            if self.items[item_id].check_out():
                print("📕 Item checked out.")
            else:
                print("⚠️ Item already checked out.")
        else:
            print("❌ Item not found.")

    def check_in_item(self, item_id):
        if item_id in self.items:
            if self.items[item_id].check_in():
                print("📗 Item checked in.")
            else:
                print("⚠️ Item already available.")
        else:
            print("❌ Item not found.")

    def show_all_items(self):
        for item in self.items.values():
            print(item.summary())
            
class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def summary(self):
        return f"[{self.item_id}] Book: {self.title} by {self.author} - {self.num_pages} pages - {self.status}"

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, run_time):
        super().__init__(title, director, item_id)
        self.run_time = run_time

    def summary(self):
        return f"[{self.item_id}] DVD: {self.title} by {self.author} - {self.run_time} min - {self.status}"
def main():
    catalog = LibraryCatalog()

    while True:
        print("\n📚 Community Library System")
        print("1. Add New Item")
        print("2. Check Out Item")
        print("3. Check In Item")
        print("4. Show All Items")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item_type = input("Enter type (book/dvd): ").lower()
            title = input("Title: ")
            author = input("Author/Director: ")
            item_id = input("Item ID: ")

            if item_type == "book":
                pages = input("Number of pages: ")
                new_item = Book(title, author, item_id, pages)
            elif item_type == "dvd":
                runtime = input("Run time (minutes): ")
                new_item = DVD(title, author, item_id, runtime)
            else:
                new_item = LibraryItem(title, author, item_id)

            catalog.add_item(new_item)

        elif choice == "2":
            item_id = input("Enter item ID to check out: ")
            catalog.check_out_item(item_id)

        elif choice == "3":
            item_id = input("Enter item ID to check in: ")
            catalog.check_in_item(item_id)

        elif choice == "4":
            catalog.show_all_items()

        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
if __name__ == "__main__":
    main()