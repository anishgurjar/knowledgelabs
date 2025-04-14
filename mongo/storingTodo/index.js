const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const jwt = require('jsonwebtoken');
const JWT_SECRET = "anish123";
const { UserModel, TodoModel, connectDB } = require('./db'); // Fixed typo in 'connectDB'
const app = express();
const bcrypt = require('bcrypt');
const { z } = require('zod');

app.use(cors());
app.use(helmet());
app.use(express.json());

connectDB(); // Fixed typo in 'connectDB'

app.post('/signup', async (req, res) => {
    // enforce body schema using zod
    const requiredBody = z.object({
        username: z.string().min(1, "Username is required"),
        password: z.string()
            .min(7, "Password must be at least 7 characters long")
            .regex(/[A-Z]/, "Password must contain at least one uppercase letter")
            .regex(/[0-9]/, "Password must contain at least one number")
            .regex(/[\W_]/, "Password must contain at least one special character")
            .nonempty("Password is required")
    }).refine(data => data.username.trim() !== '', {
        message: "Username is required",
        path: ["username"],
    });

    const parsedData = requiredBody.safeParse(req.body);

    if (!parsedData.success) {
        return res.json({
            "message": "Incorrect Format",
            "error": parsedData.error
        });
    }

    const { username, password } = parsedData.data; // Extract username and password from parsed data
    const passwordHash = await bcrypt.hash(password, 10);
    await UserModel.create({ username, password: passwordHash });
    return res.status(200).send("Username and password created");
});

app.post('/signin', async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) {
        return res.status(400).send("Invalid Input");
    }
    const userObj = await UserModel.findOne({ username });

    if (!userObj) {
        return res.status(403).send("Either username or password is invalid");
    }

    const passwordMatch = await bcrypt.compare(password, userObj.password);

    if (!passwordMatch) {
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