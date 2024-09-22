class Node:
    def __init__(self,title, artist, ):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None
class playlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,title, artist, position):
        new_song = Node(title,artist)
        if self.head is None:
            self.head = new_song
            self.tail = new_song

        elif position == 0:
           new_song.next = self.head
           self.head.prev = new_song
           self.head = new_song
        else:
            current = self.head
            for _ in range(position-1):
                if current.next is None:
                    break
                current = current.next
            new_song.next = current.next
            current.prev = new_song
            if current.next:
                current.next = new_song
            else:
                self.tail = new_song
                current.next = new_song

    def display(self):
        current = self.head
        while current:
            print(current.title,current.artist, end=" ")
            current = current.next

P = playlist()
P.add("Song A", "Artist 1", 0)
P.add("Song B", "Artist 2", 1)
P.add("Song C", "Artist 3", 1)
P.display()



