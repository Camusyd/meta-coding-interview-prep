// Practica_LinkedList.java
// Implementación básica de un Nodo y una Lista Enlazada Simple en Java

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head; // El puntero al primer nodo

    // Inserción al inicio (O(1))
    public void insertAtHead(int data) {
        Node newNode = new Node(data);
        newNode.next = head; // El nuevo nodo apunta a la cabeza antigua
        head = newNode;      // El nuevo nodo se convierte en la nueva cabeza
    }

    // Recorrer e imprimir la lista (O(n))
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

public class Practica_LinkedList {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        
        list.insertAtHead(3);
        list.insertAtHead(2);
        list.insertAtHead(1); // Lista: 1 -> 2 -> 3 -> null

        System.out.print("Lista Enlazada: ");
        list.display();
    }
}