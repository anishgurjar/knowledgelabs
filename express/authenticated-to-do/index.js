const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const jwt = require('jsonwebtoken');
const JWT_SECRET = "anish123";

const app = express();
const users = [];

app.use(cors());
app.use(helmet());
app.use(express.json());

app.post('/signup', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;
    if (!username || !password){
        return res.status(400).send("Invalid Input")
    }
    users.push({"username": username, "password": password})
    return res.status(200).send("Username and password created");
})

app.post('/signin',(req, res) => {
    const username = req.body.username;
    const password = req.body.password;
    if (!username || !password){
        return res.status(400).send("Invalid Input")
    }
    const userObj = users.find((user) => user.username === username && user.password === password)
    if (!userObj){ return res.status(403).send("Either username or password is invalid") }
    const token = jwt.sign({"username": userObj.username}, JWT_SECRET);
    return res.status(200).json({"token": token})
})

//auth middleware
function authenticate(req, res, next){
    const token = req.headers['authorization'];
    if (!token){ return res.status(400).send("Invalid Response")}
    const user = jwt.verify(token, JWT_SECRET);
    if (!user){ return res.status(400).send("Invalid token")}
    req.user = user
    next();
}

const todos = []
app.post('/addtodos', authenticate, (req, res) => {
    const todo = req.body
    if(!todo.id || !todo.task){ return res.status(400).send("Invalid Payload")}
    todos.push(todo)
    return res.status(200).send("Successfully added todo")
})

app.post('/gettodos', authenticate, (req, res) => {
    return res.status(200).json(todos)
})

app.get('/gettodo/:id', authenticate, (req, res) => {
    const id = req.params.id
    const item = todos.find((todo) => todo.id === id)
    if (!item){ return res.status(404).send("Todo not found")}
    return res.status(200).json(item)
})

app.delete('/deletetodo/:id', authenticate, (req, res) => {
    const id = req.params.id
    const itemIndex = todos.findIndex((todo) => todo.id === id)
    if (itemIndex === -1){ return res.status(404).send("Todo not found")}
    todos.splice(itemIndex, 1)
    return res.status(200).json(todos)
})

const PORT = 3000
app.listen(PORT, () => console.log(`Listening on Port ${PORT}`))