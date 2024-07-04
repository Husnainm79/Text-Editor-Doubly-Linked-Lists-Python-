#===================================
#===================================
# Name   : husnain
# Roll no: 261933726
# Section: 
# Date   : 
#===================================
#===================================


#------------------------------------
# Node class for a Doubly Linked List
#------------------------------------
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

#------------------------------------
class TextProcessor:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.document = None   # The root of everything. See page 2 for details
        
        # Cursor position, initialized to (-1, -1) indicating invalid cursor
        self.cursor = (-1, -1)
        
    def move_cursor_to(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        if row < 0 or col < 0:
            return  # Ignore negative values
        
        # If document is None, create the first row
        if self.document is None:
            self.document = ListNode(ListNode(' '))
        
        # Traverse rows until we reach the desired row
        current_row = self.document
        while row > 0 and current_row.next:
            current_row = current_row.next
            row -= 1
        
        # Create new rows if needed
        while row > 0:
            current_row.next = ListNode(ListNode(' '), current_row)
            current_row = current_row.next
            row -= 1
        
        # Now we're at the desired row, traverse columns
        current_col = current_row.data
        while col > 0 and current_col.next:
            current_col = current_col.next
            col -= 1
        
        # Create new columns if needed
        while col > 0:
            current_col.next = ListNode(' ', current_col)
            current_col = current_col.next
            col -= 1
        
        # Update cursor position
        self.cursor = (row, col)
        
    def move_forward(self):
        '''
        Moves the cursor one step forward
 
        Parameters:
            None
        
        Return value:
            None
        '''
        # Check if cursor is invalid
        if self.cursor == (-1, -1):
            return
        
        row, col = self.cursor
        
        # Move forward within the same line
        if col < len(self.document.data) - 1:
            col += 1
        # Move to next line
        elif self.document.next:
            self.document = self.document.next
            row += 1
            col = 0
        
        # Update cursor
        self.cursor = (row, col)
        
    def move_back(self):
        '''
        Moves the cursor one step backwards
 
        Parameters:
            None
        
        Return value:
            None
        '''
        # Check if cursor is invalid
        if self.cursor == (-1, -1):
            return
        
        row, col = self.cursor
        
        # Move backward within the same line
        if col > 0:
            col -= 1
        # Move to previous line
        elif self.document.prev:
            self.document = self.document.prev
            row -= 1
            col = len(self.document.data) - 1
        
        # Update cursor
        self.cursor = (row, col)
        
    def move_to_start(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        # Check if cursor is invalid
        if self.cursor == (-1, -1):
            return
        
        row, _ = self.cursor
        self.cursor = (row, 0)
        
    def move_to_end(self):
        '''
        Moves the cursor to the end of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        # Check if cursor is invalid
        if self.cursor == (-1, -1):
            return
        
        row, _ = self.cursor
        # Move to the last column of the current row
        col = len(self.document.data) - 1
        self.cursor = (row, col)
        
    def insert_text(self, string):
        '''
        Inserts the given string immediately after the cursor
 
        Parameters:
            a string
        
        Return value:
            None
        '''
        # Check if cursor is invalid
        if self.cursor == (-1, -1):
            self.move_cursor_to(0, 0)  # If cursor is invalid, move it to (0, 0)
        
        row, col = self.cursor
        
        # Traverse to the current row
        current_row = self.document
        while row > 0 and current_row.next:
            current_row = current_row.next
            row -= 1
        
        # Traverse to the current column
        current_col = current_row.data
        while col > 0 and current_col.next:
            current_col = current_col.next
            col -= 1
        
        # Insert the string at the cursor position
        for char in string:
            new_node = ListNode(char, current_col)
            if current_col.next:
                new_node.next = current_col.next
                current_col.next.prev = new_node
            current_col.next = new_node
            current_col = new_node
        # Update cursor to point to the last inserted character
        self.cursor = (row, col + len(string))
        
    def delete_characters(self, num):
        '''
        Deletes specified number of characters from the cursor position
 
        Parameters:
            integer number of characters to delete
        
        Return value:
            None
        '''
        # Check if cursor is invalid
        if self.cursor == (-1, -1):
            return
        
        row, col = self.cursor
        
        # Traverse to the current row
        current_row = self.document
        while row > 0 and current_row.next:
            current_row = current_row.next
            row -= 1
        
        # Traverse to the current column
        current_col = current_row.data
        while col > 0 and current_col.next:
            current_col = current_col.next
            col -= 1
        
        # Delete characters starting from the cursor position
        while num > 0 and current_col.next:
            current_col.next = current_col.next.next
            if current_col.next:
                current_col.next.prev = current_col
            num -= 1
        
    def count_characters(self):
        '''
        Counts the total number of characters in the document
 
        Parameters:
            None
        
        Return value:
            integer: total number of characters in the document
        '''
        count = 0
        current_row = self.document
        while current_row:
            current_col = current_row.data
            while current_col:
                count += 1
                current_col = current_col.next
            current_row = current_row.next
        return count
        
    def count_lines(self):
        '''
        Count total of non-empty lines in the document.
 
        Parameters:
            None
        
        Return value:
            integer: number of non-empty lines in the document
        '''
        count = 0
        current_row = self.document
        while current_row:
            if current_row.data.next:  # Check if the row is non-empty
                count += 1
            current_row = current_row.next
        return count
        
    def print_document(self):
        '''
        Prints the entire document on the screen.
        '''
        current_row = self.document
        while current_row:
            current_col = current_row.data
            while current_col:
                print(current_col.data, end="")
                current_col = current_col.next
            print()  # Newline for the next row
            current_row = current_row.next

#======================
#======================
#
#    DRIVER FUNCTION
#
#======================
def text_editor_driver():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    print("Welcome to My Text Editor")
    print("Enter commands at the prompt")
    print("Use 'quit' command to exit")

    editor = TextProcessor()

    while True:
        command = input(">> ").strip()

        if command == "quit":
            print("Exiting text editor...")
            break

        commands = command.split("\n")
        
        for cmd in commands:
            tokens = cmd.split()
            
            if len(tokens) == 3 and tokens[0] == "goto":
                row, col = int(tokens[1]), int(tokens[2])
                editor.move_cursor_to(row, col)

            elif len(tokens) > 0:
                if tokens[0] == "forward":
                    editor.move_forward()

                elif tokens[0] == "back":
                    editor.move_back()

                elif tokens[0] == "home":
                    editor.move_to_start()

                elif tokens[0] == "end":
                    editor.move_to_end()

                elif tokens[0] == "insert":
                    string = " ".join(tokens[1:])
                    editor.insert_text(string)

                elif tokens[0] == "delete":
                    if len(tokens) > 1:
                        num = int(tokens[1])
                        editor.delete_characters(num)
                    else:
                        print("Invalid command!")

                elif tokens[0] == "count_characters":
                    count = editor.count_characters()
                    print("Total number of characters:", count)

                elif tokens[0] == "count_lines":
                    count = editor.count_lines()
                    print("Total number of non-empty lines:", count)

                elif tokens[0] == "print_document":
                    print("Printing document:")
                    editor.print_document()

                else:
                    print("Invalid command!")
            else:
                print("Invalid command!")

if __name__ == '__main__':
    text_editor_driver()
