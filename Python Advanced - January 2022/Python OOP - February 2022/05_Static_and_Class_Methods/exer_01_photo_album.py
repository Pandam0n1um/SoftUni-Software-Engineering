from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__build_photos()

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for row_idx, row in enumerate(self.photos):
            if len(row) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[row_idx].append(label)
                return f"{label} photo added successfully on page {row_idx + 1} slot {len(row)}"
        return "No more free slots"

    def __build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([])
        return result

    def display(self):
        PAGE_SEPARATOR = '-' * 11
        result = PAGE_SEPARATOR + '\n'
        for row in self.photos:
            result += ' '.join(['[]' for _ in row])+'\n'
            result+=PAGE_SEPARATOR+'\n'

        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())