const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const jwt = require('jsonwebtoken');
const JWT_SECRET = "anish123";
const {UserModel, TodoModel, conenctDB} = require('./db');
const app = express();

app.use(cors());
app.use(helmet());
app.use(express.json());

conenctDB();

app.post('/signup', async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) {
        return res.status(400).send("Invalid Input");
    }
    await UserModel.create({ username, password });
    return res.status(200).send("Username and password created");
});

app.post('/signin', async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) {
        return res.status(400).send("Invalid Input");
    }
    const userObj = await UserModel.findOne({ username, password });

    if (!userObj) {
        return res.status(403).send("Either username or password is invalid");
    }
    const token = jwt.sign({ id: userObj._id }, JWT_SECRET);
    return res.status(200).json({ token });
});

// Auth middleware
function authenticate(req, res, next) {
    const token = req.headers['authorization'];
    if (!token) {
        return res.status(400).send("Invalid Response");
    }
    try {
        const user = jwt.verify(token, JWT_SECRET);
        req.user = user;
        next();
    } catch (error) {
        return res.status(400).send("Invalid token");
    }
}

app.post('/addtodos', authenticate, async (req, res) => {
    const { title } = req.body;
    if (!title) {
        return res.status(400).send("Invalid Payload");
    }
    
    await TodoModel.create({ title, "done?": false, userID: req.user.id });
    return res.status(200).send("Successfully added todo");
});

app.get('/gettodos', authenticate, async (req, res) => {
    const todos = await TodoModel.find({ userID: req.user.id });
    return res.status(200).json(todos);
});

app.get('/gettodo/:id', authenticate, async (req, res) => {
    const id = req.params.id;
    const item = await TodoModel.findById(id);
    if (!item) {
        return res.status(404).send("Todo not found");
    }
    return res.status(200).json(item);
});

app.delete('/deletetodo/:id', authenticate, async (req, res) => {
    const id = req.params.id;
    const result = await TodoModel.findByIdAndDelete(id);
    if (!result) {
        return res.status(404).send("Todo not found");
    }
    return res.status(200).json({ message: "Todo deleted successfully" });
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Listening on Port ${PORT}`));