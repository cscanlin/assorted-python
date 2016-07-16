import os
from os.path import basename, dirname, join, getsize
import sys
import shutil

class DuplicateFinder(object):
    ignore = frozenset(['Cover.jpg', 'AlbumArtSmall.jpg', 'Folder.jpg', 'Thumbs.db',
                        'desktop.ini', 'READ ME FIRST.txt', 'ReadMe.txt', 'readme.txt'])

    def __init__(self, drive, option, destination=os.path.expanduser('F:\\moved')):
        self.drive = drive
        self.option = option
        self.destination = destination
        self.seen_files = set()
        self.file_list = []
        self.file_duplist = []
        self.dir_duplist = []
        self.total_size = 0
        self.moved = 0
        self.not_moved = 0

    def files_in_directory(self):
        for (directory, __, files) in os.walk(self.drive):
            for filename in files:
                if filename not in self.ignore:
                    yield join(directory, filename)

    def add_dupes_to_duplists(self):
        self.file_duplist.append(basename(self.current_file))
        if dirname not in self.dir_duplist:
            self.dir_duplist.append(dirname(self.current_file))
            print("\nFolder: {0}".format(dirname(self.current_file)))

    def move_file(self):
        try:
            print("Moving: {0}".format(basename(self.current_file)), end=" ... ")
            shutil.move(self.current_file, self.destination)
            print("-=MOVED=-")
            self.moved += 1
        except shutil.Error:  # You should change this to catch a specific Exception
            self.not_moved += 1
            print("!!! File already exists !!!")

    def delete_file(self):
        print("Deleting: " + basename(self.current_file), end=" ... ")
        os.remove(self.current_file)
        print("-=DELETED=-")

    def run(self):
        for self.current_file in self.files_in_directory():
            # List/Move/Delete file if file is a duplicate
            if basename(self.current_file) in self.seen_files:
                self.total_size += getsize(self.current_file)
                self.add_dupes_to_duplists()

                # List all duplicate files in the given path
                if self.option == "-list":
                    print("    {}".format(basename(self.current_file)))
                elif self.option == "-move":
                    self.move_file()
                elif self.option == "-delete":
                    self.delete_file()

            if basename(self.current_file) not in self.file_list:
                self.seen_files.add(basename(self.current_file))
                self.file_list.append(basename(self.current_file))

    def stats(self):
        stats = """
            ..........................................
            {len_seen_files} total files on drive.
            {len_dir_duplist} directories have duplicates.
            {len_file_duplist} duplicate files.\tSize: {total_size_formatted}
            """.format(
            len_seen_files=len(self.seen_files),
            len_dir_duplist=len(self.dir_duplist),
            len_file_duplist=len(self.file_duplist),
            total_size_formatted=int(self.total_size / 1000000000),
        )

        if self.option == "-move":
            stats += """
            {self.moved} duplicate files moved to:\t{self.destination}
            {self.not_moved} files not moved""".format(self=self)
        return stats

out_path = os.path.join(dirname(os.path.abspath(__file__)), 'out_folder')
df = DuplicateFinder(drive=sys.argv[1], option=sys.argv[2], destination=out_path)
df.run()
print(df.stats())
