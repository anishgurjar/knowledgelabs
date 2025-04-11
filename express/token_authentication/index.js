const express = require('express')
const cors = require('cors');
const helmet = require('helmet');
const crypto = require('crypto');

const app = express();

//security middlewares
app.use(cors())
app.use(helmet())
app.use(express.json())

//in memory users array
let users = []


function auth(req, res, next) {
    const token = req.headers['authorization'];
    if (!token) {
        return res.status(401).send("Unauthorized");
    }
    const user = users.find((user) => user.token === token);
    if (!user) {
        return res.status(401).send("Invalid Auth");
    }
    req.user = user; // do not do this ideally 
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
    console.log(userCreds);
    if (!userCreds) { 
        return res.status(401).send("Either username or password is invalid");
    }
    const token = crypto.randomBytes(32).toString('hex');
    userCreds['token'] = token;
    return res.status(200).json({"token": token});
})

//creating an authenticated endpoint
app.use('/me', auth, (req, res) => {
    res.status(200).json(req.user);
});

const PORT = 3000

app.listen(PORT, () => {console.log(`Listening on port ${PORT}`)});