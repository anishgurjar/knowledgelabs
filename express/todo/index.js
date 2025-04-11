const express = require("express");
const app = express();

app.use(cors());
app.use(helmet());
app.use(express.json());

//custom logger middleware
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    //call next here if needed
})

let todo = [];

app.get('/', (req, res) => {
    res.json(todo);
});

app.get('/todo/:id', (req, res) => {
    const id = req.params.id;
    if (!id || !id.trim()) return res.status(400).send("Invalid ID");
    const itemIndex = todo.findIndex((item) => item.id === id);
    if (itemIndex === -1) return res.status(404).send("Todo item not found");
    return res.status(200).json(todo[itemIndex]);
});

app.post('/addTodo', (req, res) => {
    const item = req.body;
    if (!item.id || !item.task) return res.status(400).send("Invalid payload");
    todo.push(item);
    res.status(201).json(todo);
});

app.delete('/deleteTodo/:id', (req, res) => {
    const id = req.params.id;
    const itemIndex = todo.findIndex((item) => item.id === id);
    if (itemIndex === -1) return res.status(404).send("Todo item not found");
    todo.splice(itemIndex, 1);
    res.status(200).json(todo);
});

const PORT = 3000;
app.listen(PORT, () => { console.log(`Server Started, Listening on Port ${PORT}`); });