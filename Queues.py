class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.head == None:
           self.head = new_node
           self.tail = new_node
        else:
           self.tail.next = new_node
           self.tail = new_node
    
    def dequeue(self): 
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

            if self.head == None:
               self.tail = None
    
    def has_elements(self):
        return self.head != None


class PrinterTasks:
  def __init__(self):
    self.queue = Queue()
      
  def add_document(self, document):
    # Add the document to the queue
    self.queue.enqueue(document)
      
  def print_documents(self):
    # Iterate over the queue while it has elements
    while self.queue.has_elements():
      # Remove the document from the queue
      print("Printing", self.queue.dequeue())

#example:
printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()

#using queue module
import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue
my_orders_queue.get()