const express = require('express');
const app = express();

//middleware to parse json
app.use(express.json());

app.get('/', (req, res) => {
    res.send("Hello World")
})

app.post('/samplepost', (req, res) => {
    const body = req.body
    res.json({'yousent': body})
})

app.listen(3000, ()=>{console.log("Server running on port 3000")});