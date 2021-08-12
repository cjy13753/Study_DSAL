import java.util.LinkedList;
import java.util.ListIterator;

public class LinkedListStack {

    public static void main(String[] args) {

        Employee janeJones = new Employee("Jonh", "Doe", 4567);
        Employee johnDoe = new Employee("Mary", "Smith", 22);
        Employee marySmith = new Employee("Jane", "Jones", 123);
        Employee mikeWilson = new Employee("Mike", "Wilson", 3245);
        Employee billEnd = new Employee("Bill", "End", 78);

        LinkedStack stack = new LinkedStack();
        stack.push(janeJones);
        stack.push(johnDoe);
        stack.push(marySmith);
        stack.push(mikeWilson);
        stack.push(billEnd);

//        stack.printStack();

//        System.out.println(stack.peek());
//        stack.printStack();

        System.out.println("Popped: " + stack.pop());
        System.out.println(stack.peek());
    }

    public static class LinkedStack {
        private LinkedList<Employee> stack;

        public LinkedStack() {
            stack = new LinkedList<>();
        }

        public void push(Employee employee) {
            stack.push(employee);
        }

        public Employee pop() {
            return stack.pop();
        }

        public Employee peek() {
            return stack.peek();
        }

        public boolean isEmpty() {
            return stack.isEmpty();
        }

        public void printStack() {
            ListIterator<Employee> iterator = stack.listIterator();
            while (iterator.hasNext()) {
                System.out.println(iterator.next());
            }
        }
    }

    public static class Employee {

        private String firstName;
        private String lastName;
        private int id;

        public Employee(String firstName, String lastName, int id) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.id = id;
        }

        public String getFirstName() {
            return firstName;
        }

        public void setFirstName(String firstName) {
            this.firstName = firstName;
        }

        public String getLastName() {
            return lastName;
        }

        public void setLastName(String lastName) {
            this.lastName = lastName;
        }

        public int getId() {
            return id;
        }

        public void setId(int id) {
            this.id = id;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Employee employee = (Employee) o;

            if (id != employee.id) return false;
            if (!firstName.equals(employee.firstName)) return false;
            return lastName.equals(employee.lastName);
        }

        @Override
        public int hashCode() {
            int result = firstName.hashCode();
            result = 31 * result + lastName.hashCode();
            result = 31 * result + id;
            return result;
        }

        @Override
        public String toString() {
            return "Employee{" +
                    "firstName='" + firstName + '\'' +
                    ", lastName='" + lastName + '\'' +
                    ", id=" + id +
                    '}';
        }
    }
}
