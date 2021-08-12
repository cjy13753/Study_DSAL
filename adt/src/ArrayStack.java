import java.util.EmptyStackException;

public class ArrayStack {

    public static void main(String[] args) {

        Stack stack = new Stack(10);

        stack.push(new Employee("Jane", "Jones", 123));
        stack.push(new Employee("Jonh", "Doe", 4567));
        stack.push(new Employee("Mary", "Smith", 22));
        stack.push(new Employee("Mike", "Wilson", 3245));
        stack.push(new Employee("Bill", "End", 78));

//        stack.printStack();

        System.out.println(stack.peek());

//        stack.printStack();

        System.out.println("Popped: " + stack.pop());

        System.out.println(stack.peek());


    }

    public static class Stack {
        private Employee[] stack;
        private int top;

        public Stack(int capacity) {
            stack = new Employee[capacity];
        }

        public void push(Employee employee) {
            if (top == stack.length) {
                 // need to resize the backing array
                Employee[] newArray = new Employee[2 * stack.length];
                System.arraycopy(stack, 0, newArray, 0, stack.length);
                stack = newArray;
            }

            stack[top++] = employee;
        }

        public Employee pop() {
            if (isEmpty()) {
                throw new EmptyStackException();
            }

            Employee employee = stack[--top];
            stack[top] = null;

            return employee;
        }

        public Employee peek() {
            if (isEmpty()) {
                throw new EmptyStackException();
            }

            return stack[top - 1];
        }

        public int size() {
            return top;
        }

        public void printStack() {
            for (int i = top - 1; i >= 0; i--) {
                System.out.println(stack[i]);
            }
        }

        public boolean isEmpty() {
            return top == 0;
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
