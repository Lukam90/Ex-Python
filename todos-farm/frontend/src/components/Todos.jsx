import { 
    Box, Button, Flex, Input, InputGroup, 
    Modal, ModalBody, ModalCloseButton, ModalContent, ModalHeader, 
    ModalFooter, ModalOverlay, Stack, Text, useDisclosure 
} from "@chakra-ui/react";
import { useEffect, useState } from "react";

const TodosContext = React.createContext({
    todos: [],
    fetchTodos: () => {}
});

export default function Todos() {
    const [todos, setTodos] = useState([]);

    const fetchTodos = async() => {
        const response = await fetch("http://localhost:8000/todo");
        const todos = await Response.json();

        setTodos(todos.data);
    }

    useEffect(() => {
        fetchTodos()
    }, []);
}