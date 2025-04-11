const express = require('express')
const cors = require('cors');
const helmet = require('helmet');
const crypto = require('crypto');
const jwt = require('jsonwebtoken')

const JWT_SECRET = "Anish123"

const app = express();

//security middlewares
app.use(cors())
app.use(helmet())
app.use(express.json())

//in memory users array
let users = []

function auth(req, res, next) {
    const token = req.headers['authorization'];
    const user = jwt.verify(token, JWT_SECRET);
    req.user = user;
    if (!user){ return res.status(403).send("Invalid creds")}
    next();
}

app.post('/signup', (req, res) => {
    const userName = req.body.userName;
    const password = req.body.password; //input validation can be improved with zod
    users.push({"userName": userName, "password": password});
    res.status(200).send("Sign up successful");
})

app.post('/signin', (req, res) => {
    const userName = req.body.userName;
    const password = req.body.password;
    console.log(users);
    const userCreds = users.find((authObject) => authObject.userName === userName && authObject.password === password);
    if (!userCreds) { 
        return res.status(401).send("Either username or password is invalid");
    }
    const token = jwt.sign({"userName": userName}, JWT_SECRET)
    return res.status(200).json({"token": token});
})

//creating an authenticated endpoint
app.use('/me', auth, (req, res) => {
    res.status(200).json(req.user);
});

const PORT = 3000

app.listen(PORT, () => {console.log(`Listening on port ${PORT}`)});