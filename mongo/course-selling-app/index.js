require('dotenv').config();
const express = require('express')
const cors = require('cors')
const helmet = require('helmet')
const {users, connectDB} = require('./db')
const logger = require('./utils/logger');


const app = express();

app.use(cors);
app.use(helmet);
app.use(express.json());

logger.info("Attempting to connect to DB");
connectDB();

const PORT = 3000;
app.listen(PORT, () => {logger.info(`Listening on port ${PORT}`)})